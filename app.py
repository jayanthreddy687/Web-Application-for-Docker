#!/usr/Bin/python3

import cgi
import subprocess
print("content-tpe: text/html")
print()
f = cgi.FieldStorage()
cmd = f.getvalue('input')
op = subprocess.getoutput("sudo "+cmd)
print(op)