from tabulate import tabulate
from LectorCSV import LectorCSV
from Sistema import Sistema
from Subsistema import Subsistema 


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

        datos = [
            ["Cantidad de corridas", self.cant_corridas],
            ["Cantidad de servidores", self.cant_servidores],
            ["Tiempo total en segundos", sistema.tiempo_final],
            ["Tiempo de arrepentimiento", sistema.tiempo_arrepentimiento],
    
        ]

        print(tabulate(datos, headers=[f'Datos de inicialización', "Valor"], tablefmt="fancy_grid"))

        sistema.imprimir_resultados(nro_corrida)


    def iniciar_simulacion(self):
        datos_x_corrida = int(len(self.lector.intervalos_arribo)/self.cant_corridas)
        for i in range(self.cant_corridas):
            self.iniciar_corrida(datos_x_corrida, i)



if __name__ == "__main__":
    lector = LectorCSV("variables.csv")
    sim = Simulacion(cant_corridas=1, cant_servidores=2, lector=lector)
    sim.iniciar_simulacion()

