#Definición de la función

def viajar(costes, volumenes, s):

    #Caso base: no me queda volumen dentro de la bodega

    if(s==0 or len(costes)==0):
        return  # no puedo llenar más la mochila 
    

    if volumenes[0]>s:
        #Elemento volumen mayor que presupuesto
        return viajar(costes[1:], volumenes[1:], s)
    
    else:
        incluir= costes[0]+viajar(costes[1:], volumenes[1:], s-volumenes[0])
        no_incluir=viajar(costes[1:], volumenes[1:], s)
        return min(incluir, no_incluir)






# Método de resolución: como problema de la mochila pero sin tratar con estructuras de almacenaje dinámico de los datos

#División: divide el problema en instancias más pequeñas del mismo
#Resolución: resolvemos para el caso base cuando no cabe o no me quedan elementos
#Combinación: combinas los mínimos de todas las distintas soluciones que has obtenido


#Es como un enfoque del problemma de la mochila pero sin usar estructuras de almacenaje dinámico.
#Pesos: es el volumen de cada elemento
#Valores: es el precio de cada elemento
#Capacidad: total de volumen de la bodega
#Queremos minimizar el coste del llenado de la bodega al completo