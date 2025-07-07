from models.Cliente import Cliente
from models.Subsistema import Subsistema
from tabulate import tabulate
from utils import segundos_a_hhmmss

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
        self.subsistemas = subsistemas
        self.tiempo = 0
        self.tiempo_proxima_llegada = 0
        self.tiempo_proxima_salida = float('inf')
        self.tiempo_arrepentimiento = tiempo_arrepentimiento
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
    



    @property
    def cant_arrepentidos(self):
        cant_arrepentidos = 0
        for subsistema in self.subsistemas:
            cant_arrepentidos += subsistema.cantidad_arrepentidos
        return cant_arrepentidos

    def hallar_porcentaje_arrepentidos(self):
        clientes_totales = 0
        for subsistema in self.subsistemas:
            clientes_totales += subsistema.cantidad_total_clientes
        if clientes_totales == 0:
            return 0
        return self.cant_arrepentidos * 100 / clientes_totales


    def imprimir_resultados(self, nro_corrida):
        clientes_atendidos_sistema = 0
        sumatoria_permanencia_sistema = 0
        sumatoria_atencion_sistema = 0
        sumatoria_tiempo_ocioso_sistema = 0
        sumatoria_espera_sistema = 0

        for indice, subsistema in enumerate(self.subsistemas):
            clientes_atendidos = subsistema.clientes_atendidos
            sumatoria_permanencia = subsistema.sumatoria_tiempo_atencion + subsistema.sumatoria_tiempo_espera
            sumatoria_atencion = subsistema.sumatoria_tiempo_atencion
            sumatoria_espera = subsistema.promedio_tiempo_espera
  

            # datos = [
            # ["Cantidad de clientes atendidos en el subsistema", subsistema.clientes_atendidos],
            # ["Promedio del tiempo de permanencia en el subsistema", subsistema.promedio_tiempo_permanencia],
            # ["Promedio del tiempo de espera en el subsistema", subsistema.promedio_tiempo_espera],
            # ["Promedio del tiempo de atención en el subsistema", subsistema.promedio_tiempo_atencion],
            # ["Porcentaje de tiempo ocioso del subsistema", subsistema.sumatoria_tiempo_ocioso * 100 / self.tiempo_final],
            # ]

            # print(tabulate(datos, headers=[f'Subsistema {indice + 1}', "Valor"], tablefmt="fancy_grid"))

            sumatoria_tiempo_ocioso_sistema += subsistema.sumatoria_tiempo_ocioso
            clientes_atendidos_sistema += clientes_atendidos
            sumatoria_permanencia_sistema += sumatoria_permanencia
            sumatoria_atencion_sistema += sumatoria_atencion
            sumatoria_espera_sistema += sumatoria_espera

        # if clientes_atendidos > 0:
        promedio_permanencia_sistema = sumatoria_permanencia_sistema / clientes_atendidos_sistema
        promedio_espera = sumatoria_espera_sistema / len(self.subsistemas)
        promedio_atencion = sumatoria_atencion_sistema / clientes_atendidos_sistema
        # else:
        #     promedio_permanencia_sistema = 0
        #     promedio_espera = 0
        #     promedio_atencion = 0

        tiempo_ocioso = self.hallar_porcentaje_tiempo_ocioso() / len(self.subsistemas)
        arrepentidos = self.hallar_porcentaje_arrepentidos()
       
        
        datos = [
            ["Promedio del tiempo de permanencia en el sistema", segundos_a_hhmmss(promedio_permanencia_sistema)],
            ["Promedio del tiempo de espera en el sistema", segundos_a_hhmmss(promedio_espera)],
            ["Promedio del tiempo de atención en el sistema", segundos_a_hhmmss(promedio_atencion)],
            ["Porcentaje de tiempo ocioso del sistema", str(round(tiempo_ocioso,2)) + "%"],
            ["Cantidad de clientes atendidos en el sistema", clientes_atendidos_sistema],
            ["Cantidad de clientes arrepentidos en el sistema", self.cant_arrepentidos],  
            ["Porcentaje de personas arrepentidas en el sistema", str(round(arrepentidos,2)) + "%"],
        ]

        print(tabulate(datos, headers=[f'Corrida {nro_corrida + 1}', "Valor"], tablefmt="fancy_grid"))


        return [promedio_permanencia_sistema, 
                promedio_espera, 
                promedio_atencion, 
                round(tiempo_ocioso,2), 
                clientes_atendidos_sistema, 
                self.cant_arrepentidos, 
                round(arrepentidos,2)
                ]

    