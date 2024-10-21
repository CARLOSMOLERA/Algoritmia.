def director_deportivo(total, valoraciones, coste, presupuesto):
    pd={}
    if presupuesto==0 or total==0:#Si nos quedamos sin presupuesto o sin jugadores 
        return 0
    
    if (total, presupuesto) in pd.keys():#caso de que ya esté en el diccionario lo que estamos buscando: en este problema al no haber reutilización de elementos no sucede
        return pd[(total, presupuesto)]
    
    else:#caso de que no esté en la memoria

        if coste[total-1]>presupuesto:#si nos pasamos de presupuesto, no almacenas la valoración de este jugador en el diccionario
            pd[(total, presupuesto)] = director_deportivo(total-1, valoraciones,coste, presupuesto)
            # Aquí realmente  no tocas nada y solo quitas ese elemento

        else: #en el caso de que su coste si que quepa dentro del presupuesto
            pd[(total, presupuesto)]=max(

                director_deportivo(total-1, valoraciones,coste, presupuesto),
                valoraciones[total-1]+director_deportivo(total-1, valoraciones,coste, presupuesto-coste[total-1]),
            )
        #Nos quedamos con el valor máximo entre haberlo tenido en cuenta o no para el equipo

    return pd[(total, presupuesto)] #solo mando el elemento actual al buscar la mayor valoracion



#Cosas a tener en cuenta:

'''
1.Indices: los índices de las listas siempre van un elemento por detrás
2. La solución de desglosa hasta el inicio y se construye de abajo hacia arriba 
3. Se devuelve el ultimo elemento del diccionario o el elemento actual en la primera llamada al ser el que almacena la valoracion
'''

#NO NOS INTERESA EL CAMINO SEGUIDO, SINO CONSEGUIR MAXIMIZAR EL RESULTADO

def main():
    presupuesto=3000
    coste=[950,2400,500,2000]
    valoraciones = [6,1,3,8]
    total=4
    print(director_deportivo(total, valoraciones, coste, presupuesto))

main()







    










# Argumentos que toma el problema de la mochila:

'''
1.Pesos-Costes: coste asociado a cada uno de los elementos, es una lista
2.Valor-Valoración: valoración asociada a cada uno de los elementos
3.Capacidad-Presupuesto: total que puedo meter en la mochila
4. n-Total: es un control del total de elementos con que trabajo'''

