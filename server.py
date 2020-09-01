#!/usr/bin/python 

import socket # Import socket module
s = socket.socket() #
host = socket.gethostname() #
port = 1245 #
s.bind((host, port)) #
s.listen(5)
# Now wait for client connection.
while True:
	c, addr = s.accept()
# Establish connection with client.
	print 'Got connection from', addr
	c.send('Thank you for connecting')
        print c.recv(1024)
c.close()
# Close the connection

