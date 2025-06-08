# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:05:49 2021

@author: EV
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
A=1
f0=10
fs=500
N=1000
n=np.arange(N)
T=1/fs
x1=A*np.sin(2*np.pi*f0*n*T)
tiempo=n*T

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(tiempo,x1, label="Señal X1")
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% B) x2


x2=1/3*A*np.sin(2*np.pi*3*f0*n*T)
fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.plot(tiempo,x1+x2, label="Señal X1+X2")
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1+x2 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% C) x3
x3=1/5*A*np.sin(2*np.pi*5*f0*n*T)
fig, ax = plt.subplots(num='Figura 3',clear=True)
ax.plot(tiempo,x1+x2+x3)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1+x2+x3 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% D) x4
x4=1/7*A*np.sin(2*np.pi*7*f0*n*T)
fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.plot(tiempo,x1+x2+x3)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1+x2+x3+x4 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% E) x5
x5=1/9*A*np.sin(2*np.pi*9*f0*n*T)
fig, ax = plt.subplots(num='Figura 5',clear=True)
ax.plot(tiempo,x1+x2+x3+x4+x5)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1+x2+x3+x4+x5 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% TODAS EN UNA
xi=x1
xii=x1+x2
xiii=x1+x2+x3
xiv=x1+x2+x3+x4
xv=x1+x2+x3+x4+x5
fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1, num='Figura X',clear=True)
fig.suptitle('Gráfica de las señales- Jesus Espinoza')
ax1.plot(tiempo,xi, color='green')
ax1.set_ylabel('amplitud')
ax1.grid()

ax2.plot(tiempo,xii, color='yellow')
ax2.set_ylabel('amplitud')
ax2.grid()

ax3.plot(tiempo,xiii, color='purple')
ax3.set_ylabel('amplitud')
ax3.grid()

ax4.plot(tiempo,xiv)
ax4.set_ylabel('amplitud')
ax4.grid()

ax5.plot(tiempo,xv, color='orange')
ax5.set_ylabel('amplitud')
ax5.set_xlabel('tiempo en s')
ax5.grid()
#%% G)
N1=1000
fx, Xf = signal.freqz(x1, worN=N1, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.stem(fx, abs(Xf))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% ESPECTROS DE X2-X5
N1=1000
fx2, Xf2 = signal.freqz(xii, worN=N1, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura X2',clear=True)
ax.stem(fx2, abs(Xf2))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2 - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

fx3, Xf3 = signal.freqz(xiii, worN=N1, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura X3',clear=True)
ax.stem(fx3, abs(Xf3))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2+X3 - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

fx4, Xf4 = signal.freqz(xiv, worN=N1, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura X4',clear=True)
ax.stem(fx4, abs(Xf4))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2+X3+X4 - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

fx5, Xf5 = signal.freqz(xv, worN=N1, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura X5',clear=True)
ax.stem(fx5, abs(Xf5))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2+X3+X4+X5 - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% G) análisis en frecuencia de x1+x2
fx, XfB = signal.freqz(x1+x2, worN=N, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura 7', clear=True)
ax.stem(fx, abs(XfB))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% análisis en frecuencia de x1+x2+x3
fx, XfC = signal.freqz(x1+x2+x3, worN=N, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura 8', clear=True)
ax.stem(fx, abs(XfC))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro X1+X2 Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% PRACTICA 5 Inciso I
x2new=1/2*A*np.sin(2*np.pi*2*f0*n*T)
x3new=1/3*A*np.sin(2*np.pi*3*f0*n*T)
x4new=1/4*A*np.sin(2*np.pi*4*f0*n*T)
x5new=1/5*A*np.sin(2*np.pi*5*f0*n*T)
#%% J)
fig, ax = plt.subplots(num='Figura 9',clear=True)
ax.plot(tiempo,x1+x2new+x3new+x4new+x5new)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal x1+x2+x3+x4+x5  modificadas - Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% L)

fx, Xfnew = signal.freqz(x1+x2new+x3new+x4new+x5new, worN=1000, whole=True, fs=500)

fig, ax = plt.subplots(num='Figura 10', clear=True)
ax.stem(fx, abs(Xfnew))
ax.set(xlabel='frecuencia (Hz)', ylabel='Amplitud',
       title='Gráfica de espectro x1+x2+x3+x4+x5  modificadas - Valeria Chico y  Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% M)
data = np.loadtxt('ecg-pulso.txt')
ecg = data[:,1]
N = len(ecg)
n = np.arange(N)
fs = 500
T = 1/fs
tiempo = n*T
fig, ax = plt.subplots(num='Figura 11', clear=True)
ax.plot(tiempo, ecg)
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud (mV)',
       title= 'Gráfica de señal de ECG - Valeria Chico y Jesús Espinoza')
ax.grid()
plt.show()

fx, XfM = signal.freqz(ecg, worN=N, whole=True, fs=500)
#%% N)
fig, ax = plt.subplots(num='Figura 12', clear=True)
ax.plot(fx, abs(XfM))
ax.set(xlabel='Frecuencia (Hz)', ylabel='Amplitud (mV)',
       title= 'Gráfica del espectro de la señal de ECG - Valeria Chico y Jesús Espinoza')
ax.grid()
plt.show()
