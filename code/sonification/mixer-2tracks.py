import numpy as np
from wave_file import wave_read_16bit_mono
from wave_file import wave_write_16bit_stereo

track1FileName = "wav/big-dipper-treble-cmajor-piano.wav"
track2FileName = "wav/big-dipper-bass-cmajor-triad-piano.wav"
outputFileName = "wav/big-dipper-mixed-cmajor-piano-piano-triad.wav"

number_of_track = 2
fs = 44100
length_of_s_master = int(fs * 12)
# track = np.zeros((length_of_s_master, number_of_track))
# s_master = np.zeros((length_of_s_master, 1))

fs, s= wave_read_16bit_mono(track1FileName)
track = np.zeros((len(s), number_of_track))
s_master = np.zeros((len(s), 2))
track[:, 0] = s
print(len(s))

fs, s = wave_read_16bit_mono(track2FileName)
track[:, 1] = s
print(len(s))

v = np.array([1, 1])
p = np.array([0.5, 0.5])

for i in range(number_of_track):
    s_master[:, 0] += track[:, i] * v[i] * np.cos(np.pi * p[i] / 2)
    s_master[:, 1] += track[:, i] * v[i] * np.sin(np.pi * p[i] / 2)

master_volume = 0.9
s_master /= np.max(np.abs(s_master))
s_master *= master_volume

# for n in range(int(len(s) * 0.01)):
#     s_master[n, 0] = s_master[n, 0] * n/(fs * 0.01)
#     s_master[n, 1] = s_master[n, 1] * n/(fs  * 0.01)


wave_write_16bit_stereo(fs, s_master, outputFileName)
print(outputFileName)
