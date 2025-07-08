from tabulate import tabulate
from models.LectorCSV import LectorCSV
from models.Sistema import Sistema
from models.Subsistema import Subsistema
from utils import segundos_a_hhmmss, armar_grafico
import json
from scipy.stats import t
import numpy as np

class Simulacion:
    def __init__(
        self,
        cant_corridas,
        cant_servidores,
        lector: LectorCSV
    ):
        self.cant_corridas = cant_corridas
        self.cant_servidores = cant_servidores
        self.lector = lector
        # permanencia | espera | atencion | ocioso | atendidos | arrepentidos | arrepentidos%
        self.datos_globales = [0, 0, 0, 0, 0, 0, 0]
        self.resultados = []

    def iniciar_corrida(self, datos_x_corrida, nro_corrida):
        sistema = Sistema(subsistemas=[])
        subsistemas = [Subsistema(sistema)
                       for _ in range(self.cant_servidores)]
        sistema.subsistemas = subsistemas

        [intervalo, tiempo_atencion] = self.lector.obtener_siguiente()
        sistema.obtener_proxima_llegada(intervalo)

        while sistema.tiempo < sistema.tiempo_final:
            if (datos_x_corrida > 0 or sistema.hay_clientes_en_sistema()):
                subsistema_prox_salida = sistema.obtener_proxima_salida()

                if sistema.tiempo_proxima_llegada <= sistema.tiempo_proxima_salida and datos_x_corrida > 0:
                    sistema.avanzar_tiempo(sistema.tiempo_proxima_llegada)
                    sistema.arribar_cliente(tiempo_atencion)

                    datos_x_corrida -= 1
                    if datos_x_corrida > 0:
                        intervalo, tiempo_atencion = self.lector.obtener_siguiente()
                        sistema.obtener_proxima_llegada(intervalo)
                else:
                    sistema.avanzar_tiempo(sistema.tiempo_proxima_salida)
                    subsistema_prox_salida.finalizar_atencion()
            else:
                # Si ya no van a llegar más clientes y ya todos fueron atendidos se acumula el tiempo ocioso restante hasta el final de la corrida
                for subsistema in sistema.subsistemas:
                    subsistema.comienzo_tiempo_ocioso = sistema.tiempo
                sistema.tiempo = sistema.tiempo_final
                for subsistema in sistema.subsistemas:
                    subsistema.acumular_tiempo_ocioso()

        resultado = sistema.imprimir_resultados(nro_corrida)
        self.resultados.append(
            {
                "corrida": {
                    "Tiempo de permanencia": resultado[0],
                    "Tiempo de espera": resultado[1],
                    "Tiempo de atención": resultado[2],
                    "Porcentaje de tiempo ocioso": resultado[3],
                    "Clientes atendidos": resultado[4],
                    "Clientes arrepentidos": resultado[5],
                    "Porcentaje de arrepentidos": resultado[6],
                }
            }
        )
        self.datos_globales = [x + y for x, y in zip(self.datos_globales, resultado)]

    def iniciar_simulacion(self):
        datos_x_corrida = int(len(self.lector.intervalos_arribo) / self.cant_corridas)

        # Preparar datos para la tabla
        tabla_datos = [
            ["Datos de inicialización", ""],
            ["Cantidad de corridas", str(self.cant_corridas)],
            ["Cantidad de servidores", str(self.cant_servidores)],
            ["Tiempo total en segundos", str(14400)],
            ["Tiempo de arrepentimiento", str(300)],
            ["", ""],  # Separador
        ]

        # Ejecutar simulaciones
        for i in range(self.cant_corridas):
            self.iniciar_corrida(datos_x_corrida, i)
            # input(f"\nCorrida {i + 1} finalizada. Presioná Enter para continuar...")

        # Calcular promedios globales
        for i in range(len(self.datos_globales)):
            self.datos_globales[i] /= self.cant_corridas

        # Extraer valores por métrica de las corridas
        permanencias = [c["corrida"]["Tiempo de permanencia"] for c in self.resultados]
        esperas = [c["corrida"]["Tiempo de espera"] for c in self.resultados]
        atenciones = [c["corrida"]["Tiempo de atención"] for c in self.resultados]
        ociosos = [c["corrida"]["Porcentaje de tiempo ocioso"] for c in self.resultados]
        arrepentidos = [c["corrida"]["Porcentaje de arrepentidos"] for c in self.resultados]

        # Calcular intervalos de confianza al 95%
        ic_esp = calcular_ic_95(esperas)
        ic_ocio = calcular_ic_95(ociosos)
        ic_arr = calcular_ic_95(arrepentidos)

        # Agregar intervalos de confianza y valores medios a la tabla
        tabla_datos.extend([
            ["Intervalos de confianza al 95% y valores medios", ""],
            ["Tiempo de espera", f"{segundos_a_hhmmss(ic_esp[0])} - {segundos_a_hhmmss(ic_esp[1])} (Media {segundos_a_hhmmss(self.datos_globales[1])})"],
            ["Tiempo ocioso", f"{ic_ocio[0]}% - {ic_ocio[1]}% (Media {round(self.datos_globales[3], 2)}%)"],
            ["Porcentaje de arrepentidos", f"{ic_arr[0]}% - {ic_arr[1]}% (Media {round(self.datos_globales[6], 2)}%)"],
        ])

        # Mostrar tabla consolidada
        print(tabulate(tabla_datos, headers=["Métrica", "Valor"], tablefmt="fancy_grid"))

def calcular_ic_95(valores):
    n = len(valores)
    media = np.mean(valores)
    s = np.std(valores, ddof=1)
    t_crit = t.ppf(0.975, df=n-1)  # 95% de confianza
    margen_error = t_crit * (s / np.sqrt(n))
    return round(media - margen_error, 2), round(media + margen_error, 2)