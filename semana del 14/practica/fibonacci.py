import numpy as np 
import math
import time


memo=[]
#Programación dinámica

#Memoización: busca en la memoria y si no está la rellena
def fibonacci(n):
    if n<=1:
        return n
    try:
        return memo[n]
    except IndexError:
        memo.append(fibonacci(n-1)+ fibonacci(n-2))
        return memo[-1]#devuelve el elemento que se ha creado
    
# Si no es el caso base, busca en la memoria y si no está, lo guarda con llamada recursiva y devuelve esa memoria




#Tabulación: rellena toda la tabla y devuelve el valor de la tabla que necesitamos

tabla = []
def fibonacci2(n):

    if n<=1:
        return n
    #Rellenamos la tabla
    tabla.append(0)
    tabla.append(1)
    for i in range(2,n+1):
         tabla.append(tabla[i-1]+tabla[i-2])# vas rellenando toda la tabla de los casos

    return tabla[n]
#Si no es el caso base, rellena toda una tabla basándose en los caso de cero y uno y después devuelve el valor buscado






print(fibonacci(3))
print(time.time(),fibonacci2(3),time.time())




