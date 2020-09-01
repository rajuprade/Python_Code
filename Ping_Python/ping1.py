#!/usr/bin/python 
import os
for ping in range(31,60):
   ip="192.168.%d.2" %ping
   os.system("ping -c 3 %s" % ip)
