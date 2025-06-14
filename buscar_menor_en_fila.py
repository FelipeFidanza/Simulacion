def buscar_menor(tps:list) -> list:
    """
    1. Esta función recibe una lista de tiempos de proxima salida (TPS) y devuelve el menor tiempo
    2. Esta función recibe una lista de cantidad de personas por servidor (NS) y devuelve la de menor cantidad.
    """
    menor = tps[0]
    pos = 0
    for i in range(1, len(tps)): 
        if tps[i] < menor:
            menor = tps[i]
            pos = i
    print("El menor en la fila es:", menor, "en la posición", pos)
    return [pos, menor]
