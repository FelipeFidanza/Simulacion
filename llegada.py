from generar_ia import generar_intervalos_entre_arribos
from buscar_menor_en_fila import buscar_menor
from tratar_arrepentimiento import tratar_arrepentimiento
from generar_ta import generar_tiempo_de_atencion

def llegada(STP: list, TPLL: list, TPS: list, k: int, T: list, NS: list, N: list, STA: list, STO: list, CTO: list, lamda: float, mu: float , arrepentidos: int):
    """
    Esta función analiza todo el lado izquierdo del diagrama, es decir, para el caso de que el tiempo de llegada sea menor
    que el tiempo de salida.
    """
    for i in range(len(STP)):
      # sumatoria de tiempo de permanencia en el subsistema i
      STP[i] += (TPLL[k] - T) * NS[i]

    T = TPLL

    IA = generar_intervalos_entre_arribos(lamda) # Intervalo entre arribos

    TPLL = T + IA

    p = buscar_menor(NS)

    # El arrepentimiento devuelve un bool, que determinará si el cliente entra o no al sistema,
    # si no entra hay que acumular el arrepentimiento en una var
    if tratar_arrepentimiento(TPS[p], T, 300): # Se arrepiente
       arrepentidos += 1
       return
    
    # En caso de que entre al subsistema
    NS[p] += 1

    N[p] += 1

    if NS[p] == 1:
       TA = generar_tiempo_de_atencion(mu)

       TPS[p] = T + TA

       STA[p] += TA

       STO[p] += T - CTO[p]
       

