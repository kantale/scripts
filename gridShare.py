import os
import re
import sys

def get_param(name, arguments, default):

	for argument in arguments:
		found = re.search(r'%s=(.*)' % (name), argument)
		if found:
			return found.group(1)

	return default

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


if __name__ == '__main__':

	grid_root = get_param('grid_root', sys.argv, None)
	cluster_root = get_param('cluster_root', sys.argv, None)

	walker = copy_to_grid(grid_root, cluster_root)

	for command in walker:
		print command