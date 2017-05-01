#!/usr/bin/python

import os, hashlib, json, sys

if len(sys.argv) != 3:
        print "Syntax: xxxxxx.py <source file.json> <dest file.json>"
        sys.exit(0)
else:
        srcfile = sys.argv[1]
	dstfile = sys.argv[2]

with open(srcfile) as sf:
    shashdict = json.loads(sf.read())

with open(dstfile) as df:
    dhashdict = json.loads(df.read())

for key in shashdict:
	if key in dhashdict:
		found=True
	else:
		print "Missing: " + shashdict[key]

