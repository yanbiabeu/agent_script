#!/usr/bin/python3


import sys
import os
import requests
import subprocess


os.system('clear')
#ports = range(20,8000)
protocols = ['udp', 'tcp']

def usage():
   print("\nPlease provide two arguments: the port number and the protocol\n")
   print( "Example: python3 %s 80 tcp \n" %(sys.argv[0]))
   exit()

if len(sys.argv) != 3:
	usage()
else:

	PortPovided = int(sys.argv[1])
	ProtocolProvided = sys.argv[2]

if os.getuid() != 0:
      print("\nThis must be run as user root!!\n")
      exit()

elif  len(sys.argv) < 3 or len(sys.argv) > 3:
        usage()

elif PortPovided not in range(20,8000):
	print("\n\nplease provide a valide port number between 20 and 8000\n\n")
	#usage()
elif ProtocolProvided not in protocols:
	print("\nyou have provided an invalid protocol please choose between udp and tcp\n\n")
	#usage()
else:

	subprocess.call(["sed -i -e 's/hello/helloworld/g' /home/serge/serge"], shell=True)

#END
