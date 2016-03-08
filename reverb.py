# Reverb
# Using a series of all pass filters

from pyo import *

pa_list_devices()
s = Server(audio='portaudio', nchnls=1)
s.setInputDevice(0)
s.setOutputDevice(1)
s.boot()
s.start()
a = Input(chnl=0).out()


print a
# pa = pyaudio.PyAudio()
# stream = self.open_mic_stream()
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# INPUT_BLOCK_TIME = 0.05
# INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)

# device_index = find_input_device()
# stream = pa.open(format = FORMAT, channels = CHANNELS, rate = RATE, 
# 	input = true, input_device_index = device_index, 
# 	frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

# while 1:
# 	try:
# 		block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
# 	except IOError, e:
# 		print("Error recording input")


# read some audio file (real-time tbd)

# determine greatest delay value and store that number of values
# most efficent way to remove an item from one side of an array and add it to the other?


# Sample at some reasonable rate
# compute all pass filtered components (assuming signal has lasted long enough) and add
# play current audio


