

class Sistema:
    def __init__(
        self, 
        subsistemas,
        cant_subsistemas,
        mu,
        lamda,
        tiempo_final = 14400,
        tiempo_proxima_llegada = 0,
        intervalo_entre_arribos = 0,
        tiempo_arrepentimiento = 300,
        cant_arrepentidos = 0,
        tiempo = 0
    ):
        self.subsistemas = subsistemas
        self.mu = tiempo_final * cant_subsistemas / 300
        self.lamda = 300 / tiempo_final
        
    def generar_ia(self):
        pass
    
    def buscar_cola_mas_corta(self):
        pass
        
    def llegada(self):
       pass 
       
    def salida(self):
        pass
        
    def verificar_tiempo(self):
        pass
        
class Subsistema:
    def __init__(
        self, 
        clientes= [], 
        cantidad_total_clientes = 0,
        tiempo_proxima_salida = 0, 
        comienzo_tiempo_ocioso = 0,
        sumatoria_tiempo_ocioso = 0, 
        sumatoria_tiempo_permanencia = 0, 
        sumatoria_tiempo_atencion = 0,
        activo = False,
    ):
        pass
        
    def incrementar_total_clientes(self):
        self.cantidad_total_clientes += 1
        
    def incrementar_tiempo_de_espera(self):
        pass
        
    def verificar_arrepentidos(self):
        pass
        
    def acumular_tiempo_ocioso(self):
        pass
        
    def acumular_tiempo_atencion(self):
        pass
        
    def acumular_tiempo_permanencia(self):
        pass
        
    def unica_persona(self) -> bool:
        return False
        
        
        
class Cliente:
    def __init__(
        self, 
        tiempo_espera = 0,
        tiempo_atencion = 0,
        arrepentido = False
    ):
        pass
        
    def generar_tiempo_atencion(self, lamda):
        #logica para generar tiempo de atención
        nuevo_tiempo_atencion = 0
        self.tiempo_atencion = nuevo_tiempo_atencion
    
    
        
    
            