#Info from https://realpython.com/python-http-server/
#The purpose of this code is to test the legocar button controls
#To start a web server go to a terminal and type....
#python3 -m http.server
#To call something in the directory call
#localhost:8080 will list the files in the directory
#localhost:8080/testScript.py
#This delivers everything but does not act as a python script
#create a new folder called cgi-bin under this directory
#start the webserver like this
#python3 -m http.server --cgi
#This tells the server to serve up .py pages using scripting instead of literals
#from a web browser call http://localhost:8000/cgi-bin/testScript3.py
#To find how to access this from any browser on the local network
#in the terminal type ipconfig /all
#Look for the lease obtaied field which should match
#when you started the server.
#So now the call could be for example
#http://192.168.0.209:8000/cgi-bin/testScript3.py


import os
from http.cookies import SimpleCookie
from random import choices

cookies = SimpleCookie(os.getenv("HTTP_COOKIE"))

try:
    visits = int(cookies["visits"].value) + 1
except KeyError:
    visits = 1

cookies["visits"] = str(visits)
cookies["visits"]["max-age"] = 5  # Expire after 5 seconds

print(
    f"""\
Content-Type: text/html
{cookies}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello from a CGI Script</title>
  <style>
    body {{
      background-color: #{"".join(choices("0123456789abcdef", k=6))};
    }}
  </style>
</head>
<body>
<h1>CGI Script: {os.getenv("SCRIPT_NAME")}</h1>
<p>You visited this page <b>{cookies["visits"].value}</b> times.</p>
<h2>Environment Variables</h2>
<ul>
  <li><b>CONTENT_TYPE:</b> {os.getenv("CONTENT_TYPE")}</li>
  <li><b>HTTP_USER_AGENT:</b> {os.getenv("HTTP_USER_AGENT")}</li>
  <li><b>QUERY_STRING:</b> {os.getenv("QUERY_STRING")}</li>
  <li><b>REQUEST_METHOD:</b> {os.getenv("REQUEST_METHOD")}</li>
</ul>
</body>
</html>"""
)