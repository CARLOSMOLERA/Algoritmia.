def merge(array):
    if len(array)==1:
        return array
    

    media=len(array)//2 
    izq=merge(array[:media])
    der=merge(array[media:])
    return(sort(izq,der))
    


def sort(izq, der):
    i=0
    j=0
    resultado = []
    while(i<len(izq)or j<len(der)):
        if(izq[i]<der[j]):
            i+=1 # el puntero siempre se queda en el menor
            resultado.append(izq[i])
        else:
            resultado.append(der[j])
            j+=1
    resultado.append(izq[i:])
    resultado.append(der[j:])
    return resultado



#Divide: dividimos el problema de manera recursiva en dos mitades iguales
#Resuelve: dicha división se da hasta que se llega al caso base en que el vector está directamente ordenado
#Combinación: se combinan las dos mitades en una sola lista ordenada la cual se va construyendo recursivamente


