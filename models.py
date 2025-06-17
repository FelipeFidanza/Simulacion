from ast import Index
import random
import math

class Sistema:
    def __init__(
        self, 
        subsistemas,
        cant_subsistemas,
        mu,
        lamda,
        tiempo_proxima_llegada = 0,
        tiempo_final = 14400,
        intervalo_entre_arribos = 0,
        tiempo_arrepentimiento = 300,
        cant_arrepentidos = 0,
        tiempo = 0
    ):
        self.subsistemas = subsistemas
        self.mu = tiempo_final * cant_subsistemas / 300
        self.lamda = 300 / tiempo_final
        self.tiempo_proxima_llegada = tiempo_proxima_llegada
        self.tiempo = tiempo
        
    def generar_ia(self):
        U = random.uniform(0, 1)
        return -math.log(U) / self.lamda
    
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
        
class Subsistema:
    def __init__(
        self, 
        clientes = [], 
        cantidad_total_clientes = 0,
        tiempo_proxima_salida = 0, 
        comienzo_tiempo_ocioso = 0,
        sumatoria_tiempo_ocioso = 0, 
        sumatoria_tiempo_permanencia = 0, 
        sumatoria_tiempo_atencion = 0,
        activo = False,
    ):
        self.clientes = clientes
        
    def actualizar_tiempos_espera(self):
        #arranca el 1 pq se saltea el primero que está siendo atendido
        for cliente in self.clientes[1:]:
            i = self.clientes.index(cliente)
            clientes_adelante = self.clientes[i - 1]
            #La hora de espera se define al momento de entrar al subsistema y 
            # es el tiempo de atención restante del cliente que está siendo atendido
            # mas la sumatoria de de los tiempos de atención de las personas que están
            # adelante en la fila
                
            
            
        
    def incrementar_tiempo_de_espera(self):
        pass
        
    def verificar_arrepentidos(self):
        pass
        
    def acumular_tiempo_ocioso(self):
        pass
        
    def acumular_tiempo_atencion(self):
        pass
        
    def acumular_tiempo_permanencia(self, sistema: Sistema):
        self.sumatoria_tiempo_permanencia += (sistema.tiempo_proxima_llegada - sistema.tiempo) * len(self.clientes)
        
        
    def unica_persona(self) -> bool:
        return False
        
        
        
class Cliente:
    def __init__(
        self, 
        tiempo_llegada,
        tiempo_atencion = 0,
        arrepentido = False,
    ):
        self.tiempo_llegada = tiempo_llegada
        
    def generar_tiempo_atencion(self, lamda):
        #logica para generar tiempo de atención
        nuevo_tiempo_atencion = 0
        self.tiempo_atencion = nuevo_tiempo_atencion
    
    
        
    
            