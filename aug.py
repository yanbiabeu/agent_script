#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Reads afile in reverse')
parser.add_argument('filename', help='the file to be read')
parser.add_argument('--limit', '-l', type=int,help='the number of line to be reversed')
parser.add_argument('--version','-v', action='version', version='1.0 by Naveen', help='show the program version')

args = parser.parse_args()

with open(args.filename) as myfile:
	lines = myfile.readlines()

	for line in lines:
	 	print(line[::-1])


