import random
import math


def generar_tiempo_de_atencion(mu: float) -> float:
    """
    Esta función genera el tiempo de atención teniendo en cuenta la duración de la llamada, a través de la función exponencial.
    """
    # Genero un numero aleatorio con una distribución uniforme
    U = random.uniform(0, 1)
    return -math.log(U) / mu