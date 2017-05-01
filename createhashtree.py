#!/usr/bin/python
###############################################################################
# Title   : createhashtree
# Purpose : Perform an MD5 hash on all files in the current directory
#           and subdirectories. Output as a JSON file, specified as parameter
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

###############################################################################

import os, hashlib, json, sys

print len(sys.argv)
if len(sys.argv) != 2:
	print "Syntax: createhashtree.py <results file.json>"
	sys.exit(0)
else:
	jsonfile = sys.argv[1]
current_dir = os.getcwd()
hashdict = {}
print current_dir
ctr = 0
for root,dirs,files in os.walk(current_dir):
	for f in files:
		ctr += 1
		current_file = os.path.join(root,f)
		H = hashlib.md5()
		
		with open(current_file) as FIN:
			H.update(FIN.read())
		relativefile = current_file.replace(current_dir + "/","")
		hashdict[H.hexdigest()] = relativefile 
		print "Ctr=" + str(ctr)

with open(jsonfile,"w") as outfile:
	outfile.write(json.dumps(hashdict, indent=4, sort_keys=False))
