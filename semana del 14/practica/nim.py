#Algoritmo de configuración del jeugo del NIM


def nim(m, n):

    # Caso base: si n es menor o igual a m, se puede ganar
    if n <= m:
        return True, 

    for i in range(1, m + 1):
        # Probar quitar i piedras
        if not nim(m, n - i):  # Llamada recursiva
            return True  # Si encontramos una jugada ganadora

    return False  # Si no hay jugadas ganadoras

def main():
    m = 3  # Cantidad de piedras que se pueden quitar
    n = 6  # Número inicial de piedras
    ganador = nim(m, n)

    if ganador:
        print(f"Se puede ganar comenzando con {n} piedras")
    else:
        print(f"No se puede ganar comenzando con {n} piedras.")

main()


   