from Cliente import Cliente
import math

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
        self.tiempo_proxima_salida = float('inf')
        self.sumatoria_tiempo_ocioso = 0
        self.sumatoria_tiempo_permanencia = 0
        self.sumatoria_tiempo_atencion = 0
        self.sumatoria_tiempo_espera = 0
        self.sistema = sistema

    def finalizar_atencion(self):
        cliente_actual = self.clientes.pop(0)
        if math.isfinite(self.sistema.tiempo):
            tiempo_permanencia = self.sistema.tiempo - cliente_actual.tiempo_llegada
          

        if self.clientes:
            self.calcular_proxima_salida()
        else:
            self.comienzo_tiempo_ocioso = self.sistema.tiempo
            self.tiempo_proxima_salida = float("inf")


    def calcular_proxima_salida(self):
        cliente = self.clientes[0]
        cliente.tiempo_inicio_atencion = self.sistema.tiempo
        self.tiempo_proxima_salida = cliente.tiempo_inicio_atencion + cliente.tiempo_atencion

        if math.isfinite(self.tiempo_proxima_salida):
           self.sumatoria_tiempo_atencion += cliente.tiempo_atencion
       

    def tratar_arrepentimiento(self):
        cliente_en_servicio = self.clientes[0]
        tiempo_transcurrido_en_servicio = self.sistema.tiempo - cliente_en_servicio.tiempo_inicio_atencion

        # tiempo de espera del cliente que ya esta siendo atendido
        tiempo_espera = cliente_en_servicio.tiempo_atencion - tiempo_transcurrido_en_servicio


        for cliente in self.clientes[1:-1]:
            # tiempo de espera del cliente que esta siendo atendido mas los clientes que esten por delante en la fila sin contar el que llego recien
            tiempo_espera += cliente.tiempo_atencion

        if tiempo_espera > self.sistema.tiempo_arrepentimiento:
            self.clientes.pop()
            self.sistema.cant_arrepentidos += 1
        else:
            self.sumatoria_tiempo_espera += tiempo_espera
            self.cantidad_total_clientes += 1
           

    def recibir_cliente(self, cliente):
        self.clientes.append(cliente)
        
        if len(self.clientes) == 1:
            self.calcular_proxima_salida()  
            self.cantidad_total_clientes += 1        
        else:
            self.tratar_arrepentimiento()

    def acumular_tiempo_ocioso(self):
        self.sumatoria_tiempo_ocioso += self.sistema.tiempo - self.comienzo_tiempo_ocioso

    def acumular_tiempo_atencion(self, cliente: Cliente):
        self.sumatoria_tiempo_atencion += cliente.tiempo_atencion

    def acumular_tiempo_permanencia(self, tiempo_prox_evento=float('inf')):
        if math.isfinite(tiempo_prox_evento):
          
            self.sumatoria_tiempo_permanencia += (tiempo_prox_evento - self.sistema.tiempo) * len(self.clientes)
           

    @property
    def promedio_tiempo_permanencia(self):
        if self.cantidad_total_clientes == 0:
            return 0
        return self.sumatoria_tiempo_permanencia / self.cantidad_total_clientes
    
    @property
    def promedio_tiempo_espera(self):
        if self.cantidad_total_clientes == 0:
            return 0
        return self.sumatoria_tiempo_espera / self.cantidad_total_clientes
    
    @property
    def promedio_tiempo_atencion(self):
        if self.cantidad_total_clientes == 0:
            return 0
        return self.sumatoria_tiempo_atencion / self.cantidad_total_clientes