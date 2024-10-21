import numpy as np
import math
import time
import sys
sys.setrecursionlimit(1500)

#Estudio de la versión discreta: valores y pesos enteros
#Indexamos en la tpd los distintos estados de la mochila

#PD[i][W]: valor máximo que se puede obtener con los i primeros pesos
#de una mochila de capacidad restante w

#Versión memoizada de como construir tabla PD
pd = {}

def mochila(n, w, pesos, valores):
    global pd#es un diccionario de los elementos y sus pesos
    if n == 0 or w == 0:
        return 0

    if (n,w)in pd:  # Si ya está calculado: cuando se bifurca en el max
        return pd[(n,w)]


# Si el peso del elemento es mayor que la capacidad restante, ignoramos este elemento
    if pesos[n-1] > w:
        pd[(n,w)] = mochila(n-1, w, pesos, valores)
    else:
        # Calculamos el máximo entre no incluirlo o incluirlo
        pd[(n,w)]=max(
            mochila(n-1, w, pesos, valores),
            valores[n-1] + mochila(n-1, w - pesos[n-1], pesos, valores)
            )

    return pd[(n,w)]#cuando deshago las llamadas recursivas llamo a esto



# Ejemplo 1
n1 = 4
w1 = 5
pesos1 = [1, 2, 3, 4]
valores1 = [10, 20, 30, 40]
print(mochila(n1,w1,pesos1, valores1))
# Ejemplo 2
n2 = 3
w2 = 50
pesos2 = [10, 20, 30]
valores2 = [60, 100, 120]
print(mochila(n2,w2,pesos2, valores2))

# Ejemplo 3
n3 = 5
w3 = 10
pesos3 = [2, 3, 4, 5, 9]
valores3 = [3, 4, 5, 8, 10]
print(mochila(n3,w3,pesos3, valores3))
# Ejemplo 4
n4 = 6
w4 = 15
pesos4 = [1, 3, 4, 5, 6, 7]
valores4 = [1, 4, 5, 7, 8, 9]
print(mochila(n4,w4,pesos4, valores4))



# En la mochila empiezas desde el final hasta que llegas a lo que viene siendo el 
# caso base 