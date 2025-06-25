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

    def iniciar_corrida(self, datos_x_corrida):
        sistema = Sistema(subsistemas=[])
        subsistemas = [Subsistema(sistema)
                       for _ in range(self.cant_servidores)]
        sistema.subsistemas = subsistemas

        for _ in range(datos_x_corrida):
            if sistema.tiempo_final <= sistema.tiempo:
                [intervalo, tiempo_atencion] = self.lector.obtener_siguiente()
                sistema.obtener_proxima_llegada(intervalo)
                subsistema_prox_salida = sistema.obtener_proxima_salida()

                if sistema.tiempo_proxima_llegada <= sistema.tiempo_proxima_salida:
                    sistema.arribar_cliente(
                        tiempo_atencion, sistema.tiempo_proxima_llegada)
                else:
                    subsistema_prox_salida.finalizar_atencion()
            else:  
                break

        self.imprimir_resultados()


    def iniciar_simulacion(self):
        datos_x_corrida = int(len(self.lector.intervalos_arribo)/self.cant_corridas)
        for _ in range(self.cant_corridas):
            self.iniciar_corrida(datos_x_corrida)

    def imprimir_resultados(self):
        pass


if __name__ == "__main__":
    lector = LectorCSV("variables.csv")
    sim = Simulacion(cant_corridas=5, cant_servidores=5, lector=lector)
    sim.iniciar_simulacion()

