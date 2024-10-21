def planear_gira(c, r, entradas, idx=0):
    # Caso base: si no hay más conciertos o se ha alcanzado la capacidad
    if idx >= len(entradas) or c == 0:
        return 0

    # Opción 1: No tomar el concierto actual
    max_entradas = planear_gira(c, r, entradas, idx + 1)

    # Opción 2: Tomar el concierto actual
    if c > 0:
        # Saltar el día actual y los 3 días adicionales
        next_idx = idx + r # r es 3 en este caso
        max_entradas = max(max_entradas, entradas[idx] + planear_gira(c - 1, r, entradas, next_idx))

    return max_entradas

def main():
    entradas = [3000, 6000, 7000, 8000, 9000]
    c = 3  # Número máximo de conciertos
    r = 3  # Intervalo de días entre conciertos (3 días)
    resultado = planear_gira(c, r, entradas)
    print(resultado)

main()
