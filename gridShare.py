import os
import re
import sys
import urllib2


help = """
	Author: Alexandros Kanterakis
	email: alexandros.kanterakis@gmail.com

	python gridShare.py \
		GRIDROOT=srm://srm.grid.sara.nl/pnfs/grid.sara.nl/data/bbmri.nl/RP2/resources/imputationReference/gonl_release3.1 \
		CLUSTERDIR=/target/gpfs2/gcc/resources/imputationReference/gonl_release3.1 \
		USERNAME=akanterakis \
		REMOTEHOST=clustervp \
		TMPDIR=/home/kanterak/tmptransfer
	
	Notes: 
		USERNAME is the *cluster* username, REMOTEHOST is the *cluster* host and TMPDIR is a temporary directory in the *GRID*
		This script should run from GRID
		The GRID and CLUSTER should be configured to connect with SSH through shared pubic keys. 

	Additional options:
		dummy=True # Doesn't do anything. Just shows the commands that are supposed to be executed
		skip=gonl_release3.1/jobs,gonl_release3.1/tmp  # Comma separated list of dirs thay will be skipped from copying. Example values.
		delete=True # Deletes all the files in the grid that locates in the cluster. 
		change_permissions=RW,R,NONE 	#Changes permission to all the files in the grid that locates in the cluster. 
										The applied command for this example is: srm-set-permissions -type=CHANGE -owner=RW -group=R -other=NONE 

		To delete a complete directory on the grid (withour any involvement of a cluster dir) use:
		python gridShare.py GRIDROOT=<SRM DIRECTORY> delete_grid=True
"""

"""
Examples:
python gridShare.py GRIDROOT=srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1/ delete_grid=True
"""

constants = {
	'GRIDROOT' : 'srm://srm.grid.sara.nl/pnfs/grid.sara.nl/data/bbmri.nl/RP2/resources/imputationReference/gonl_release3.1',
	'USERNAME' : 'akanterakis',
	'REMOTEHOST' : 'clustervp',
	'CLUSTERDIR' : '/target/gpfs2/gcc/resources/imputationReference/gonl_release3.1',
	'TMPDIR' : '/home/kanterak/tmptransfer',
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

def copy_files(cluster_root_dir, grid_root_dir, dummy = False, skip_dirs = [], delete = False, change_permissions = False):
	cluster_file_list = list_files(cluster_root_dir)

	for cluster_file_name in cluster_file_list:
		print '-' * 20

		if cluster_file_name[-1] == '/':
			#This is a directory

			cluster_file_name_dir = os.path.split(cluster_file_name[0:-1])[1]
			grid_file_name_dir = os.path.join(grid_root_dir, cluster_file_name_dir)

			#Should we skip it?
			grid_file_name_dir_content = content_dirs(grid_file_name_dir)
			dont_skip_this_dir = all([grid_file_name_dir_content[0:len(x)] != x for x in skip_dirs])

			if dont_skip_this_dir:
				if delete:
					pass

					#Attention: The directory should be empty..
					#command = 'srmrmdir %s' % (grid_file_name_dir)
					#exec_command(command, dummy)

				elif change_permissions:
					command = 'srm-set-permissions -type=CHANGE %s %s' % (change_permissions, grid_file_name_dir)
					exec_command(command, dummy)

					command = 'srm-set-permissions -type=ADD -owner=X -group=X %s' % (grid_file_name_dir)
					exec_command(command, dummy)

				else:
					command = 'srmmkdir %s' % (grid_file_name_dir)
					exec_command(command, dummy)

					command = 'srm-set-permissions -type=CHANGE -owner=RWX -group=RX -other=NONE %s' % (grid_file_name_dir)
					exec_command(command, dummy)

				copy_files(cluster_file_name[0:-1], grid_file_name_dir, dummy, skip_dirs, delete, change_permissions)
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
			if returned and not delete and not change_permissions:

				#Move the file to temporary local
				command = 'scp %s@%s:%s %s' % (constants['USERNAME'], constants['REMOTEHOST'], cluster_file_name, os.path.join(constants['TMPDIR'], cluster_file_name_last))
				exec_command(command, dummy)

				#Copy file to grid
				command = 'srmcp -server_mode=passive file:///%s %s' % (os.path.join(constants['TMPDIR'], cluster_file_name_last), grid_file_name_dir)
				exec_command(command, dummy)

				#Appply permsissions
				command = 'srm-set-permissions -type=CHANGE -owner=RW -group=R -other=NONE %s' % (grid_file_name_dir)
				exec_command(command, dummy)

				#Remove the file from temporary local
				command = 'rm %s' % (os.path.join(constants['TMPDIR'], cluster_file_name_last))
				exec_command(command, dummy)
			else:
				if delete:
					print "Deleting file:", grid_file_name_dir
					command = 'srmrm %s' % (grid_file_name_dir)
					exec_command(command, dummy)

				elif change_permissions:
					print "Changing permissions to file:", grid_file_name_dir
					command = 'srm-set-permissions -type=CHANGE %s %s' % (change_permissions, grid_file_name_dir)
					exec_command(command, dummy)

				else:
					print 'File: ', grid_file_name_dir, 'already exists on the grid. Skip copying'

def delete_grid_dir(grid_dir, dummy=False):

	print 'Deleting dir:', grid_dir

	#Get preffix
	sub_dirs = content_dirs(grid_dir)
	last_two = sub_dirs[-2:]
	last_two.reverse()
	prefix = '//'.join(last_two)
	print 'Prefix is:', prefix

	#Get all the contents of this directory
	command = 'srmls %s > dir_contents' % (grid_dir)
	exec_command(command, dummy)

	#Read contents
	contents = [x for x in open('dir_contents').readlines()[1:] if len(x.strip()) > 1]
	for entry in contents:
		entry_name = entry.split()[1]
		full_entry_name = ''.join([prefix, entry_name])
		if full_entry_name[-1] == '/':
			#This is a directory
			delete_grid_dir(full_entry_name[0:-1], dummy=dummy)
		else:
			command = 'srmrm %s' % (full_entry_name)
			exec_command(command, dummy=dummy)

	command = 'srmrmdir %s' % (grid_dir)
	exec_command(command, dummy=dummy)


if __name__ == '__main__':

 	dummy = eval(get_param('dummy', sys.argv, 'False'))
 	skip = get_param('skip', sys.argv, None)
 	delete = eval(get_param('delete', sys.argv, 'False'))
 	change_permissions = get_param('change_permissions', sys.argv, '')
 	delete_grid = eval(get_param('delete_grid', sys.argv, 'False'))

 	for x in ['GRIDROOT', 'USERNAME', 'REMOTEHOST', 'CLUSTERDIR', 'TMPDIR']:
 		constants[x] = get_param(x, sys.argv, constants[x])

 	skip_dirs = []
 	if skip:
 		skip_dirs = [content_dirs(x) for x in skip.split(',')]

 	if change_permissions:
 		try:
	 		change_permissions =  ' '.join(map(lambda x: x[0] + x[1], zip(['-owner=', '-group=', '-other='], change_permissions.split(","))))
 		except Exception, e:
 			print 'Could not process parameter change_permissions. Example: RW,R,NONE '
 			raise e
 
 	if delete_grid:
 		delete_grid_dir(constants['GRIDROOT'], dummy)
	else:
		copy_files(constants['CLUSTERDIR'], constants['GRIDROOT'], dummy, skip_dirs, delete, change_permissions)

