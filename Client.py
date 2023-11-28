# Rusn on PC, directly from Thonny
# The client

import socket
s = socket.socket()
host = ''# IP of the Raspberry Pi, running the server
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()