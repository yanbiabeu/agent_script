#!/usr/bin/python3



import sys
import os
#import urllib2
import requests
import tarfile

def usage():
   print("\nPlease provide one argument: the kernel version\n")
   print( "Example: python3 %s 4.14.8 \n" %(sys.argv[0]))
   exit()

if os.getuid() != 0:
      print("\nThis must be run as user root!!\n")
      exit()

if  len(sys.argv) < 2 or len(sys.argv) > 2:
	usage()


print("\nThe argument you entered is: %s \n " %(sys.argv[1]))


Ans = input("Do you want to continue(y/n)? ")
while Ans.lower() not in ['y', 'n' ]:
	try:	
		print("\nInvalid choice, please enter y or n\n")
		Ans = input("Do you want to continue(y/n)? ")
	except KeyboardInterrupt:
		print("\nYou interrupted the code goodbye!!")
		os.system('sleep 2')
		exit()

if Ans == 'n':
       print("\nThank you and have a nice day\n")
       exit()
if Ans == 'y':   
       print("\n The kernel compilation will start soon please wait...\n")
Kernel_url ='https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-%s.tar.xz' %(sys.argv[1])

def WgetDown(pack):
	Kernel_url ='https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-%s.tar.xz' %(sys.argv[1])
	print('\n Downloading the  with wget ...')
	kernel = requests.get(Kernel_url)

try:
	kernel = requests.get(Kernel_url)
except ConnectionError:
	print("unable to download kernel package please double check that your version is a valid one")
	exit()

package = 'linux-%s.tar.xz' %(sys.argv[1])
open(package, 'wb').write(kernel.content) 
  
if kernel:
	print("Successfully download kernel package!!") 

try:
	extraction= tarfile.open(package)
	extraction.extractall()
except tarfile.ReadError:
	print("Unable to find the file to be extracted")


#sys.stderr.write('Failed\n')
#sys.stderr.flush()
#sys.stdout.write('Success\n')
#print(sys.argv[1])
#print(len(sys.argv))

