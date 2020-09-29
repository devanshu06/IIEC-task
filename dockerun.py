#!/usr/bin/python3

print("content-type: text/html")
print()


import subprocess as sp
import cgi

form = cgi.FieldStorage()
#osname = input("enter your os name :")
osname =  form.getvalue("x")
imagename=  form.getvalue("i")

cmd = "sudo docker run -dit --name {0} {1}".format(osname,imagename)
output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0 :
    print(" Docker Image launched by Name {}. ".format(osname))
else:
    print(" some error : {} ".format(out))
