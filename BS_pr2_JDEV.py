# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:06:31 2021

@author: EV
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%% ECG 1
data=pd.read_excel('ECG 1.xlsx', header=None, skiprows=8) #contienen 3 columnas, la tercera con nan (not a number)
tiempo=data[0]
tiempo=np.array(tiempo) #conversión de tiempo a un arreglo de numpy

ecg=data[1]
ecg=np.array(ecg) #conversión de ecg a un arreglo de numpy

fig, ax = plt.subplots(num='Figura 1',clear=True)

ax.plot(tiempo,ecg, label="Señal de ECG 1")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='tiempo (s)', ylabel='voltaje (mV)',
       title='Gráfica de ECG -Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()

#%% ECG 2
data=pd.read_excel('ECG 2.xlsx', header=None, skiprows=8) #contienen 3 columnas, la tercera con nan (not a number)
tiempo=data[0]
tiempo=np.array(tiempo) #conversión de tiempo a un arreglo de numpy

ecg=data[1]
ecg=np.array(ecg) #conversión de ecg a un arreglo de numpy

fig, ax = plt.subplots(num='Figura 2',clear=True)

ax.plot(tiempo,ecg, label="Señal de ECG 2")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='tiempo (s)', ylabel='voltaje (mV)',
       title='Gráfica de ECG -Valeria Chico y Jesus Espinoza')

ax.grid()
ax.legend()
plt.show()
