from LectorCSV import LectorCSV
from Sistema import Sistema
from Subsistema import Subsistema


class Simulacion:
    def __init__(
        self,
        cant_corridas,
        cant_servidores
    ):
        self.cant_corridas = cant_corridas
        self.cant_servidores = cant_servidores

    def iniciar_corrida(self, datos_x_corrida):
        sistema = Sistema(subsistemas=[])
        subsistemas = [Subsistema(sistema)
                       for _ in range(self.cant_servidores)]
        sistema.subsistemas = subsistemas

        for cliente in datos_x_corrida:
            if sistema.tiempo_final <= sistema.tiempo:
                [intervalo, tiempo_atencion] = lector.obtener_siguiente()
                sistema.obtener_proxima_llegada(intervalo)
                subsistema_prox_salida = sistema.obtener_proxima_salida()

                if sistema.tiempo_proxima_llegada <= sistema.tiempo_proxima_salida:
                    sistema.arribar_cliente(
                        tiempo_atencion, sistema.tiempo_proxima_llegada)
                else:
                    subsistema_prox_salida.finalizar_atencion()
            else:
                self.imprimir_resultados()
                break

    def iniciar_simulacion(self):
        datos_x_corrida = int(lector.intervalos_arribo/self.cant_corridas)
        for corrida in range(1, self.cant_corridas + 1):
            self.iniciar_corrida(datos_x_corrida)

    def imprimir_resultados():
        pass


lector = LectorCSV('variables.csv')
