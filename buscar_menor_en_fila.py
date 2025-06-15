def buscar_menor(fila:list) -> int:
    """
    1. Esta función recibe una lista de tiempos de proxima salida (fila) y devuelve la posicion del menor tiempo
    2. Esta función recibe una lista de cantidad de personas por servidor (NS) y devuelve la posicion de menor cantidad.
    """
    menor = fila[0]
    pos = 0
    for i in range(1, len(fila)): 
        if fila[i] < menor:
            menor = fila[i]
            pos = i
    print("El menor en la fila es:", menor, "en la posición", pos)
    return pos
