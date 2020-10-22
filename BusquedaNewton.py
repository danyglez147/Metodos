#Ejercicio 4 Busqueda de newton
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def funcion(x):
    return pow(x,2)-np.sin(x)
def derivada1(x):
    return 2*x -np.cos(x)
def derivada2(x):
    return 2 + np.sin(x)

xy= 0.1
xi= 0.5
def MetodoNewton(funcion,derivada1,derivada2,xi,xy):
    xn=xi
    n=0
    while abs(derivada1(xn))>=xy:
        xn=xn-derivada1(xn)/derivada2(xn)
        n+=1
        print('Newton valor minimo:  \n y= ',funcion(xn))
        if n==11:
          break
    return xn

#Grafica
x=arange(0,1,0.01)
plt.plot(x,funcion(x))
x=MetodoNewton(funcion,derivada1,derivada2,xi,xy)
plt.plot(x,funcion(x),marker=".", color="blue")

