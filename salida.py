from buscar_menor_en_fila import buscar_menor
from generar_ta import generar_tiempo_de_atencion

def salida(STP:list, TPS:list, k:int, T:int, NS:list,STA:list, CTO:list, mu:float):
    """
    Analiza todo el lado derecho del diagrama, es decir, para el caso de que el tiempo de llegada sea mayor
    que el tiempo de salida, entonces se producira una salida del sistema.
    """

    for i in range(len(STP)):
      # sumatoria de tiempo de permanencia en el subsistema i
      STP[i] += TPS[k] - T * NS[i]
    
    T = TPS[k]
    NS[k] -= 1

    if NS[k] >= 1:
    # ya hay personas en el subsistema k
      TA = generar_tiempo_de_atencion(mu)
      TPS[k] = T + TA
      STA[k]+= TA
    else:
      # fila vacia, comienzo de tiempo ocioso de subsistema k
      CTO[k] = T
      TPS[k] = 10000000


    