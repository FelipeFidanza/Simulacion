from tabulate import tabulate
from models.LectorCSV import LectorCSV
from models.Sistema import Sistema
from models.Subsistema import Subsistema 
from utils import segundos_a_hhmmss, armar_grafico
import json

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
        self.datos_globales = [0, 0, 0, 0, 0, 0, 0] # permanencia | espera | atencion | ocioso | atendidos | arrepentidos | arrepentidos%
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
                "corrida" : {
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
        datos_x_corrida = int(len(self.lector.intervalos_arribo)/self.cant_corridas)
    
        datos = [
            ["Cantidad de corridas", self.cant_corridas],
            ["Cantidad de servidores", self.cant_servidores],
            ["Tiempo total en segundos", 14400],
            ["Tiempo de arrepentimiento", 300],
    
        ]

        print(tabulate(datos, headers=[f'Datos de inicialización', "Valor"], tablefmt="fancy_grid")) 
        for i in range(self.cant_corridas):
            self.iniciar_corrida(datos_x_corrida, i)
            #input(f"\nCorrida {i + 1} finalizada. Presioná Enter para continuar...")

        for i in range(len(self.datos_globales)):
            self.datos_globales[i] = self.datos_globales[i] / self.cant_corridas


        datos = [
            ["Tiempo de permanencia", segundos_a_hhmmss(self.datos_globales[0])],
            ["Tiempo de espera", segundos_a_hhmmss(self.datos_globales[1])],
            ["Tiempo de atención", segundos_a_hhmmss(self.datos_globales[2])],
            ["Tiempo ocioso", str(round(self.datos_globales[3],2)) + "%"],
            ["Clientes atendidos", str(int(self.datos_globales[4]))],
         
            ["Porcentaje de arrepentidos", str(round(self.datos_globales[6],2)) + "%"],
        ]

        print(tabulate(datos, headers=[f'Resultados de la simulación (promedios)', "Valor"], tablefmt="fancy_grid"))

        # armar_grafico(self.resultados)





