# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:27:37 2021

@author: EV
"""
#%% 1) Diseño de filtro
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal #importar solo un modulo de una biblioteca 
import math

fs = 1000		# frecuencia de muestreo (especificar)
fc =30	# frecuencia de corte baja en Hz (especificar)
fc_n = fc/(fs/2) 	# frecuencia de corte normalizada respecto a fs/2

M = 2			# orden del filtro (especificar)

b, a = signal.butter(M, fc_n, 'low')
mi=1/math.sqrt(2)
#%% 2) ubicación de los polos y los ceros en el plano Z del filtro 1)
from plot_zplane import zplane 
theta = 2*np.pi*(fc/fs)
a0=1
a1=2*mi*np.cos(theta)
a2=mi**2
b0=1
b1=2
b2=1
b = np.array([b0, b1, b2])
a = np.array([a0, -a1, a2])
zplane(b, a)
#%% 3) Aplicacion filtro en ECG
import scipy.io as sio 
datos= sio.loadmat("ECG60")
senal = datos["ECG60"]

data=np.loadtxt('ecg-pulso.txt')
pulso = data[:,0]
#ecg=data[:,1]

fs = 1000          # frecuencia de muestreo (especificar)
Ts = 1/fs          # periodo de muestreo
N = len(pulso)     # numero de muestras de la señal de pulso
n = np.arange(0,N)    # secuencia de numeros de muestras
tiempo = n*Ts 


fig, ax = plt.subplots(num='Figura a2',clear=True)
ax.plot(tiempo,senal, label="Señal ECG")
ax.set(xlabel='tiempo (s)', ylabel='mV',
       title='Gráfica de pulso Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%%3 b)
from scipy import signal
senal_f = signal.lfilter(b, a, senal, axis=0)

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.plot(tiempo,senal_f, label="Señal ECG filtrada")
ax.set(xlabel='tiempo (s)', ylabel='mV',
       title='Gráfica de pulso Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% 4) Filtro 5o orden
fsx = 1000		# frecuencia de muestreo (especificar)
fcx =30	# frecuencia de corte baja en Hz (especificar)
fc_nx = fcx/(fsx/2) 
bx, ax = signal.butter(5, fc_nx, 'low')
zplane(bx,ax)

senal_fx = signal.lfilter(bx, ax, senal, axis=0)

fig, ax = plt.subplots(num='Figura 2b',clear=True)
ax.plot(tiempo,senal_fx, label="Señal ECG filtrada 5 orden")
ax.set(xlabel='tiempo (s)', ylabel='mV',
       title='Gráfica de pulso Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
#%% Extra subplots señales original, 2o y 5o orden
fig, (ax1,ax2,ax3)=plt.subplots(3,1, num='Figura con señales', clear=True)
fig.suptitle('Gráfica de las señales de ECG- Jesus Espinoza')

ax1.plot(tiempo,senal, color='green')
ax1.set_ylabel('amplitud en mV')
ax1.set_xlabel('tiempo en s')
ax1.set_title('Señal de ECG original')
ax1.grid()

ax2.plot(tiempo,senal_f, color='orange')
ax2.set_ylabel('amplitud en mV')
#ax2.set_xlabel('tiempo en s')
ax2.set_title('Señal de ECG filtrada 2o orden')
ax2.grid()

ax3.plot(tiempo,senal_fx, color='purple')
ax3.set_ylabel('amplitud en mV')
ax3.set_xlabel('tiempo en s')
ax3.set_title('Señal de ECG filtrada 5o orden')
ax3.grid()
 
