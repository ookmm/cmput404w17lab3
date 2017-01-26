#!/usr/bin/env python

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

print "Content-Type: text/html"

# Set the Cookie
if username == "bob" and password == "mypass":
	print "Set-Cookie: loggedin=true"

print # ^^^^ HTTP ^^^^ vvvv HTML vvvv

print "<HTML><BODY>"
print "<H1>Hello World</H1>"

print "<P>Your magic number is: "
print form.getvalue('magic_tracking_number')
print "</P>"

print "<P>Your Browser is: "
if "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "Firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome!"
print "</P>"

# Show environment variables
#print json.dumps(dict(os.environ), indent=2, sort_keys=True)

print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

# Check if username and password are correct
print "<P>Username: " + str(username) + "</P>"
print "<P>Password: " + str(password) + "</P>"

if username == "bob" and password == "mypass":
	print "<P>Login successful</P>"

if 'loggedin' in C:
	print "<P>Logged in: " + str(C['loggedin'].value) + "</p>"
else:
	print "<P>No cookie</P>"

print "<P>" + os.environ['HTTP_COOKIE'] + "</P>"





print "</BODY></HTML>"