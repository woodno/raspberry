# DataInsert1.py

import socket 

host = "www.aplu.dx.am"
port = 80
remote_ip = socket.gethostbyname(host)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((remote_ip , port))
for x in range(1, 6):
    y = x * x
    request = "GET /insert.php?x=" + str(x) + "&y=" + str(y) + \
              " HTTP/1.1\r\nHost: " + host + "\r\n\r\n" 
    s.sendall(request)
print "Done"

