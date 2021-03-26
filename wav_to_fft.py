import soundfile

data, samplerate = soundfile.read('Burgh 2021 Final.wav')
soundfile.write('new.wav', data, samplerate, subtype='PCM_16')


import IPython.display as ipd
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

wav = 'download.wav'
sr, samps = read(wav)
ipd.Audio(samps, rate=sr)

# creating variables for clarification
samples_per_second = sr
total_samples = len(samps)
time_seconds = total_samples / samples_per_second
print("Sampling rate: ", samples_per_second)
print("Total number of samples: ", total_samples)
print("Total time in seconds: ", time_seconds)


import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('download.wav')
fft_out = fft(data)
plt.plot(data, np.abs(fft_out))
plt.show()