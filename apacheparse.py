#!/usr/bin/python
import os
import sys
import re
import json
from optparse import OptionParser
import apacheformat

jsonout = {}
options = None
#p = OptionParser(usage="Usage: %prog -H <host> [<options>]", version=VERSION)
pparser = OptionParser(usage="Usage: %prog -f <file>")
pparser.add_option("-l", "--log", type="string", dest="log", help="read data from log filename")
pparser.add_option("-s", "--start", type="int", dest="StartNumber", help="Starting linenumber of log filename")
pparser.add_option("-e", "--end", type="int", dest="EndNumber", help="Ending linenumber of log filename")
pparser.add_option("-a", "--appname", type="string", dest="Appname", help="Add application name to log file")
pparser.add_option("-p", "--pattern", type="string", dest="Pattern", help="String to remove from log filename")
pparser.add_option("-r", "--remove", type="string", dest="Remove", help="Remove Column from log filename")
pparser.add_option("-f", "--format", type="string", dest="Format", help="Apache Log_Format")

(options, args) = pparser.parse_args()


if not options.log:
	print "File is missing"
	exit(1)
else:
	logfile = options.log
#	print logfile

f = open(logfile,'r').readlines()


if not options.StartNumber:
	s = 0
else:
	s = options.StartNumber
#	print s

if not options.EndNumber:
	e = len(f)
else:
	e = options.EndNumber
#	print e

if not options.Appname:
	print "Appname is mising"
	exit(1)
else:
	appname = options.Appname

if not options.Pattern:
	patt = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
else:
	patt = options.Pattern 
#    print patt

if not options.Format:
	print "Apache format missing, please enter apache log format"
	exit(1)
else:
	apacheformat = options.Format
#	print apacheformat
	aformat = apacheformat.logformat(apacheformat)
#	print aformat
	
if options.Remove:
	r = options.Remove
	if r not in aformat:
		print "remove should either of this"
		print aformat
		exit(1)

#	print aformat

count = len(aformat)

for l in range(s,e):
        line =	map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', f[l]))
        word = line
        word.append(appname)
        for z in range(count):
			jsonout[aformat[z]] = word[z]
	
	if options.Remove:
		apacheformat.remove_column(jsonout,r)

	for key,value in jsonout.items():
    		rword = jsonout[key]
    		match = re.search(patt,rword)
    		if match: 
    			jsonout[key] = '-'

    
	print json.dumps(jsonout)
