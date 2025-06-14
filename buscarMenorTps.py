def buscarMenorTps(tps:list):
    menor = tps[0]
    for i in range(1, len(tps)):
        if tps[i] < menor:
            menor = tps[i]
    print("El menor tiempo de salida es:", menor)
    return menor
