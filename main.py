from entry import *
from exit import *

# Definición de variables

T = 0           # Tiempo
TPLL = 0        # Tiempo de la proxima llegada
TPS = 10000000  # Tiempo de la proxima salida del subsistema
NS = 0          # Cantidad de personas en el subsistema i
N = 0           # Cantidad total de personas que pasaron por el subsistema i
STP = 0         # Sumatoria de tiempo de permanencia en el subsistema i
STA = 0         # Sumatoria de tiempo de atención del subsistema i
TF = 14400      # Tiempo que dura la simulacion
STO = 0         # Sumatoria de tiempo ocioso en el subsistema i
CTO = 0         # Comienzo de tiempo ocioso de subsistema i
PPS = 0         # Promedio de permanencia en el subsistema i
PTE = 0         # Promedio de tiempo de espera en cola en el subsistema i
PTA = 0         # Promedio de tiempo de atención en el subsistema i
PTO = 0         # Porcentaje de tiempo ocioso del subsistema i


