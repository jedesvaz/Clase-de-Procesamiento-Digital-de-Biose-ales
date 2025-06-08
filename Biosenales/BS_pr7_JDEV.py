# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:30:09 2021

@author: EV
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, find_peaks
PATH= 'C:\\Users\\eltal\\Documents\\Tareas\\Tareas de PDBioseñales\\python\\' 	# ruta donde se encuentra 
# el archivo en la PC (especificar)

DATAFILE= 'ecg3.c8k'        	# nombre del archivo (especificar)
TIME2READ=40               	# cantidad de tiempo a leer en segundos (especificar)

fs=1000                 	# frecuencia de muestreo 
Ts=1/fs				# periodo de muestreo
SAMPLES2READ=TIME2READ*fs 	# numero de muestras a leer del archivo
                         
file2read= PATH+DATAFILE       	# Nombre completo del archivo (incluye su ruta)
fid = open(file2read,'rb')	      # abre el archivo binario para leerlo

# La siguiente instrucción lee el archivo de datos (datos de 16 Bits) 
# según la cantidad de muestras establecidas en SAMPLES2READ,
# multiplicada por 12, por ser 12 derivaciones. 
# Genera la variable datos donde se encuentran todas las derivaciones en secuencia.

datos = np.fromfile(fid, np.int16, count= SAMPLES2READ *12) 

# Posteriormente se reordenan los datos para obtener
# 12 columnas, donde cada columna es una derivación del ECG

signals = datos.reshape((SAMPLES2READ,12))

# la variable signals tendrá los valores decimales que genera el ADC
# estos valores deberán ser convertidos a voltios empleando la ec.1
LSB=5/(2**12)
signals=((signals*LSB)-2.5)/500
DI=signals[:,0]
DII=signals[:,1]
DIII=signals[:,2]
N=len(DI)
n=np.arange(N)
tiempo=n*Ts


fig, (ax1,ax2,ax3) = plt.subplots(3,1, num='Figura 1',clear=True)
ax1.plot(tiempo,DI, color="green")
ax1.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DI -  Valeria Chico y Jesus Espinoza')

ax1.grid()
ax1.legend()


ax2.plot(tiempo,DII, color="orange")
ax2.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DII')

ax2.grid()
ax2.legend()


ax3.plot(tiempo,DIII,color="purple")
ax3.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DIII')

ax3.grid()
ax3.legend()
#plt1.show()
#%% Filtrado
fl=2
fh=30
fln=2/(fs/2)
fhn=30/(fs/2)
M=3
b,a=butter(M, [fln, fhn], btype='bandpass')

signals_f=lfilter(b,a, signals,axis=0)
DI_f=signals_f[:,0]
DII_f=signals_f[:,1]
DIII_f=signals_f[:,2]


fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.plot(tiempo,DI_f)
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal SqW -  JDEV')

ax.grid()
ax.legend()
plt.show()
#%%
fig, (ax1,ax2,ax3) = plt.subplots(3,1, num='Figura 3',clear=True)
ax1.plot(tiempo,DI_f, color="green")
ax1.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DI filtrada -  JDEV')

ax1.grid()
ax1.legend()


ax2.plot(tiempo,DII_f, color="orange")
ax2.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DII filtrada')

ax2.grid()
ax2.legend()


ax3.plot(tiempo,DIII_f,color="purple")
ax3.set(xlabel='tiempo (s)', ylabel='Amplitud (V)',
       title='Gráfica de señal DIII filtrada')

ax3.grid()
ax3.legend()
#%% Detector de QRS
peaks, _ = find_peaks(DI_f, height=0.0004, distance=1)

fig, ax = plt.subplots(num='Figura 4',clear=True)
ax.plot(tiempo,DI_f)
ax.plot(tiempo[peaks],DI_f[peaks],'*')
ax.set(xlabel='tiempo (s)', ylabel='Amplitud',
       title='Gráfica de señal  -  JDEV')

ax.grid()
ax.legend()
plt.show()
#%% Algoritmo de frecuencia cardíaca


asq=np.diff(DI_f)
FCP=1/asq*60