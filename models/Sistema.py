from Cliente import Cliente
from Subsistema import Subsistema


class Sistema:
    """
    Clase que representa el sistema de atención al cliente, 
    que contiene múltiples subsistemas (servidores).
    Opcionalmente se puede definir un tiempo final y de arrepentimiento.
    Por defecto, el tiempo final es 14400 segundos (4 horas) y el tiempo de arrepentimiento es 300 segundos (5 minutos). 
    """

    def __init__(
        self,
        subsistemas,
        tiempo_final=14400,
        tiempo_arrepentimiento=300,
    ):
        self.subsistemas : Subsistema = subsistemas
        self.tiempo = 0
        self.tiempo_proxima_llegada = 0
        self.tiempo_proxima_salida = 0
        self.tiempo_arrepentimiento = tiempo_arrepentimiento
        self.mu = tiempo_final * len(self.subsistemas) / 300
        self.lamda = 300 / tiempo_final
        self.cant_arrepentidos = 0
        self.tiempo_final = tiempo_final

    def buscar_fila_mas_corta(self) -> Subsistema:
        # TODO: incializar la variable de tal forma que nunca cambiemos el tipo int -> objeto Subsistema
        subsistema_menor_fila = self.subsistemas[0]
        for subsistema in self.subsistemas:
            if len(subsistema.clientes) < len(subsistema_menor_fila.clientes):
                subsistema_menor_fila = subsistema
        return subsistema_menor_fila

    def obtener_proxima_llegada(self, intervalo_entre_arribos):
        self.tiempo_proxima_llegada = self.tiempo + intervalo_entre_arribos

    def obtener_proxima_salida(self) -> Subsistema:
        subsistema_proxima_salida = self.subsistemas[0]
        for subsistema in self.subsistemas:
            if subsistema.tiempo_proxima_salida < subsistema_proxima_salida.tiempo_proxima_salida:
                subsistema_proxima_salida = subsistema
        self.tiempo_proxima_salida = subsistema_proxima_salida.tiempo_proxima_salida
        return subsistema_proxima_salida

    def arribar_cliente(self, tiempo_atencion, tiempo_prox_llegada):
        """
        Genera un cliente con un tiempo de llegada y un tiempo de atención.
        El tiempo de llegada es el tiempo actual del sistema y el tiempo de atención es generado aleatoriamente.
        """
        cliente = Cliente(tiempo_prox_llegada, tiempo_atencion)

        fila_a_ingresar = self.buscar_fila_mas_corta()

        fila_a_ingresar.recibir_cliente(cliente)

        self.tiempo = tiempo_prox_llegada

    def hallar_porcentaje_tiempo_ocioso(self):
        tiempo_oscioso_total = 0
        for subsistema in self.subsistemas:
            tiempo_oscioso_total += subsistema.sumatoria_tiempo_ocioso

        return tiempo_oscioso_total * 100 / self.tiempo

    def hallar_porcentaje_arrepentidos(self):
        clientes_sistema = 0
        for subsistema in self.subsistemas:
            clientes_sistema += subsistema.cantidad_total_clientes 
        return self.cant_arrepentidos * 100 / clientes_sistema

    def imprimir_resultados(self):
        clientes_sistema = 0
        promedio_permanencia_sistema = 0
        promedio_espera_sistema = 0
        promedio_atencion = 0
        for subsistema in self.subsistemas:
            clientes_sistema += subsistema.cantidad_total_clientes
            promedio_permanencia_sistema += subsistema.promedio_tiempo_permanencia
            promedio_espera_sistema += subsistema.promedio_tiempo_espera
            promedio_atencion += subsistema.promedio_tiempo_atencion
        tiempo_ocioso = self.hallar_porcentaje_tiempo_ocioso()
        arrepentidos = self.hallar_porcentaje_arrepentidos()

        print("Promedio del tiempo de permanencia en el sistema:" + " "*5 + "| " + promedio_permanencia_sistema) #49
        print("Promedio del tiempo de espera en el sistema:" + " "*10 + "| " + promedio_espera_sistema) #44
        print("Promedio del tiempo de atencion en el sistema:" + " "*8 + "| "  + promedio_atencion) #46
        print("Porcentaje de tiempo ocioso del sistema:" + " "*14 + "| " + tiempo_ocioso) #40
        print("Porcentaje de personas arrepentidas en el sistema:" + " "*4 + "| " + arrepentidos) #50