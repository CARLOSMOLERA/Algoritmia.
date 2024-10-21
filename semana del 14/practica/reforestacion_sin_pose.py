#Definición de la función

import numpy as np 

def plantar(mapa:np.ndarray):
    

    if(mapa.shape==(1,1)):#si solo queda un elemento en la matriz estoy en el target
        return 1 if mapa[0][0]==0 else float('inf') #para que no contribuya a ensanchar el camino
    
    #Mirar si me he salido del mapa
    if mapa.shape[0]==0 or mapa.shape[1]==0: #significaría que me he pasado quitando filas o columnas 
        return float("inf")
    

    #Cuando llegue a un camino prohibido: sé que la celda en la que estoy es el indice máximo de la matriz en ambas dimensiones porque le voy quitando trozos
    if(mapa[-1,-1]==1):# estoy en un sitio prohibido
        return float("inf")# para decirle que se está equivocando y ese camino ya no lo toque 
    

    else:# Caso de dar los diferentes pasos
        #Sumo los pasos actuales a lo que tengo: les sumo uno por paso
        norte = 1+ plantar(mapa[1:,:],)
        oeste  = 1+plantar(mapa[:,1:])
        suroeste =1+ plantar(mapa[1:,1:])

        # Las llamadas son secuenciales pero me construyen el árbol de abajo hacia arriba igualmente
        return min(norte, oeste, suroeste)
        



# Para mi lo positivo es desplazarme en sentido izquierdo, por tanto hay que considerarlo en el source y target

def main():
    mat = [
        [0,0,0,0],
        [0,1,1,0],
        [0,1,0,0]
        ]
    mat = np.array(mat)
    
    print("Se recorrerá en un mínimo de:",plantar(mat))
    # De derecha a izquierda se van restando las posiciones porque tomamos el eje en la esquina superior derecha


main()





#IMPLEMENTACIÓN DEL PROBLEMA DE LA MOCHILA CON ENFOQUE RECURSIVO SIN MEMORIA DINÁMICA 

#Modalidad sin uso de la memoria dinámica
#Divide: dividimos el problema en el hecho de dar diferentes pasos, teniendo como opciones los distintos caminos a seguir 
#Resolución:cuando nos encontramos al final del camino o al principio la resolución es trivial.*
#Combinación: combinamos los posibles resultados tomando el mínimo de las posibles soluciones y vamos construyendo el camino
#
#* Si nos topamos con un 1 o nos salimos del mapa se devuelve inf para que ese camino nunca pueda ser consideradp
#


#OBJETIVO: ES LLEGAR A LA ESQUINA INFERIOR IZQUIERDA DE LA ZONA DE OPERACION

'''

Claves
1. Conocer posicion: se en que posición estoy en tanto que al eliminar filas o columnas cada vez que me muevo siempre voy a estar en el extremo superior
de la matriz

2. Limites: cuando hay un cero en shape significa que me he pasado bien eliminando filas o bien eliminando las columna

3.Slices en array: [slicefila, slicecolumna]-->si no lo haces así está mal '''








