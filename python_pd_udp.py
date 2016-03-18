# Python and PD interaction script
from socket import *
import os, sys
from multiprocessing import Process

if __name__ == "__main__":
	p = Process(target=execfile, args=("start_pd.py",))
	p.start()
	p.join(10)
	p2 = Process(target=execfile, args=("socket_udp.py",))
	p2.start()
	p2.join(10)