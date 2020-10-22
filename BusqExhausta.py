#Ejercicio 1,2 Busqueda Exhaustiva
import matplotlib.pyplot as plt
from numpy import *

def funcion(x):
  return pow(x,2)-sin(x)

#Grafica
x=arange(0,1,0.01)
lista=[]
for cont in x:
      lista.append(funcion(cont))

plt.plot(x,funcion(x))

datos = " "
for x in lista:
    datos+=str(x)+" \n"
print(datos)
print("El punto de inflexion es un minimo, y su valor es: ",min(lista))
