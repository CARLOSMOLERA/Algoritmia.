#Función director deportivo


# Es que es casi como el problema de la mochila pero es que no se ya cómo hacerlo
def director_deportivo(valoraciones, fichas, budget, ):
    if budget<=fichas[0]:
        return 0
    elif len(valoraciones)==1:#cabe en el presupuesto
        return valoraciones[0]

    else:#caso de que no me haya pasado de presupuesto
        #Busco mi elemento actual en la lista de valoraciones
        
        for i in range(len(valoraciones[1:])):#valido el máximo aqui dentro 
            suma=max(
                    director_deportivo(valoraciones[i+1:], fichas[i+1:], budget),
                   valoraciones[0]+ director_deportivo(valoraciones[i+1:], fichas[i+1:], budget-fichas[0])
                    )
            

        return suma
    #maximo arrosega y valoraciones es el del actual
    

def main():
    # Ejemplo de valoraciones y fichas
    valoraciones = [6, 1, 3, 8]  # Valoraciones de los jugadores
    fichas = [950, 2400, 500, 2000]          # Costos de los jugadores
    budget = 3000                        # Presupuesto total

    # Llama a la función y muestra el resultado
    resultado = director_deportivo(valoraciones, fichas, budget)
    print(f"Máxima valoración que se puede obtener: {resultado}")
main()