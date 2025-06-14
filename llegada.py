from generar_ia import generar_intervalos_entre_arribos
from tratar_arrepentimiento import tratar_arrepentimiento
from generar_ta import generar_tiempo_de_atencion

def llegada(STP, TPLL, T, NS, N, STA, STO, CTO):
    """
    Esta función analiza todo el lado izquierdo del diagrama, es decir, para el caso de que el tiempo de llegada sea menor
    que el tiempo de salida.
    """



    tratar_arrepentimiento(3, 1, 1)
    # El arrepentimiento devuelve un bool, que determinará si el cliente entra o no al sistema,
    # si no entra hay que acumular el arrepentimiento en una var