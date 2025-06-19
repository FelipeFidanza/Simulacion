from ast import Index
import random
import math

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
        self.tiempo_arrepentimiento = tiempo_arrepentimiento
        self.mu = tiempo_final * len(self.subsistemas) / 300
        self.lamda = 300 / tiempo_final
        self.cant_arrepentidos = 0
        self.intervalo_entre_arribos = 0
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
    
    def buscar_cola_mas_corta(self):
        #TODO: incializar la variable de tal forma que nunca cambiemos el tipo int -> objeto Subsistema
        subsistema_menor_fila = float("inf")
        for subsistema in self.subsistemas: 
            cantidad_clientes = len(subsistema.clientes)
            if cantidad_clientes > subsistema_menor_fila:
                subsistema_menor_fila = subsistema
        return subsistema_menor_fila
       
    def obtener_proxima_salida(self):
        subsistema_proxima_salida = float("inf")
        for subsistema in self.subsistemas: 
            proxima_salida = subsistema.tiempo_proxima_salida
            if proxima_salida < subsistema_proxima_salida:
                subsistema_proxima_salida = subsistema
        return subsistema_proxima_salida
        
    def verificar_tiempo(self):
        pass

class Cliente:
    def __init__(
        self, 
        tiempo_llegada,
        tiempo_atencion,
    ):
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_atencion = tiempo_atencion
        self.arrepentido = False
        
        
class Subsistema:
    """
    Clase que representa un subsistema dentro del sistema de atención al cliente.
    Cada subsistema tiene una lista de clientes en espera
    """
    def __init__(
        self, 
    ):
        self.clientes = []
        self.comienzo_tiempo_ocioso = 0
        self.cantidad_total_clientes = 0
        self.tiempo_proxima_salida = 0
        self.sumatoria_tiempo_ocioso = 0
        self.sumatoria_tiempo_permanencia = 0 
        self.sumatoria_tiempo_atencion = 0

    def recibir_cliente(self, cliente):
        self.clientes.append(cliente)
        self.cantidad_total_clientes += 1
        self.acumular_tiempo_atencion(cliente)

    def finalizar_atencion(self):
        if self.clientes:
            cliente = self.clientes.pop(0)
            self.calcular_proxima_salida()
            return cliente
    
    def calcular_proxima_salida(self):
        if self.clientes:
            cliente = self.clientes[0]
            self.tiempo_proxima_salida = cliente.tiempo_llegada + cliente.tiempo_atencion
        else:
            self.tiempo_proxima_salida = float("inf")
        
    def tratar_arrepentimiento(self):
        #arranca el 1 pq se saltea el primero que está siendo atendido
        for cliente in self.clientes[1:]:
            i = self.clientes.index(cliente)
            clientes_adelante = self.clientes[i - 1]
            #La hora de espera se define al momento de entrar al subsistema y 
            # es el tiempo de atención restante del cliente que está siendo atendido
            # mas la sumatoria de de los tiempos de atención de las personas que están
            # adelante en la fila
                   
        
    def acumular_tiempo_ocioso(self, sistema: Sistema):
        self.sumatoria_tiempo_ocioso += sistema.tiempo - self.comienzo_tiempo_ocioso

    def acumular_tiempo_atencion(self, cliente: Cliente):
        self.sumatoria_tiempo_atencion += cliente.tiempo_atencion
        
    def acumular_tiempo_permanencia(self, sistema: Sistema):
        self.sumatoria_tiempo_permanencia += (sistema.tiempo_proxima_llegada - sistema.tiempo) * len(self.clientes)
        
    
 

        
        
        

    
        
    
            