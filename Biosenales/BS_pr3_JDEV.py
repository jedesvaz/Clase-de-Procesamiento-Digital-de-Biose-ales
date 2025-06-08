# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:08:26 2021

@author: EV
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal #importar solo un modulo de una biblioteca 

data=np.loadtxt('ecg-pulso.txt')
pulso = data[:,0]
ecg=data[:,1]

fs = 500           # frecuencia de muestreo (especificar)
Ts = 1/fs          # periodo de muestreo
N = len(pulso)     # numero de muestras de la señal de pulso
n = np.arange(0,N)    # secuencia de numeros de muestras
tiempo = n*Ts      
fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.plot(tiempo,pulso, label="Señal pulso")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='tiempo (s)', ylabel='ohms',
       title='Gráfica de pulso Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%
fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.plot(tiempo,ecg, label="Señal ECG")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='tiempo (s)', ylabel='mV',
       title='Gráfica de pulso Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% Filtro 60
fs=500
fc=60
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')
#%% Filtro 30
fs=500
fc=30
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')
#%% ECG 60
fs=500
fc=60
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')

ecg_f=signal.lfilter(b,a,ecg)

fig, (ax1,ax2)=plt.subplots(2,1, num='Figura con subplots', clear=True)
fig.suptitle('Gráfica de las señales de ECG- Jesus Espinoza')

ax1.plot(tiempo,ecg, color='green')
ax1.set_ylabel('amplitud en mV')
ax1.set_xlabel('tiempo en s')
ax1.set_title('Señal de ECG original')
ax1.grid()

ax2.plot(tiempo,ecg_f, color='red')
ax2.set_ylabel('amplitud en mV')
#ax2.set_xlabel('tiempo en s')
ax2.set_title('Señal de ECG filtrada')
ax2.grid()

#%% Pulso 60
fs=500
fc=60
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')

pulso_f=signal.lfilter(b,a,pulso)

fig, (ax1,ax2)=plt.subplots(2,1, num='Figura con subplots', clear=True)
fig.suptitle('Gráfica de las señales de pulso- Jesus Espinoza')

ax1.plot(tiempo,pulso, color='green')
ax1.set_ylabel('amplitud en mV')
ax1.set_xlabel('tiempo en s')
ax1.set_title('Señal de ECG original')
ax1.grid()

ax2.plot(tiempo,pulso_f, color='orange')
ax2.set_ylabel('amplitud en mV')
#ax2.set_xlabel('tiempo en s')
ax2.set_title('Señal de ECG filtrada')
ax2.grid()

#%%Práctica 3 ECG
fs=500
fc=60
fc30=30
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')

ecg_f=signal.lfilter(b,a,ecg)


fc_n30=fc30/(fs/2) #frecuencia de corte normalizada
M=3
b,aa=signal.butter(M,fc_n30, 'low')
ecg_f30=signal.lfilter(b,aa,ecg)

fig, (ax1,ax2,ax3)=plt.subplots(3,1, num='Figura con subplots', clear=True)
fig.suptitle('Gráfica de las señales de ECG- Valeria Chico y Jesus Espinoza')

ax1.plot(tiempo,ecg, color='green')
ax1.set_ylabel('amplitud en mV')
#ax1.set_xlabel('tiempo en s')
ax1.set_title('Señal de ECG original')
ax1.grid()

ax2.plot(tiempo,ecg_f, color='red')
ax2.set_ylabel('amplitud en mV')
#ax2.set_xlabel('tiempo en s')
ax2.set_title('Señal de ECG filtrada 60Hz')
ax2.grid()

ax3.plot(tiempo,ecg_f30, color='purple')
ax3.set_ylabel('amplitud en mV')
ax3.set_xlabel('tiempo en s')
ax3.set_title('Señal de ECG filtrada 30 Hz')
ax3.grid()

#%% Practica 3 Pulso
fs=500
fc=60
fc30=30
fc_n=fc/(fs/2) #frecuencia de corte normalizada
M=3
b,a=signal.butter(M,fc_n, 'low')

pulso_f=signal.lfilter(b,a,pulso)


fc_n30=fc30/(fs/2) #frecuencia de corte normalizada
M=3
b,aa=signal.butter(M,fc_n30, 'low')
pulso_f30=signal.lfilter(b,aa,pulso)

fig, (ax1,ax2,ax3)=plt.subplots(3,1, num='Figura con subplots', clear=True)
fig.suptitle('Gráfica de las señales de pulso- Valeria Chico y Jesus Espinoza')

ax1.plot(tiempo,pulso, color='green')
ax1.set_ylabel('amplitud en Ohms')
#ax1.set_xlabel('tiempo en s')
ax1.set_title('Señal de pulso original')
ax1.grid()

ax2.plot(tiempo,pulso_f, color='red')
ax2.set_ylabel('amplitud en Ohms')
#ax2.set_xlabel('tiempo en s')
ax2.set_title('Señal de pulso filtrada 60Hz')
ax2.grid()

ax3.plot(tiempo,pulso_f30, color='purple')
ax3.set_ylabel('amplitud en Ohms')
ax3.set_xlabel('tiempo en s')
ax3.set_title('Señal de pulso filtrada 30 Hz')
ax3.grid()