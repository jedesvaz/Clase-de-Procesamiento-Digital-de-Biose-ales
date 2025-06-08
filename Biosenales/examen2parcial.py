# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:13:37 2021

@author: EV
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz,lfilter

fs=100
fl=8
fh=12

fln=fl/(fs/2)
fhn=fh/(fs/2)
AnchoTn=1/(fs/2)

N=6.6/AnchoTn
M=np.ceil(N)
n=np.arange(M+1)
w=0.54-0.46*np.cos(2*np.pi*n/M)
fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(n,w, label="Gráfica de la ventana")
ax.set(xlabel='No. de muestra', ylabel='Amplitud',
       title='Gráfica de la ventana Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
f2=fhn/2
f1=fln/2
n1=np.arange(-165,166)
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

f, H = freqz(h, fs=fs)
fig,[ax1, ax2] = plt.subplots(2,1, num= 'Figura 4', clear=True)
ax1.plot(f, abs(H))
ax2.plot(f, 20*np.log10(abs(H)))
ax1.set(xlabel= 'frecuencia en hz' , ylabel= 'amplitud',
       title= 'respuesta en frecuencia')
ax2.set(xlabel= 'frecuencia en Hz' , ylabel= 'amplitud en dB',
       title= 'respuesta en frecuencia')
ax1.grid()
ax2.grid()
plt.show()

#%% Filtro r. banda inversión espectral
hinvertida=-h
hinvertida[165]=hinvertida[165]+1

fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.stem(n1,hinvertida)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de filtro enventanado r. banda Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%%
frb,Hrb=freqz(hinvertida,fs=fs)
fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.plot(frb,abs(Hrb))
ax.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud (dB)',
       title='Respuesta en frecuencia de r. banda enventanado Jesus Espinoza')
ax.grid()
plt.show()
#%%EXTRA
N=300
n2=np.arange(N)
f0=5
A=1
T=1/fs
x=A*np.sin(2*np.pi*f0*n2*T)
tiempo=n2*T
fig, ax = plt.subplots(num='Figura 7',clear=True)
ax.plot(tiempo, x, color='orange', label="Gráfica de la señal original")
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud',
       title='Gráfica de la señal ')
y=lfilter(hinvertida,1, x)
ax.plot(tiempo, y, color='green', label="Gráfica de la señal filtrada")

ax.grid()
ax.legend()
plt.show()
