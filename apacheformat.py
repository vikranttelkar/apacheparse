#!/usr/bin/python
import re
import os
import sys

#a = "%h %l %u %t "%r" %>s %b"			
def logformat(format):
	a = format
	b = a.split(' ')
	c = []
	d = len(b)
	e = { '%h':'Rhost', '%l':'Rlogin', '%u':'Ruser', '%t':'Time', '"%r"':'Response', '%>s':'Status', '%b':'Byte', '%{User-Agent}i':'Useragent','%{Referer}i':'Referer', }
	for x in range(d):
		if b[x] in e.keys():
        			c.append(e[b[x]])
        c.append('eventType')
        return c    
    

def remove_column(dict,key):
	del dict[key]
	return dict



