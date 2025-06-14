def  tratarArrepentimiento(TPSk: int, T: int, tolerancia:int) -> bool:
    """
    Esta función toma el tiempo del servidor con la menor proxima salida (TPSk), el tiempo actual (T), la tolerancia
    de espera (en segundos), y determina si el cliente se arrepentira o no.
    """
    espera_estimada = TPSk - T
    arrepentido = False
    
    if espera_estimada > tolerancia:
        arrepentido = True
        print(f"El cliente se arrepiente de esperar más de {tolerancia} segundos. Tiempo estimado de espera: {espera_estimada} segundos.")
    else:
        print(f"El cliente no se arrepiente. Tiempo estimado de espera: {espera_estimada} segundos.")

    
    return arrepentido