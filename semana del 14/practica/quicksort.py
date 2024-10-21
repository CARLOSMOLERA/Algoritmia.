#Creación de quicksort:ordenacion por division hasta len==1

def quicksort(array):
    if len(array)==1:
        return array# Resolución del problema más simple
    
    else:
        pivote = mediana(array)
        izq , der=particion(array, pivote)#División en problemas más pequeños

    return(quicksort(izq)+[pivote]+quicksort(der))#Combinación de los resutlados




def mediana(array):
    if(len(array)%2==0):
        return array[len(array)//2]
    return array[(len(array)//2)+1]


def particion(array, pivote):
    izq,der=[],[]
    for element in array:
        if element<=pivote:
            izq.append(element)

        else:
            der.append(element)
    return izq, der




#Divide: elige un pivote y coloca a su izquierda los numeros menores= y a la derecha los mayores; el pivote quedará ordenado de cara al vector
# final y el resto de elementos a izquierda y derecha se ordenarán de manera recursiva


#Resolver: una vez llegamos al caso límite en que el vector ya está directamente ordenado, la resolución es directa

#Combinación: el vector se va  a ordenar recursivamente a ambos lados del pivote que va a ocupar la posición que le corresponde
