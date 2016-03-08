# Python and PD interaction script
from socket import *
import os, sys

def volume(message=''):
	os.system("1 75 | pdsend 3000")

def dspOn():
	s = socket(AF_INET,SOCK_STREAM)
	s.connect(('localhost',3000))
	s.send('10;\n')
	s.close()

if __name__ == "__main__":
	dspOn()