import os
import re
import sys
import urllib2

constants = {
	'GRIDROOT' : 'srm://srm.grid.sara.nl/pnfs/grid.sara.nl/data/bbmri.nl/RP2/resources/imputationReference/gonl_release3.1',
	'CLUSTERROOT' : 'akanterakis@clustervp:/target/gpfs2/gcc/resources/imputationReference/gonl_release3.1',
	'USERNAME' : 'akanterakis',
	'REMOTEHOST' : 'clustervp',
	'CLUSTERDIR' : '/target/gpfs2/gcc/resources/imputationReference/gonl_release3.1',
	'TMPDIR' : 'tmptransfer',
	'HOMEDIR' : 'home/kanterak',
}

def list_files(dir_name):
	command = 'ssh %s@%s "ls -1dp --group-directories-first %s/*" > file_list.txt' % (constants['USERNAME'], constants['REMOTEHOST'], dir_name)
	print command
	os.system(command)
	return [x.replace('\n', '') for x in open('file_list.txt').readlines()]

def fetch_page(url):
	print "Fetching: " + url
	try:
		fp = urllib2.urlopen(url)
		ret = fp.read()
		fp.close()
	except urllib2.HTTPError:
		print '   FAIL import'
		ret = ''

	return ret

def fetch_page_l(url):
	return lambda : fetch_page(url)

gridShare_script_l = fetch_page_l('https://raw.github.com/georgebyelas/molgenis_apps/master/modules/compute/datatransfer/gridShare.sh')

def get_param(name, arguments, default):

	for argument in arguments:
		found = re.search(r'%s=(.*)' % (name), argument)
		if found:
			return found.group(1)

	return default

def fetch_gridShareScript():
	content = gridShare_script_l()

	content = re.sub(r'GRIDROOT="[\w\:\/\.]*"', r'GRIDROOT="%s"' % (constants['GRIDROOT']), content)
	content = re.sub(r'CLUSTERROOT="[\w\:\/\.\@]*"', r'CLUSTERROOT="%s"' % (constants['CLUSTERROOT']), content)

	open('gridShare.sh', 'w').write(content)

def walk_dir(currentDir):
    for root, dirs, files in os.walk(currentDir): # Walk directory tree
		for dir_name in dirs:
			yield 'dir', dir_name
		for f in files:
			yield 'file', os.path.join(root, f)

def print_dir(dir_name):
	walker = walk_dir(dir_name)

	for x,y in walker:
		print x,y

def copy_to_grid(root_name, dir_name):
	walker = walk_dir(dir_name)

	for kind, name in walker:
		if kind == 'dir':
			command = ' '.join(['srmmkdir', os.path.join(root_name, name)])
			yield command

		if kind == 'file':
			command = ' '.join(['getFile', os.path.join(root_name, name)])
			yield command

def all(a_list):
	'''
	This function is builtin in python >= 2.5 ...
	'''
	for x in a_list:
		if not x:
			return False

	return True

def exec_command(command, dummy=False):
	print 'Running:', command
	if not dummy:
		os.system(command)

def content_dirs(dir_name):
	"""
	This function can be simply defined as:
	content_dirs = lambda x : [os.path.split(x)[1]] + [content_dirs(os.path.split(x)[0])][0] if len(x) else []
	But python 2.4.3 (Grid version) does not support: expr if .. else
	"""
	if len(dir_name):
		return [os.path.split(dir_name)[1]] + [content_dirs(os.path.split(dir_name)[0])][0]
	else:
		return []


def copy_files(cluster_root_dir, grid_root_dir, dummy = False, skip_dirs = []):
	cluster_file_list = list_files(cluster_root_dir)

	for cluster_file_name in cluster_file_list:
		if cluster_file_name[-1] == '/':
			#This is a directory

			cluster_file_name_dir = os.path.split(cluster_file_name[0:-1])[1]
			grid_file_name_dir = os.path.join(grid_root_dir, cluster_file_name_dir)

			#Should we skip it?
			grid_file_name_dir_content = content_dirs(grid_file_name_dir)
			print skip_dirs
			
			skip_this_dir = all([grid_file_name_dir_content[0:len(x)] != x for x in skip_dirs])

			if skip_this_dir:
				print "Skipping dir: ", grid_file_name_dir
			else:
				command = 'srmmkdir %s' % (grid_file_name_dir)
				exec_command(command, dummy)

			copy_files(cluster_file_name[0:-1], grid_file_name_dir)
		else:
			#This is a simple file
			cluster_file_name_last = os.path.split(cluster_file_name)[1]

			#Move the file to temporary local
			command = 'scp %s@%s:%s %s' % (constants['USERNAME'], constants['REMOTEHOST'], cluster_file_name, os.path.join(constants['HOMEDIR'], constants['TMPDIR'], cluster_file_name_last))
			exec_command(command, dummy)

			grid_file_name_dir = os.path.join(grid_root_dir, cluster_file_name_last)

			command = 'srmcp -server_mode=passive file:///$HOME/%s %s' % (os.path.join(constants['TMPDIR'], cluster_file_name_last), grid_file_name_dir)
			exec_command(command, dummy)

if __name__ == '__main__':

	#Example: python gridShare.py dummy=True skip=gonl_release3.1/jobs,gonl_release3.1/tmp 
 	dummy = eval(get_param('dummy', sys.argv, 'False'))
 	skip = get_param('skip', sys.argv, None)

 	skip_dirs = []
 	if skip:
 		skip_dirs = [content_dirs(x) for x in skip.split(',')]

	copy_files(constants['CLUSTERDIR'], constants['GRIDROOT'], dummy, skip_dirs)

