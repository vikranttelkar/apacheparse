apacheparse
===========

Parse apache log file

Parse apache log file and provide output in json format.

./apacheparse.py -l test.log -a test -f "%h %l %u %t "%r" %>s %b"

This will prase apache log file and provide output in json format.
