from llegada import llegada
from salida import salida
from buscar_menor_en_fila import buscar_menor


# Definición de variables

T = 0           # Tiempo
TF = 14400      # Tiempo que dura la simulacion (4hs)
C = 5           # Cantidad de servidores en el sistema
TPLL = 0        # Tiempo de la proxima llegada
TPS = [10000000] * C  # Tiempo de la proxima salida del subsistema i
NS = [0] * C          # Cantidad de personas en el subsistema i
N = [0] * C         # Cantidad total de personas que pasaron por el subsistema i
STP = [0] * C         # Sumatoria de tiempo de permanencia en el subsistema i
STA = [0] * C         # Sumatoria de tiempo de atención del subsistema i
STO = [0] * C         # Sumatoria de tiempo ocioso en el subsistema i
CTO = [0] * C         # Comienzo de tiempo ocioso de subsistema i
PPS = [0] * C         # Promedio de permanencia en el subsistema i
PTE = [0] * C         # Promedio de tiempo de espera en cola en el subsistema i
PTA = [0] * C        # Promedio de tiempo de atención en el subsistema i
PTO = [0] * C         # Porcentaje de tiempo ocioso del subsistema i
mu = TF * C/ 300       # Tasa de atención del sistema (300: es la cantidad de llegadas que registramos)
lamda = 300/TF     # Tasa de llegada al sistema 
arrepentidos = 0    # Contador de arrepentidos en el sistema


# Itera hasta que el tiempo de la simulación alcance el tiempo máximo establecido
while T <= TF:
    k = buscar_menor(TPS)  
    if TPLL <= TPS[k]:
        llegada(STP, TPLL, TPS, k, T, NS, N, STA, STO, CTO, lamda, mu, arrepentidos)
    else:
        salida(STP, TPS, k, T, NS, STA, CTO, mu)

#--------------------------------------------------Generar informes--------------------------------------------------#

for i in range(5):
    # Promedio de permanencia en el subsistema
    PPS = STP / N

    # Promedio de espera en cola en el subsistema
    PTE = (STP - STA) / N

    # Promedio de atención en cola en el subsistema
    PTA = STA / N

    # Porcentaje de arrepentimiento
    PA = arrepentidos * 100 / N

    print(f"Promedio de permanencia en el subsistema {i}: {PPS}.")
    print(f"Promedio de espera en cola en el subsistema {i}: {PTE}.")
    print(f"Promedio de atención en cola en el subsistema {i}: {PTA}.")
    print(f"Porcentaje de personas arrepentidas en el subsistema {i}: {PPS}.")
    print()

# Porcentaje de tiempo ocioso del sistema
PTO = STO * 100 / T

print(f"Porcentaje de tiempo ocioso en el sistema: {PTO}%.")


