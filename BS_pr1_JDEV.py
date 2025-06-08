# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:13:31 2021

@author: EV
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
inicio=int(input("Ingrese el número de muestra de inicio: "))
fin=int(input("Ingrese el número de muestra de fin: "))
#inicio y fin son cadenas de caracteres hasta este momento
#Act: Con la funcion int(), se convierten las cadenas de caracteres de input a enteros
n0=int(input("Ingrese el desplazamiento del impulso: ")) #paso 3
n=np.arange(inicio, fin+1) #paso 4
x=np.zeros(len(n)) #paso 5
x[n==n0]=1

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.stem(n, x)
#ax.plot(t,s, label="n")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='n - numero de muestras', ylabel='x- amplitud',
       title='Gráfica de impulso desplazado Jesús Daniel Espinoza Vázquez')

ax.grid()
ax.legend()
plt.show()

#%%
n0=5
n=np.arange(1,21)
x=np.zeros(len(n))
x[n==n0]=1*0.9

fig, ax = plt.subplots(num='Figura 2',clear=True)
ax.stem(n, x)
#ax.plot(t,s, label="n")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='n - numero de muestras', ylabel='x- amplitud',
       title='Gráfica de impulso desplazado Jesús Daniel Espinoza Vázquez')

ax.grid()
ax.legend()
plt.show()

#%%Señal Escalón
inicio=int(input("Ingrese el número de muestra de inicio: "))
fin=int(input("Ingrese el número de muestra de fin: "))
n0=int(input("S.Ingrese el desplazamiento del escalón: ")) #paso 3
n=np.arange(inicio, fin+1) #paso 4
x=np.zeros(len(n)) #paso 5
x[n>=n0]=1 #Fíjate en esta!!!!!!!!!!!

fig, ax = plt.subplots(num='Figura 1',clear=True)
ax.stem(n, x)
#ax.plot(t,s, label="n")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='n - numero de muestras', ylabel='x- amplitud',
       title='Gráfica de escalón desplazado Valeria Chico, Jesús Espinoza')

ax.grid()
ax.legend()
plt.show()



#%% Impulso X4


inicio=-10
fin=0
#inicio y fin son cadenas de caracteres hasta este momento
#Act: Con la funcion int(), se convierten las cadenas de caracteres de input a enteros
n0=-7
n=np.arange(inicio, fin+1) #paso 4
x=np.zeros(len(n)) #paso 5
x[n==n0]=1 #Fíjate en esta!!!!!!!!!!!

fig, ax = plt.subplots(num='Figura 5',clear=True)
ax.stem(n, 4.5*x)
#ax.plot(t,s, label="n")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='n - numero de muestras', ylabel='x- amplitud',
       title='Gráfica de impulso 4.5d(n+7) Valeria Chico Jesús Espinoza')

ax.grid()

plt.show()


#%% Impulso X5
inicio=-5
fin=5
#inicio y fin son cadenas de caracteres hasta este momento
#Act: Con la funcion int(), se convierten las cadenas de caracteres de input a enteros
n01=-2
n02=4

n=np.arange(inicio, fin+1) #paso 4
x1=np.zeros(len(n)) #paso 5
x2=np.zeros(len(n))
x1[n==n01]=1*2#Fíjate en esta!!!!!!!!!!!
x2[n==n02]=-1
xf=x1+x2
fig, ax = plt.subplots(num='Figura 6',clear=True)
ax.stem(n, xf)
#ax.plot(t,s, label="n")
#ax.plot(t,c, label="amplitud")
ax.set(xlabel='n - numero de muestras', ylabel='x- amplitud',
       title='Gráfica de impulso 2d(n+2)-d(n-4) Valeria Chico, Jesús Espinoza')

ax.grid()

plt.show()

#%% Señal Exponencial

inicio = 0
fin = 10

n = np.arange(inicio, fin+1)
x = 0.9**n

fig, ax = plt.subplots(num= 'Figura 1', clear=True)

ax.stem(n, x)
ax.set(xlabel= 'n - numero de muestras' , ylabel= 'x - amplitud',
       title= 'Grafica de secuencia exponencial  - Valeria Chico, Jesús Espinoza')
plt.show()
ax.grid()

#%% Sinusoides
inicio = 0
fin = 25
#1 
n = np.arange(inicio, fin+1)
x = np.sin(np.pi*n/17)

fig, ax = plt.subplots(num= 'Figura 1', clear=True)

ax.stem(n, x)
ax.set(xlabel= 'n - numero de muestras' , ylabel= 'x - amplitud',
       title= 'Grafica de sinusoides - Valeria Chico, Jesús Espinoza ')
plt.show()
ax.grid()
#%%Sinusoides 2
inicio = -15
fin = 25

n = np.arange(inicio, fin+1)
x = np.sin(np.pi*n/10)

fig, ax = plt.subplots(num= 'Figura 1', clear=True)

ax.stem(n, x)
ax.set(xlabel= 'n - numero de muestras' , ylabel= 'x - amplitud',
       title= 'Grafica de sinusoides - Valeria Chico, Jesús Espinoza ')
plt.show()
ax.grid()

#%%Sinusoides 3
inicio = -10
fin = 10

n = np.arange(inicio, fin+1, 0.01)
x = 5*np.sin(np.pi*n*3+np.pi/2)

fig, ax = plt.subplots(num= 'Figura 11', clear=True)

ax.stem(n, x)
ax.set(xlabel= 'n - numero de muestras' , ylabel= 'x - amplitud',
       title= 'Grafica de sinusoides - Valeria Chico, Jesús Espinoza ')
plt.show()
ax.grid()
#%% Sinusoides 4 
inicio = 0
fin = 50

n = np.arange(inicio, fin+1, 0.01)
x = np.cos(np.pi*n/(np.sqrt(23)))

fig, ax = plt.subplots(num= 'Figura 12', clear=True)

ax.stem(n, x)
ax.set(xlabel= 'n - numero de muestras' , ylabel= 'x - amplitud',
       title= 'Grafica de sinusoides - Valeria Chico, Jesús Espinoza ')
plt.show()
ax.grid()

#%% ECG
import scipy.io as sio
datos=sio.loadmat("ECG1")
senal=datos['ecg'] #ecg es una clave dentro del diccionario
tiempo=senal[:,0]
ecg=senal[:,1]

fig, ax = plt.subplots(num= 'Figura 1', clear=True)

ax.plot(tiempo, ecg)
ax.set(xlabel= 'Tiempo (s)' , ylabel= 'x - amplitud (mV)',
       title= 'ECG - JDEV ')
#plt.show()
ax.grid()



