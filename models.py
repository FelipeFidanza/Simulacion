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
    
    def buscar_fila_mas_corta(self):
        #TODO: incializar la variable de tal forma que nunca cambiemos el tipo int -> objeto Subsistema
        subsistema_menor_fila = float("inf")
        for subsistema in self.subsistemas: 
            cantidad_clientes = len(subsistema.clientes)
            if cantidad_clientes > subsistema_menor_fila:
                subsistema_menor_fila = subsistema
        return subsistema_menor_fila
    
    def obtener_proxima_llegada(self):
        intervalo_entre_arribos = self.generar_ia()
        self.tiempo_proxima_llegada = self.tiempo + intervalo_entre_arribos
       
    def obtener_proxima_salida(self):
        subsistema_proxima_salida = float("inf")
        for subsistema in self.subsistemas: 
            proxima_salida = subsistema.tiempo_proxima_salida
            if proxima_salida < subsistema_proxima_salida:
                subsistema_proxima_salida = proxima_salida
        self.tiempo_proxima_salida = subsistema_proxima_salida
    
    def verificar_proximo_evento(self):
        """
        Verifica cuál es el próximo evento a ocurrir en el sistema: una llegada o una salida.
        """
        self.obtener_proxima_llegada()
        self.obtener_proxima_salida()

        return self.tiempo_proxima_llegada <= self.tiempo_proxima_salida
    
    def generar_cliente(self):
        """
        Genera un cliente con un tiempo de llegada y un tiempo de atención.
        El tiempo de llegada es el tiempo actual del sistema y el tiempo de atención es generado aleatoriamente.
        """
        tiempo_llegada = self.tiempo
        tiempo_atencion = self.generar_ta()
        cliente = Cliente(tiempo_llegada, tiempo_atencion)

        fila_a_ingresar = self.buscar_fila_mas_corta()

        fila_a_ingresar.recibir_cliente(cliente)
        
    def verificar_tiempo_final(self):
        return self.tiempo_final <= self.tiempo
        

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
        sistema
    ):
        self.clientes = []
        self.comienzo_tiempo_ocioso = 0
        self.cantidad_total_clientes = 0
        self.tiempo_proxima_salida = 0
        self.sumatoria_tiempo_ocioso = 0
        self.sumatoria_tiempo_permanencia = 0 
        self.sumatoria_tiempo_atencion = 0
        self.sistema = sistema


    def recibir_cliente(self, cliente):
        self.clientes.append(cliente)
        self.cantidad_total_clientes += 1
        self.acumular_tiempo_atencion(cliente)

       # self.tratar_arrepentimiento(cliente)

        if len(self.clientes) == 1:
            self.calcular_proxima_salida()


    def finalizar_atencion(self):
        
        self.clientes = self.clientes[1:]
        if self.clientes:
            self.calcular_proxima_salida()
        else:
            self.comienzo_tiempo_ocioso = self.sistema.tiempo
    
    def calcular_proxima_salida(self):
        if self.clientes:
            cliente = self.clientes[0]
            self.tiempo_proxima_salida = cliente.tiempo_llegada + cliente.tiempo_atencion
        else:
            self.tiempo_proxima_salida = float("inf")
        
    def tratar_arrepentimiento(self, cliente):
        #arranca el 1 pq se saltea el primero que está siendo atendido
        for cliente in self.clientes[1:]:
            i = self.clientes.index(cliente)
            clientes_adelante = self.clientes[i - 1]
            #La hora de espera se define al momento de entrar al subsistema y 
            # es el tiempo de atención restante del cliente que está siendo atendido
            # mas la sumatoria de de los tiempos de atención de las personas que están
            # adelante en la fila
                   
        
    def acumular_tiempo_ocioso(self):
        self.sumatoria_tiempo_ocioso += self.sistema.tiempo - self.comienzo_tiempo_ocioso

    def acumular_tiempo_atencion(self, cliente: Cliente):
        self.sumatoria_tiempo_atencion += cliente.tiempo_atencion
        
    def acumular_tiempo_permanencia(self):
        self.sumatoria_tiempo_permanencia += (self.sistema.tiempo_proxima_llegada - self.sistema.tiempo) * len(self.clientes)
        
    
 

        
        
        

    
        
    
            