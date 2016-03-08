# Python and PD interaction script
import os, sys

def volume(message=''):
	os.system("1 75 | pdsend 3000")

def dspOn():
	os.system("echo '0' | pdsend 3000")

if __name__ == "__main__":
	dspOn()