#Este Programa genera la grafica para un numero N de pasos ingresados por el usuario
#y verifica la hipotesis teórica inciso d)
import numpy as np
import matplotlib.pylab as pl
import random 
from math import*


n=int(input("Digite el numero de pasos de la caminata: "))

x = np.zeros(n) 
y = np.zeros(n)
sx=np.zeros(n)
sy=np.zeros(n)

for i in range(1,n):#genera numeros normalizados
    x[i]=(np.random.rand()-0.5)* 2.    # −1 =< x =< 1
    y[i]=(np.random.rand()-0.5)* 2.    # −1 =< y =< 1
    L=sqrt(x[i]**2 + y[i]**2)
    x[i]=x[i]/L
    y[i]=y[i]/L
    
    sx[i]=x[i]+sx[i-1]
    sy[i]=y[i]+sy[i-1]

R2=sx[n-1]**2 + sy[n-1]**2

pl.plot(sx,sy,'k',linewidth=0.7);pl.plot(0,0,'ro')
pl.grid(True)
pl.title(f'Caminata con {n} pasos')
pl.xlabel("x")
pl.ylabel("y")
pl.show()

def hipotesis(x,y):
    htl=[]
    for i in range(n):
        for j in range(n):
            if i==j or i>j:
                pass
            else:
                ht=(x[i]*x[j])
                htl.append(ht)
            
    suma=0
    for i in range(len(htl)):
        suma=suma+htl[i]

    hipteo=suma/(len(htl)*R2)
    print(f"\nLa hipoteis teórica es: {hipteo}")
hipotesis(x,y)