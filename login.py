#!/usr/bin/env python3

import cgi, cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os, secret
from http.cookies import SimpleCookies

s = cgi.FieldStorage()
username = s.getfirst("username") 
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE]")
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = get
print("Content-Type: text/html")
if form_ok:

print()

If not username and not password:
    print(login_page())
else 
