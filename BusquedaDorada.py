#Ejercicio 3 Busqueda Dorada
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def funcion(x):
    return pow(x,2)-sin(x)

def BusquedaDorada():
    a=0
    b=1
    tau=2-1.618033988 #Constante en algoritmo de GoldenSearch
    epsilon=1e-6  #constante epsilon
    cont=0
    lista=[]
    
    while(True):
        alpha1=a*(1-tau)+b*tau
        alpha2=a*tau+b*(1-tau)
        funcion_alpha1=funcion(alpha1)
        funcion_alpha2=funcion(alpha2)
        
        if(funcion_alpha1>funcion_alpha2):
           a=alpha1
        else:
            b=alpha2       
            
        cont=cont+1
        lista.append([funcion_alpha1])
        print(funcion_alpha1)

        if(np.abs(funcion_alpha1-funcion_alpha2)<epsilon):
            print("Minimo usando Razon Dorada")
            print(funcion_alpha1)
            break
BusquedaDorada()

#Grafica
x=arange(0,1,0.01)
plt.plot(x,funcion(x))
