# Rusn on PC, directly from Thonny
# The client
# Brendan McBride

import socket
s = socket.socket()
host = '10.102.13.210'# IP of the Raspberry Pi, running the server
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()
