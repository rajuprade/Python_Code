#!/usr/bin/python           # This is server.py file

# Works on Python-----

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host ='192.168.8.45'
port = 5001                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   cmd_string = raw_input("Enter the command:")
   c.send(cmd_string.encode())
   print (c.recv(1024))
   c.close()                # Close the connection
