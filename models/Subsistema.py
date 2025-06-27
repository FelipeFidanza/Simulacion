from Cliente import Cliente

class Subsistema:
    """
    Clase que representa un subsistema dentro del sistema de atención al cliente.
    Cada subsistema tiene una lista de clientes en espera
    """

    def __init__(
        self,
        sistema
    ):
        self.clientes = []
        self.comienzo_tiempo_ocioso = 0
        self.cantidad_total_clientes = 0
        self.tiempo_proxima_salida = 0
        self.sumatoria_tiempo_ocioso = 0
        self.sumatoria_tiempo_permanencia = 0
        self.sumatoria_tiempo_atencion = 0
        self.sumatoria_tiempo_espera = 0
        self.sistema = sistema

    def finalizar_atencion(self):
        self.acumular_tiempo_permanencia()
        self.clientes.pop(0)
        if self.clientes:
            self.calcular_proxima_salida()
            self.sistema.avanzar_tiempo(self.tiempo_proxima_salida)
            self.acumular_tiempo_atencion(self.clientes[-1])
        else:
            self.comienzo_tiempo_ocioso = self.sistema.tiempo
            self.tiempo_proxima_salida = float("inf")

    def calcular_proxima_salida(self):
        cliente = self.clientes[0]
        cliente.tiempo_inicio_atencion = self.sistema.tiempo
        self.tiempo_proxima_salida = cliente.tiempo_inicio_atencion + cliente.tiempo_atencion

    def tratar_arrepentimiento(self):
        tiempo_espera = 0
        # [\(u . u)/, \(u . u)/,/ \(u . u)/, \(u . u)/]
        tiempo_espera += self.clientes[0].tiempo_inicio_atencion + \
            self.clientes[0].tiempo_atencion - self.sistema.tiempo

        for cliente in self.clientes[1:-1]:
            tiempo_espera += cliente.tiempo_atencion

        if tiempo_espera > self.sistema.tiempo_arrepentimiento:
            self.clientes.pop()
            self.sistema.cant_arrepentidos += 1
            return
        
        self.sumatoria_tiempo_espera += tiempo_espera

        self.cantidad_total_clientes += 1

    def recibir_cliente(self, cliente):
        self.clientes.append(cliente)

        if len(self.clientes) == 1:
            self.calcular_proxima_salida()
            return

        self.tratar_arrepentimiento()

    def acumular_tiempo_ocioso(self):
        self.sumatoria_tiempo_ocioso += self.sistema.tiempo - self.comienzo_tiempo_ocioso

    def acumular_tiempo_atencion(self, cliente: Cliente):
        self.sumatoria_tiempo_atencion += cliente.tiempo_atencion

    def acumular_tiempo_permanencia(self):
        self.sumatoria_tiempo_permanencia += (
            self.sistema.tiempo_proxima_llegada - self.sistema.tiempo) * len(self.clientes)

    @property
    def promedio_tiempo_permanencia(self):
        return self.sumatoria_tiempo_permanencia / self.cantidad_total_clientes
    
    @property
    def promedio_tiempo_espera(self):
        return self.sumatoria_tiempo_espera / self.cantidad_total_clientes
    
    @property
    def promedio_tiempo_atencion(self):
        return self.sumatoria_tiempo_atencion / self.cantidad_total_clientes