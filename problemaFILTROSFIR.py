# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:10:16 2021

@author: EV
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
fl=25
fh=100
fs=500

fln=fl/(fs/2)
fhn=fh/(fs/2)
AnchoTn=20/(fs/2)
#Ventana Hanning 
#AnchoT de la Hanning =6.2*pi/N AnchoT más pequeños respecto a esta, hamming y blackman
#AnchoT Normalizado= 6.2/N
N=6.2/AnchoTn
print('Orden del filtro= ', np.ceil(N))#ceil() es para redondear para arriba 
M=np.ceil(N)
n=np.arange(M+1)
w=0.5*(1-np.cos(2*np.pi*n/M))

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(n,w, label="Gráfica de la ventana")
ax.set(xlabel='No. de muestra', ylabel='Amplitud',
       title='Gráfica de la ventana Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%   w=2*pi*frecuencia de corte
f2=fhn/2
f1=fln/2
n1=np.arange(-39,40)
hi=(2*f2*np.sin(n1*2*np.pi*f2))/(n1*2*np.pi*f2)-(2*f1*np.sin(n1*2*np.pi*f1))/(n1*2*np.pi*f1)
hi[n1==0]=2*(f2-f1)
fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.stem(n1,hi)
ax.set(xlabel='No. de muestra', ylabel='Amplitud',
       title='Gráfica de filtro p. banda Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%
h=w*hi #filtro enventanado
fig, ax = plt.subplots(num='Figura 3',clear=True)
ax.stem(n,h)
ax.set(xlabel='No. de muestra', ylabel='Amplitud',
       title='Gráfica de filtro p. banda enventanado Jesus Espinoza')
ax.grid()
plt.show()
#%%
f,H=freqz(h,fs=fs)
fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.plot(f,20*np.log10(abs(H)))
ax.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud (dB)',
       title='Respuesta en frecuencia de p. banda enventanado Jesus Espinoza')
ax.grid()
plt.show()
#%% Filtro r. banda inversión espectral
hinvertida=-h
hinvertida[39]=hinvertida[39]+1

fig, ax = plt.subplots(num='Figura 5',clear=True)
ax.stem(n1,hinvertida)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro enventanado r. banda Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
frb,Hrb=freqz(hinvertida,fs=fs)
fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.plot(frb,20*np.log10(abs(Hrb)))
ax.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud (dB)',
       title='Respuesta en frecuencia de r. banda enventanado Jesus Espinoza')
ax.grid()
plt.show()