#Info from https://realpython.com/python-http-server/
#The purpose of this code is to test the legocar button controls
#To start a web server go to a terminal and type....
#python3 -m http.server
#To call something in the directory call
#localhost:8080/testScript.py
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