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

def copy_files(cluster_root_dir, grid_root_dir):
	cluster_file_list = list_files(cluster_root_dir)

#	content_dirs = lambda x : [os.path.split(x)[1]] + [content_dirs(os.path.split(x)[0])][0] if len(x) else []

	for cluster_file_name in cluster_file_list:
		if cluster_file_name[-1] == '/':
			#This is a directory
			cluster_file_name_dir = os.path.split(cluster_file_name)[1]

			command = 'srmmkdir %s' % os.path.join((constants['GRIDROOT']), cluster_file_name_dir)

if __name__ == '__main__':

#	grid_root = get_param('grid_root', sys.argv, None)
#	cluster_root = get_param('cluster_root', sys.argv, None)

#	walker = copy_to_grid(grid_root, cluster_root)

#	fetch_gridShareScript()

#	for command in walker:
#		print command

	copy_files(constants['CLUSTERDIR'], constants['GRIDROOT'])

