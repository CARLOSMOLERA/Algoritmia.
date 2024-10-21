#Definición de la función
import numpy as np 

def mazmorra(mat):


    #Alcanzar a la princesa
    if(mat.shape==(1,1)):#solo me queda el elemento target en el mapa 
        return mat[0][0]
        

    #Salirme del mapa
    if(0 in mat.shape):# significa que me he salido del mapa en algún punto
        return float("-inf") #para que no se pueda considerar dicha solución


    #Creo un valor muy negativo: solo se actualizará si derecha o abajo son negativos
    maximo = float('-inf')
 
    # Necesito obtener el número negativo más pequeño posible y sumarle uno al final para decir los positivos que me hacen falta*
    derecha =mat[0][0]+mazmorra(mat[:,1:])#con esto vamos a ir actualizando mi vida restante 
    abajo = mat[0][0]+mazmorra(mat[1:,:])


    #Guardamos una referencia que solo se actualizará si los valores de der o abajo son negativos
    #Guardará los que más cercanos a cero se presenten
    if derecha<0:# solo quiero cosas negativas
        maximo = max(maximo, derecha)
    if abajo<0:
         maximo = max(maximo, abajo)

    #Tenemos que comprobar si va siendo negativo
    return maximo #quiero que la función trabaje con este valor, no con el minimo o el maximo de todo el camino 


# Ejemplo: la vida final del caballero es de -5--> le harán falta seis puntos de vida 


def main():
    mat = np.array([[-2,-3,3],
                   [-5,-10,1],
                   [10,30,-5]])
    target = (2,2)
    source = (0,0)
    print(-mazmorra(mat)+1)# solo quiere que me mueva en la diagonal, se podría generalizar poniendo sources y targets

    #El movimiento es el usual--> derecha y abajo incrementa filas y columnas
main()



#Objetivo:'
'''

1.Logica: tenemos que obtener el mínimo valor negativo y la vida necesaria será ese
valor negativo en valor absoluto mas uno

2.Desarrollo: vamos desarrollando y llamanod recursivamente a derecha y abajo. A excepci
on de los casos base que devolverán sus cosas determinadas, de las llamadas a izquierda o derecha
nos vamos a quedar solo con la más cercana a cero de ambas porque es la que nos interersa

3. Maximo: surgen ante la necesidad de comparar primero si el camino es menor que cero y de ser así, elegir la variante mas 
cercana a cero de las dos que se presenten, es simplemente eso

De otra manera si hacemos el max de las ramas puede ser positivo y el min -inf, 
por eso se necesita de una variable intermedia o una comparación de cuál de los dos 
es más cercana a cero '''