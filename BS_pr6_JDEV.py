# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:05:22 2021

@author: EV
"""

from scipy.io import loadmat #librería.módulo import función
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import butter, lfilter
from scipy.signal import freqz

datos = loadmat('SqW.mat')
fs=500
senal=datos['SqW']
T=1/fs
N=len(senal[0,:])
n=np.arange(N)
tiempo=n*T

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(tiempo,senal[0,:])
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal SqW -  Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% 3)
Xk=fft(senal[0,:],N)
k=np.arange(N)
fk=k*fs/N

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.stem(fk,abs(Xk))
ax.set(xlabel='fecuencia (Hz)', ylabel='Amplitud de la DFT',
       title='Espectro de señal SqW -  Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% ecg

datos1=np.loadtxt('ecg-pulso.txt')
fs=500
ecg=datos1[:,1]
N=len(ecg)
T=1/fs
n=np.arange(N)
tiempo=n*T

fig, ax = plt.subplots(num='Figura 3',clear=True)
ax.plot(tiempo,ecg)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud (mV)',
       title='Gráfica de señal ECG - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% DFT de ecg
N=2000
Xk1=fft(ecg,N)
k=np.arange(N)
fk=k*fs/N

fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.stem(fk,abs(Xk1))
ax.set(xlabel='tiempo (s)', ylabel='Amplitud (mV)',
       title='Espectro de señal ECG - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% ecg filtrada con filtro pasabanda de orden 2
fl=0.5 #frecuencia de corte baja
fh=40 #frecuencia de corte alta
fln=0.5/(fs/2)
fhn=40/(fs/2)
M=2
b,a=butter(M, [fln,fhn], btype='bandpass')

ecg_f=lfilter(b,a,ecg)
fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 5',clear=True)
ax1.plot(tiempo,ecg)
ax2.plot(tiempo, ecg_f)
ax1.set( ylabel='Amplitud (mV)',
       title='Gráfica de señal ECG - Valeria Chico y Jesus Espinoza')
ax2.set(xlabel='tiempo (s)', ylabel='Amplitud (mV)',
       title='Gráfica de señal ECG filtrada')
ax1.grid()
ax2.grid()
ax.legend()
plt.show()

#%% DFT de ecg filtrada
N=2000
Xk2=fft(ecg_f,N)
k=np.arange(N)
fk=k*fs/N

fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 6',clear=True)
ax1.stem(fk,abs(Xk1))
ax2.stem(fk, abs(Xk2))
ax1.set(ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG -Valeria Chico y Jesus Espinoza')
ax2.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG filtrada')
ax1.grid()
ax1.legend()
ax2.grid()
ax2.legend()


#%% Filtro pasa banda
[fh, H] = freqz( b, a, worN=1000, whole=False, fs=500)

fig, ax = plt.subplots(num='Figura 7',clear=True)
ax.plot(fh,abs(H))
ax.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud del espectro',
       title='Respuesta en frecuencia del Filtro orden 2 -Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% Filtros de 3 y 4 orden
M=3
b3,a3=butter(M, [fln,fhn], btype='bandpass')

ecg_f3=lfilter(b3,a3,ecg)

"""fig, (ax1) = plt.subplots(num='Figura X',clear=True)
ax1.plot(tiempo,ecg_f3)
ax1.set(xlabel='tiempo (s)', ylabel='Amplitud (mV)',
       title='Gráfica de señal ECG - Jesus Espinoza')"""


N=4
b4,a4=butter(N, [fln,fhn], btype='bandpass')

ecg_f4=lfilter(b4,a4,ecg)

# DFT De las señales filtradas de 3 y 4 orden
N=2000
Xk3=fft(ecg_f3,N)
k=np.arange(N)
fk=k*fs/N

Xk4=fft(ecg_f4,N)
k=np.arange(N)
fk=k*fs/N
#Módulos de los filtros de 3 y 4 orden
[fh3, H3] = freqz( b3, a3, worN=1000, whole=False, fs=500)
[fh4, H4] = freqz( b4, a4, worN=1000, whole=False, fs=500)

#Graficación de los señales filtradas, espectors y módulos de los filtros

fig, (ax1,ax3,ax5) = plt.subplots(nrows=3, ncols=1, num='Figura 8',clear=True)
fig.suptitle('Gráfica de las señal filtrada de 3 orden, espectro y módulo de filtro- Chico y Espinoza')

fig, (ax2,ax4,ax6) = plt.subplots(nrows=3, ncols=1, num='Figura 9',clear=True)
fig.suptitle('Gráfica de las señal filtrada de 4 orden, espectro y módulo de filtro- Chico y Espinoza')

ax1.plot(tiempo, ecg_f3, color='green')
ax1.set_ylabel('Amplitud (mV)')
ax1.set_xlabel('tiempo (s)')
ax1.grid()

ax2.plot(tiempo, ecg_f4, color='green')
ax2.set(xlabel='tiempo (s)', ylabel='Amplitud (mV)',
       title='señal ECG filtrada 4 orden')

ax3.stem(fk,abs(Xk3))
ax3.set(ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG filtrada 3 orden')



ax4.stem(fk,abs(Xk4))
ax4.set(ylabel='Amplitud de la DFT',
       title='Espectro de señal ECG filtrada 4 orden')


ax5.plot(fh3,abs(H3))
ax5.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud del espectro',
       title='Respuesta en frecuencia del Filtro orden 3')

ax6.plot(fh4,abs(H4))
ax6.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud del espectro',
       title='Respuesta en frecuencia del Filtro orden 4')