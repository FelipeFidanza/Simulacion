import random
import math

def generar_intervalos_entre_arribos(lamda: float) -> float:
    """
    Esta función genera los intervalos entre arribos, teniendo en cuenta la INVERSA de la función exponencial.
    """

    U = random.uniform(0, 1)
    return -math.log(U) / lamda