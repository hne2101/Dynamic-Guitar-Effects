# Start two processes. One executes start_pd.py, which opens the main pure data patch
# The other process creates socket communication between the pd patch and python

from multiprocessing import Process

if __name__ == "__main__":
	p = Process(target=execfile, args=("start_pd.py",))
	p.start()
	p.join(10)
	p2 = Process(target=execfile, args=("socket_udp.py",))
	p2.start()
	p2.join(10)