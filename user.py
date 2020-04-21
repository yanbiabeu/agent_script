#!/bin/python


import os
import re

'''
old = raw_input( "What is the name of your old name? ")
new = raw_input( "What is the name of your new name?  ")
os.rename( old, new)
'''
#print(dir(os))
'''
print(os.listdir('/home/serge'))
print(os.stat('service.sh').st_size)
for dirpath, dirnames, filenames in os.walk('/home/serge'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()
'''
print(os.environ.get('UID'))



