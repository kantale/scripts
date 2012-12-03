import os
import re
import sys
import urllib2

constants = {
	'GRIDROOT' : 'srm://srm.grid.sara.nl/pnfs/grid.sara.nl/data/bbmri.nl/RP2/resources/imputationReference/gonl_release3.1',
	'USERNAME' : 'akanterakis',
	'REMOTEHOST' : 'clustervp',
	'CLUSTERDIR' : '/target/gpfs2/gcc/resources/imputationReference/gonl_release3.1',
	'TMPDIR' : 'tmptransfer',
	'HOMEDIR' : '/home/kanterak',
}

def list_files(dir_name):
	command = 'ssh %s@%s "ls -1dp --group-directories-first %s/*" > file_list.txt' % (constants['USERNAME'], constants['REMOTEHOST'], dir_name)
	print command
	os.system(command)
	return [x.replace('\n', '') for x in open('file_list.txt').readlines()]


def get_param(name, arguments, default):

	for argument in arguments:
		found = re.search(r'%s=(.*)' % (name), argument)
		if found:
			return found.group(1)

	return default


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
			dont_skip_this_dir = all([grid_file_name_dir_content[0:len(x)] != x for x in skip_dirs])

			if dont_skip_this_dir:
				command = 'srmmkdir %s' % (grid_file_name_dir)
				exec_command(command, dummy)
				copy_files(cluster_file_name[0:-1], grid_file_name_dir, dummy, skip_dirs)
			else:
				print 'Skipping dir:', grid_file_name_dir

		else:
			#This is a simple file
			cluster_file_name_last = os.path.split(cluster_file_name)[1]

			grid_file_name_dir = os.path.join(grid_root_dir, cluster_file_name_last)
			#Check if the file already exists on the grid:
			command = 'srmls %s' % (grid_file_name_dir)
			print command
			returned = os.system(command)
			if returned:

				#Move the file to temporary local
				command = 'scp %s@%s:%s %s' % (constants['USERNAME'], constants['REMOTEHOST'], cluster_file_name, os.path.join(constants['HOMEDIR'], constants['TMPDIR'], cluster_file_name_last))
				exec_command(command, dummy)

				#Copy file to grid
				command = 'srmcp -server_mode=passive file:///$HOME/%s %s' % (os.path.join(constants['TMPDIR'], cluster_file_name_last), grid_file_name_dir)
				exec_command(command, dummy)

				#Remove the file from temporary local
				command = 'rm %s' % (os.path.join(constants['HOMEDIR'], constants['TMPDIR'], cluster_file_name_last))
				exec_command(command, dummy)
			else:
				print 'File: ', grid_file_name_dir, 'already exists on the grid. Skip copying'

if __name__ == '__main__':

	#Example: python gridShare.py dummy=True skip=gonl_release3.1/jobs,gonl_release3.1/tmp 
 	dummy = eval(get_param('dummy', sys.argv, 'False'))
 	skip = get_param('skip', sys.argv, None)

 	for x in ['GRIDROOT', 'USERNAME', 'REMOTEHOST', 'CLUSTERDIR', 'TMPDIR', 'HOMEDIR']:
 		constants[x] = get_param(x, sys.argv, constants[x])

 	skip_dirs = []
 	if skip:
 		skip_dirs = [content_dirs(x) for x in skip.split(',')]

	copy_files(constants['CLUSTERDIR'], constants['GRIDROOT'], dummy, skip_dirs)

