import matplotlib.pyplot as pl
from pylab import *
import numpy as np
from math import*

n=int(input("Digite el numero de N pasos: "))
k=int(sqrt(n))

todo=[]

# incisos a), b), c)
def grande(n,todo):
    Rms=[]
    
    #inciso a)
    def camaleat():
        sumx=0.0
        sumy=0.0
    
        x = np.zeros(n) 
        y = np.zeros(n)
        for i in range(1,n):#genera numeros normalizados
            x[i]=(np.random.rand()-0.5)* 2.    # −1 =< x =< 1
            y[i]=(np.random.rand()-0.5)* 2.    # −1 =< y =< 1
            L=sqrt(x[i]**2 + y[i]**2)
            x[i]=x[i]/L
            y[i]=y[i]/L
        
        for i in range(1,n):
            sumx+=x[i]
            sumy+=y[i]
    
        Rms.append(sumx**2+sumy**2)
    camaleat()


    #inciso b)
    def kexperimentos():
        for i in range(1,k):
            np.random.seed(None)
            camaleat()
    kexperimentos()

    #inciso c) obtener el valor esperado para k caminatas
    def vespR(Rms,n):
        Total=0.0
        for i in range(k):
            Total+=Rms[i]
    
        Total=Total/k
        todo.append(Total)
        print(f'EL valor de <R^2({n})> es: {Total}')
    vespR(Rms,n)
for i in range(n+1):
    grande(i,todo)


#inciso e)
def grafica(todo):
    N=[]
    for i in range(n+1):
        N.append(sqrt(i))
        todo[i]=sqrt(todo[i])
    
    lin=[0,N[n-1]]
    pl.title(f"Rrms en funcion de raiz de N")
    pl.plot(N,todo,'b',linewidth=0.8)
    pl.plot(N,N,'g')
    pl.xlabel("sqrt(N)")
    pl.ylabel("Rrms")
    pl.show()
grafica(todo)