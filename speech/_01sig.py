# -*- coding: utf-8 -*-
'''
语音识别
'''
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, sigs = wf.read('../data2/freq.wav')
print('sample_rate: ',sample_rate)      # 采样频率
print(sigs.shape,sigs.dtype, sigs[:3])
sigs = sigs / 2 ** 15   # 与sigs.dtype=int16有关
times = np.arange(len(sigs)) / sample_rate
freqs = nf.fftfreq(len(sigs), d=1 / sample_rate)
ffts = nf.fft(sigs)
pows = np.abs(ffts)     # 能量大小
mp.figure('Audio Signal', facecolor='lightgray')
mp.title('Audio Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs, c='dodgerblue', label='Signal')
mp.legend()
mp.figure('Audio Frequency', facecolor='lightgray')
mp.title('Audio Frequency', fontsize=20)
mp.xlabel('Frequency', fontsize=14)
mp.ylabel('Power', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 能量与频率,频谱图
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered',label='Frequency')
mp.legend()
mp.show()
