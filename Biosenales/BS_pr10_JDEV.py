# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:53:42 2021

@author: EV
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz,lfilter,firwin
import pandas as pd
from adapt_filt_lms import lms
from scipy.io import loadmat
datos=pd.read_excel('ECG_PRUEBA_1.xlsx', header=None, skiprows=8)
datos=np.array(datos)
tiempo=datos[:,0]
ecg=datos[:,1]

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(tiempo,ecg)
ax.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)',
       title='Gráfica de la señal Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
loc=0
scale=1
N=len(ecg)
ruido = np.random.normal(loc, scale, N)

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.plot(tiempo, ruido)
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud',
       title='Gráfica de la señal de ruido Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% Diseño de filtro FIR pasabajos con ventana Hamming
Ncoefs=10 #No. de coeficientes
M=Ncoefs-1#orden del filtro
cutoff=0.5 #frecuencia de corte normalizada
h = firwin(Ncoefs, cutoff, window='hamming', pass_zero='lowpass')
#%% implementación de filtro
senalfiltradaR=lfilter(h,1, ruido)

fig, ax = plt.subplots(num='Figura 3',clear=True)
ax.plot(tiempo,senalfiltradaR)
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud',
       title='Gráfica de la señal de ruido filtrada JDEV')

ax.grid()
ax.legend()
plt.show()

#%%Adición de señal de ruido filtrada a señal ECG
ecg_ruido=senalfiltradaR+ecg
fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.plot(tiempo,ecg_ruido)
ax.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)',
       title='Gráfica de la Adición de la señal de ECG y la señal de ruido filtrada JDEV')

ax.grid()
ax.legend()
plt.show()

#%%
fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 5', clear=True)
ax1.plot(tiempo, ecg, color='green')
ax2.plot(tiempo, ruido, color='purple')
ax3.plot(tiempo, ecg_ruido, color='orange')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal ECG JDEV')
ax2.set( ylabel= 'Amplitud',
       title= 'Señal de Ruido')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de ECG adicionada con Ruido')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
#%% c) 
d=ecg_ruido
x=ruido
alfa=0.01
M=9
y, e, w = lms(x, d, M, alfa)
#%% d)

fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 6', clear=True)
ax1.plot(tiempo, ecg, color='green')
ax2.plot(tiempo, ecg_ruido, color='purple')
ax3.plot(tiempo[0:len(e)], e, color='orange')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal ECG JDEV')
ax2.set( ylabel= 'Amplitud',
       title= 'Señal de de ECG adicionada con Ruido')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) ')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
#%%
datos=loadmat('ECG_60Hz')
d=datos['d1']
N=len(d)
n=np.arange(N)
fig, ax = plt.subplots(num='Figura 7',clear=True)
ax.plot(n,d)
ax.set(xlabel='No. de muestras', ylabel='Voltaje (mV)',
       title='Gráfica de la señal ECG- Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
fs=1000
T=1/fs
f0=60
x=np.sin(2*np.pi*n*T*f0)

fig, ax = plt.subplots(num='Figura 8',clear=True)
ax.plot(n,x)
ax.set(xlabel='No. de muestras', ylabel='Amplitud',
       title='Gráfica de la señal sinusoidal Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%


alfa=0.05
M=20
y, e, w = lms(x, d, M, alfa)
fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 9', clear=True)
ax1.plot(n,d, color='green')
ax2.plot(n,x, color='purple')
ax3.plot(n[0:len(e)], e, color='orange')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal ECG - Valeria Chico y Jesus Espinoza')
ax2.set( ylabel= 'Amplitud',
       title= 'Señal de de ECG adicionada con Ruido')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) ')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
#%%
alfa002=0.02
alfa001=0.01
y002, e002, w002=lms(x, d, M, alfa002)
y001, e001, w001=lms(x, d, M, alfa001)


fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 10', clear=True)
ax1.plot(n[0:len(e)],e, color='orange')
ax2.plot(n[0:len(e002)],e002, color='black')
ax3.plot(n[0:len(e001)], e001, color='gray')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.05 - Valeria Chico y Jesus Espinoza')
ax2.set( ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.02')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.01')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
#%%
M=3
alfa=0.05

y, e, w = lms(x, d, M, alfa)
fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 11', clear=True)
ax1.plot(n,d, color='blue')
ax2.plot(n,x, color='red')
ax3.plot(n[0:len(e)], e, color='orange')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal ECG M=3 - Valeria Chico y Jesus Espinoza')
ax2.set( ylabel= 'Amplitud',
       title= 'Señal de de ECG adicionada con Ruido')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) M=3')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
#%%

alfa002=0.02
alfa001=0.01
y002, e002, w002=lms(x, d, M, alfa002)
y001, e001, w001=lms(x, d, M, alfa001)


fig,[ax1, ax2, ax3] = plt.subplots(3,1, num= 'Figura 12', clear=True)
ax1.plot(n[0:len(e)],e, color='orange')
ax2.plot(n[0:len(e002)],e002, color='purple')
ax3.plot(n[0:len(e001)], e001, color='blue')
ax1.set( ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.05 M=3 - Valeria Chico y Jesus Espinoza')
ax2.set( ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.02')
ax3.set(xlabel='Tiempo (s)', ylabel= 'Voltaje (mV)',
       title= 'Señal de error e(n) alfa=0.01')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()