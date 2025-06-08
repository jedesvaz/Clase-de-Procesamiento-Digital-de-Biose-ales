# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:07:55 2021

@author: EV
"""

import numpy as np
from scipy.signal import freqz,lfilter
import matplotlib.pyplot as plt

fs=2000
fc=400
fcn=fc/(fs/2)

M=74
n=np.arange(M+1)
w=0.42-0.5*np.cos(2*np.pi*n/M)+0.08*np.cos(4*np.pi*n/M)

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(n,w, label="Grafica de la ventana")
ax.set(xlabel='No. de muestra', ylabel='Amplitud',
       title='Gráfica de la ventana Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%
fc1=fcn/2
n1=np.arange(-37,38)
hi=(2*fc1*np.sin(n1*2*np.pi*fc1))/(n1*2*np.pi*fc1)
hi[n1==0]=2*fc1

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.stem(n1,hi)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro ideal Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
h=hi*w
fig, ax = plt.subplots(num='Figura 3',clear=True)
ax.stem(n,h)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro enventanado Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%
f, H=freqz(h,fs=fs)
fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 4',clear=True)
ax1.plot(f,abs(H))
ax2.plot(f,20*np.log10(abs(H)))
ax1.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud',
       title='Respuesta en frecuencia Jesus Espinoza')
ax2.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud en dB',
       title='Respuesta en frecuencia  Jesus Espinoza')
ax1.grid()
ax1.legend()
plt.show()

ax2.grid()
ax2.legend()
#%% Inversión espectral
h2=-h
h2[37]=h2[37]+1 

fig, ax = plt.subplots(num='Figura 5',clear=True)
ax.stem(n,h2)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro enventanado p. altos Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
f, H2=freqz(h2,fs=fs)
fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 6',clear=True)
ax1.plot(f,20*np.log10(abs(H)))
ax2.plot(f,20*np.log10(abs(H2)))
ax1.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud',
       title='Respuesta en frecuencia de filtro p. bajos Jesus Espinoza')
ax2.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud en dB',
       title='Respuesta en frecuencia de filtro p. altos Jesus Espinoza')
ax1.grid()
ax1.legend()
plt.show()

ax2.grid()
ax2.legend()

#%%Reversión espectral
h3=((-1)**n)*h
fig, ax = plt.subplots(num='Figura 7',clear=True)
ax.stem(n,h3)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro enventanado p. altos (rev. espectral) - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
f, H3=freqz(h3,fs=fs)
fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 8',clear=True)
ax1.plot(f,20*np.log10(abs(H)))
ax2.plot(f,20*np.log10(abs(H3)))
ax1.set(ylabel='Amplitud',
       title='Respuesta en frecuencia de filtro p. bajos -Chico y Espinoza')
ax2.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud en dB',
       title='Respuesta en frecuencia de filtro p. altos (Rev. espectral)')
ax1.grid()
ax1.legend()
plt.show()

ax2.grid()
ax2.legend()

#%%
N=60
n2=np.arange(N)
f0=100
A=10
T=1/fs
x=A*np.sin(2*np.pi*f0*n2*T)
tiempo=n2*T
fig, ax = plt.subplots(num='Figura 9',clear=True)
ax.plot(n2, x, color='orange')
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud',
       title='Gráfica de la señal - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
y=lfilter(h,1, x)
ax.plot(n2, y, color='green')
#%%


fig, (ax1,ax2) = plt.subplots(2,1,num='Figura 10',clear=True)
ax1.plot(f,abs(H))
ax2.plot(f,np.angle(H)*180/np.pi)
ax1.set( ylabel='Amplitud',
       title='Respuesta en frecuencia - Valeria Chico y Jesus Espinoza')
ax2.set(xlabel='Frecuencia (Hz)', ylabel='Fase en grados',
       title=' Fase de respuesta en frecuencia de filtro p. bajos Chico y Espinoza')
ax1.grid()
ax1.legend()
plt.show()

ax2.grid()
ax2.legend()