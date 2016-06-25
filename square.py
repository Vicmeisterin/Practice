import wave
import numpy 
import scipy.io.wavfile as audio

square = wave.open("new.wav","wb")

sr = 48000
sampwidth = 1
nframes = sr * 5
nchan = 1
comptype = "NONE"
compname = ""

square.setparams((nchan, sampwidth, sr, nframes, comptype, compname))

pow16 = 2**16 / 2

for n in range(1200):
	data = numpy.zeros(300)
	square.writeframes(data * pow16);
	data = numpy.ones(300)
	square.writeframes(data * pow16);

square.close()
