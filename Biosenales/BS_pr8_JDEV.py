# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:04:56 2021

@author: EV
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, iircomb, lfilter, butter #iircomb: filtro iir tipo peine
from scipy.fft import fft #fft:
from plot_zplane import zplane

datos=np.loadtxt('ecg-pulso.txt')
ecg=datos[:,1]
fs=500
Ts=1/fs
N=len(ecg)
n=np.arange(N)
tiempo=n*Ts

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(tiempo,ecg)
ax.set(xlabel='tiempo (s)', ylabel='Voltaje (mV)',
       title='Gráfica de señal de ECG - Valeria Chico y Jesús Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% 2)
Xk=fft(ecg,N)
k=np.arange(N)
fk=k*fs/N

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.stem(fk[0:N//2+1],abs(Xk[0:N//2+1]))#// Indica que el resultado de la division sea un dato entero
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG -  Valeria Chico y Jesús Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% 3
fln=0.1/(fs/2)
fhn=40/(fs/2)
M=4

b,a=butter(M, [fln,fhn], btype='bandpass') #filtro diseañado
ecg_f=lfilter(b,a,ecg)

fig, [ax1, ax2] = plt.subplots(2,1, num='Figura 3',clear=True)
ax1.plot(tiempo,ecg)
ax1.set( ylabel='Voltaje (mV)',
       title='Gráfica de señal de ECG - JDEV')
ax2.plot(tiempo, ecg_f)
ax2.set(xlabel='tiempo (s)', ylabel='Voltaje (mV)',title='Gráfica de señal de ECG filtrada - Valeria Chico y Jesús Espinoza')
ax1.grid()
ax2.grid()
ax.legend()
plt.show()

 
#%%3 b)
[fh, H] = freqz( b, a, worN=1000, fs=500)

fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.plot(fh,abs(H))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud', 
       title='Respuesta en frecuencia del filtro Butterworth -  Valeria Chico y Jesús Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%3 b)
fig, ax = plt.subplots(num='Figura 5',clear=True)
zplane(b,a)
#%%
Xk_f=fft(ecg_f,N)
k=np.arange(N)
fk=k*fs/N

fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.stem(fk[0:N//2+1],abs(Xk_f[0:N//2+1]))#// Indica que el resultado de la division sea un dato entero
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG filtrada-  Valeria Chico y Jesús Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%Filtro de peine
f0=50
bw=2
Q=f0/bw
b1,a1=iircomb(f0,Q,ftype='notch', fs=fs)

[fh,H1]=freqz(b1,a1,worN=1000, fs=500)
#%%
f0 = 50
bw = 2
Q = f0/bw

b1, a1 = iircomb(f0, Q, ftype='notch', fs=fs)

[fh, H1] = freqz(b1,a1, worN= 1000, fs=500)
fig, ax = plt.subplots(num= 'Figura 7', clear =False)
H1_dB = 20*np.log10(abs(H1))
ax.plot(fh, H1_dB)
ax.set(xlabel='frecuencia en Hz', ylabel ='amplitud en dB ',
       title = 'Respuesta en frecuencia del filtro peine')
ax.grid()
plt.show()

fig, ax= plt.subplots(num='figura 8', clear=False)
zplane(b1,a1)

ecg_f1 = lfilter(b1, a1, ecg)

fig, [ax1, ax2, ax3] = plt.subplots(3, 1, num= 'Figura 9', clear =False)
ax1.plot(tiempo, ecg)
ax2.plot(tiempo, ecg_f)
ax3.plot(tiempo, ecg_f1)
ax1.set(xlabel='tiempo (s)', ylabel ='voltaje(mV)',
       title = 'Grafica de una señal de ECG')
ax2.set(xlabel='tiempo(s)', ylabel ='voltaje(mV)',
       title = 'Grafica de la  señal de ECG filtrada con Butterworth')
ax3.set(xlabel='tiempo(s)', ylabel ='voltaje(mV)',
       title = 'Grafica de la  señal de ECG filtrada con peine')
ax.grid()
plt.show()


Xk_f1 = fft(ecg_f1, N)

fig, ax = plt.subplots(num= 'Figura 10', clear =False)
ax.plot(fk[0:N//2+1], abs(Xk_f1[0:N//2+1]))
ax.set(xlabel='frecuencia en Hz', ylabel ='amplitud de la DFT',
       title = 'Gráfica del espectro de la  señal de ECG filtrada con peine')
ax.grid()
plt.show()


ecg_f2 = lfilter(b1, a1, ecg_f)

fig, [ax1, ax2, ax3, ax4] = plt.subplots(4, 1, num= 'Figura 11', clear =False)
ax1.plot(tiempo, ecg)
ax2.plot(tiempo, ecg_f)
ax3.plot(tiempo, ecg_f1)
ax4.plot(tiempo, ecg_f2)
ax1.set(xlabel='tiempo (s)', ylabel ='voltaje(mV)',
       title = 'Gráfica de una señal de ECG')
ax2.set(xlabel='tiempo(s)', ylabel ='voltaje(mV)',
       title = 'Gráfica de la  señal de ECG filtrada con Butterworth')
ax3.set(xlabel='tiempo(s)', ylabel ='voltaje(mV)',
       title = 'Gráfica de la  señal de ECG filtrada con peine')
ax4.set(xlabel='tiempo(s)', ylabel ='voltaje(mV)',
       title = 'Gráfica de la  señal de ECG doble filtrada')
ax.grid()
plt.show()

