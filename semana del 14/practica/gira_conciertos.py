
#Definición de la función

def planear_gira(c,r,entradas,indice=0):
    pd ={}# almacena el número de entradas
    if(indice>=len(entradas) or c==0): 
        return 0 

    else:

        indice2= indice+r-1
        maximo=max(planear_gira(c,r,entradas,indice+1),entradas[indice]+planear_gira(c-1,r,entradas,indice+r))
        
    return maximo




'''RESOLUCIÓN DEL EJERCICIO
Lo hemos hecho como una especie de problema de la mochila en que puede que elijamos tomar el concierto actual o no, de tomarlo, nuestro índice sobrbe
la lista se incrementaría r posiciones por el descanso, pero de no tomarlo solo se incrementaría en una unidad. Así pues, en el caso de que aún nos queden conciertos disponibles
o estemos denteo de la longitud  de la lista, podremos buscar el maximo de tomar o no tomar el concierto que indica el índice actual'''

def main():
    entradas=[8000,6000,9000,8000,9000]
    c=3
    r=3
    print(planear_gira(c,r,entradas))

main()






























