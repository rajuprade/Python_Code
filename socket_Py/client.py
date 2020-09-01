#!/usr/bin/python           # This is client.py file

# Works on Python

import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host ='192.168.8.45'
port = 5001               # Reserve a port for your service.

s.connect((host, port))
time.sleep(2)
print (s.recv(1024))
s.send('Client ACKNOWLEDGE')
s.close()                     # Close the socket when done
