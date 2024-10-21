#Definición de la función

import numpy as np 

def plantar(mapa:np.ndarray, pose:tuple, target:tuple):
    

    if(pose==target):
        return 1 #para que no contribuya a ensanchar el camino
    
    #Mirar si me he salido del mapa
    condicion = pose[0]>(mapa.shape[0]-1) or pose[1]<0 #shape te cuenta un número por encima del índice de acceso, lo cual es lógico
    if(condicion):
        return float("inf")
    

    #Cuando llegue a un camino prohibido
    if(mapa[pose[0]][pose[1]]==1 ):# estoy en un sitio prohibido
        return float("inf")# para decirle que se está equivocando y ese camino ya no lo toque 
    

    else:# Caso de dar los diferentes pasos
        #Sumo los pasos actuales a lo que tengo: les sumo uno por paso
        norte = 1+ plantar(mapa,(pose[0]+1,pose[1]),target)
        oeste  = 1+plantar(mapa,(pose[0],pose[1]-1),target)
        suroeste =1+ plantar(mapa,(pose[0]+1,pose[1]-1),target)
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
    target = (2,1)
    start = (1,3)
    print("Se recorrerá en un mínimo de:",plantar(mat, start, target))
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













