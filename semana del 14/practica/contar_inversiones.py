#Contar inversiones aprovechando mergesort



def counter(array):
    if len(array)==1:
        return 0,array # no me quedan más inversiones
    media = len(array)//2
    # Hacer el árbol para más claridad: si llama 1234 me cueta las de 1 2 3 4, despues las de 12 con 34 sumadas a las de antes y me devuelve eso junto con el array ordenado
    c1,izq=counter(array[:media])
    c2,der=counter(array[media:])  
    inversiones, ordenado = contar_inversiones(izq,der)
    return c1+c2+inversiones, ordenado



#Función para contar el número de inversione

def contar_inversiones(izq, der):#también me ordena las listas
    i=0
    j=0
    inversiones=0
    resultado=[]
    while (i<len(izq)and j<len(der)):
        if izq[i]<der[j]:
            resultado.append(izq[i])
            i+=1


        else:
            
            resultado.append(der[j])
            j+=1
            inversiones+=len(izq[i::])#le añado lo restante en la izquierda que es menor que el que estoy tomando de la derecha 

    # Solo va a haber una lista que llegue hasta el final en tanto que contenga elementos menores, mientras que la otra puede que no llegue al ser mayores y los añada directamente 
    try:# prueba la posibilidad de ocurrencia del posible caso situado de manera inferior
        resultado.append(*der[j:])
    except TypeError:#se ejecuta en el caso de que ocurra algun tipo de excepcion
        resultado.append(*izq[i:])
    finally:# siempre se va a ejecutar
        return inversiones,resultado



# Es muy importante el tener en cuenta que las listas ya vienen ordenadas
            


# Cada vez que un elemento de una parte derecha ya ordenada se añade a la lista final, el número de inversiones que presentará será igual al número de elementos que queden en la lista izquierda, que ya de por sí se encuentra ordenada 


def main():
    array=[4,3,7,0]
    res, array= counter(array)
    print("El número de inversiones asociado es:", res, " y el array ordenado es:", array)



main()