import random
import math
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
        tiempo_final = 14400,
        tiempo_arrepentimiento = 300,
    ): 
        self.subsistemas = subsistemas
        self.tiempo = 0
        self.tiempo_proxima_llegada = 0
        self.tiempo_proxima_salida = 0
        self.tiempo_arrepentimiento = tiempo_arrepentimiento
        self.mu = tiempo_final * len(self.subsistemas) / 300
        self.lamda = 300 / tiempo_final
        self.cant_arrepentidos = 0
        self.tiempo_final = tiempo_final


    def generar_ia(self):
        """Genera un intervalo entre arribos de clientes al sistema con la inversa de la distribución exponencial"""
        #TODO : tiene que leer un csv con los nros aleatorios
        U = random.uniform(0, 1)
        return -math.log(U) / self.lamda
    
    def generar_ta(self):
        """Genera un tiempo de atención para un cliente con la inversa de la distribución exponencial"""
        #TODO : tiene que leer un csv con los nros aleatorios
        U = random.uniform(0, 1)
        return -math.log(U) / self.mu
    
    def buscar_fila_mas_corta(self) -> Subsistema:
        #TODO: incializar la variable de tal forma que nunca cambiemos el tipo int -> objeto Subsistema
        subsistema_menor_fila = self.subsistemas[0]
        for subsistema in self.subsistemas: 
            if len(subsistema.clientes) < len(subsistema_menor_fila.clientes):
                subsistema_menor_fila = subsistema
        return subsistema_menor_fila
    
    def obtener_proxima_llegada(self):
        intervalo_entre_arribos = self.generar_ia()
        self.tiempo_proxima_llegada = self.tiempo + intervalo_entre_arribos
       
    def obtener_proxima_salida(self):
        subsistema_proxima_salida = self.subsistemas[0]
        for subsistema in self.subsistemas: 
            if subsistema.tiempo_proxima_salida < subsistema_proxima_salida.tiempo_proxima_salida:
                subsistema_proxima_salida = subsistema
        self.tiempo_proxima_salida = subsistema_proxima_salida.tiempo_proxima_salida
        return subsistema_proxima_salida
    
    

    
    # Para nosotros que esto vaya en el flujo nomas :) 

    # def verificar_proximo_evento(self):
    #     """
    #     Verifica cuál es el próximo evento a ocurrir en el sistema: una llegada o una salida.
    #     """
    #     self.obtener_proxima_llegada()
    #     self.obtener_proxima_salida()

    #     return self.tiempo_proxima_llegada <= self.tiempo_proxima_salida
    
    def arribar_cliente(self):
        """
        Genera un cliente con un tiempo de llegada y un tiempo de atención.
        El tiempo de llegada es el tiempo actual del sistema y el tiempo de atención es generado aleatoriamente.
        """
        tiempo_llegada = self.tiempo
        tiempo_atencion = self.generar_ta()
        cliente = Cliente(tiempo_llegada, tiempo_atencion)

        fila_a_ingresar = self.buscar_fila_mas_corta()

        fila_a_ingresar.recibir_cliente(cliente)
        
    # def verificar_tiempo_final(self):
    #     return self.tiempo_final <= self.tiempo