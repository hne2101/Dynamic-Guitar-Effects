# Python and PD interaction script
from socket import *
import os, sys

if __name__ == "__main__":
	s = socket(AF_INET,SOCK_DGRAM)
	s.sendto('test;\n',('localhost',3001))
	s2 = socket(AF_INET,SOCK_DGRAM)
	s2.bind(('localhost',3000))
	while 1:
		data, addr = s2.recvfrom(1024)
		print 'received message: '+str(data)