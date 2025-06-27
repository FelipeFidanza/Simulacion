from Cliente import Cliente
from Subsistema import Subsistema
from tabulate import tabulate


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
        self.tiempo_proxima_salida = float('inf')
        self.tiempo_arrepentimiento = tiempo_arrepentimiento
        self.mu = tiempo_final * len(self.subsistemas) / 300
        self.lamda = 300 / tiempo_final
        self.cant_arrepentidos = 0
        self.tiempo_final = tiempo_final

    def buscar_fila_mas_corta(self) -> Subsistema:
        subsistema_menor_fila = self.subsistemas[0]
        for subsistema in self.subsistemas:
            if len(subsistema.clientes) < len(subsistema_menor_fila.clientes):
                subsistema_menor_fila = subsistema
        return subsistema_menor_fila
    
    def avanzar_tiempo(self, tiempo):
        self.tiempo = tiempo

    def hay_clientes_en_sistema(self):
        for subsistema in self.subsistemas:
            if subsistema.clientes:
                return True
        return False

    def obtener_proxima_llegada(self, intervalo_entre_arribos):
        
        self.tiempo_proxima_llegada += intervalo_entre_arribos


    def obtener_proxima_salida(self) -> Subsistema:
        subsistema_proxima_salida = self.subsistemas[0]
        for subsistema in self.subsistemas:
            if subsistema.tiempo_proxima_salida < subsistema_proxima_salida.tiempo_proxima_salida:
                subsistema_proxima_salida = subsistema
        self.tiempo_proxima_salida = subsistema_proxima_salida.tiempo_proxima_salida
        return subsistema_proxima_salida

    def arribar_cliente(self, tiempo_atencion):
        """
        Genera un cliente con un tiempo de llegada y un tiempo de atención.
        El tiempo de llegada es el tiempo actual del sistema y el tiempo de atención es generado aleatoriamente.
        """
        
        cliente = Cliente(self.tiempo, tiempo_atencion)

        fila_a_ingresar = self.buscar_fila_mas_corta()

        fila_a_ingresar.recibir_cliente(cliente)
      

    def hallar_porcentaje_tiempo_ocioso(self):
        tiempo_oscioso_total = 0
        for subsistema in self.subsistemas:
            tiempo_oscioso_total += subsistema.sumatoria_tiempo_ocioso
        if self.tiempo == 0:
            return 0
        return tiempo_oscioso_total * 100 / self.tiempo_final

    def hallar_porcentaje_arrepentidos(self):
        clientes_atendidos = 0
        for subsistema in self.subsistemas:
            clientes_atendidos += subsistema.cantidad_total_clientes 
        if clientes_atendidos == 0:
            return 0
        return self.cant_arrepentidos * 100 / (clientes_atendidos + self.cant_arrepentidos)

    def imprimir_resultados(self, nro_corrida):
        clientes_atendidos = 0
        sumatoria_permanencia = 0
        sumatoria_atencion = 0
        sumatoria_tiempo_ocioso_sistema = 0

        for indice, subsistema in enumerate(self.subsistemas):
            clientes_atendidos += subsistema.cantidad_total_clientes
            sumatoria_permanencia += subsistema.sumatoria_tiempo_permanencia
            sumatoria_atencion += subsistema.sumatoria_tiempo_atencion
            sumatoria_tiempo_ocioso_sistema += subsistema.sumatoria_tiempo_ocioso
            print("Sumatoria de permanencia: ", sumatoria_permanencia, "sumatoria de atencion: ", sumatoria_atencion)
            sumatoria_espera = sumatoria_permanencia - sumatoria_atencion

            datos = [
            ["Cantidad de clientes atendidos en el subsistema", subsistema.cantidad_total_clientes],
            ["Promedio del tiempo de permanencia en el subsistema", subsistema.promedio_tiempo_permanencia], 
            ["Promedio del tiempo de espera en el subsistema", subsistema.promedio_tiempo_espera],           
            ["Promedio del tiempo de atención en el subsistema", subsistema.promedio_tiempo_atencion], 
            ["Porcentaje de tiempo ocioso del subsistema", subsistema.sumatoria_tiempo_ocioso * 100 / self.tiempo_final],
            ]

            print(tabulate(datos, headers=[f'Subsistema {indice + 1}', "Valor"], tablefmt="fancy_grid"))

        if clientes_atendidos > 0:
            promedio_permanencia_sistema = sumatoria_permanencia / clientes_atendidos
            promedio_espera = sumatoria_espera / clientes_atendidos
            promedio_atencion = sumatoria_atencion / clientes_atendidos
        else:
            promedio_permanencia_sistema = 0
            promedio_espera = 0
            promedio_atencion = 0

        tiempo_ocioso = self.hallar_porcentaje_tiempo_ocioso()
        arrepentidos = self.hallar_porcentaje_arrepentidos()
       
        
        datos = [
            ["Promedio del tiempo de permanencia en el sistema", promedio_permanencia_sistema],
            ["Promedio del tiempo de espera en el sistema", promedio_espera],
            ["Promedio del tiempo de atención en el sistema", promedio_atencion],
            ["Porcentaje de tiempo ocioso del sistema", tiempo_ocioso],
            ["Cantidad de clientes atendidos en el sistema", clientes_atendidos],
            ["Cantidad de clientes arrepentidos en el sistema", self.cant_arrepentidos],  
            ["Porcentaje de personas arrepentidas en el sistema", arrepentidos],
        ]

        print(tabulate(datos, headers=[f'Corrida {nro_corrida + 1}', "Valor"], tablefmt="fancy_grid"))
