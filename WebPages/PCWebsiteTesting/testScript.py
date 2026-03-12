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
#from a web browser call http://localhost:8000/cgi-bin/testScript2.py
print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
<h1>Hello, World!</h1>
</body>
</html>"""
)