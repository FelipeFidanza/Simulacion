class Cliente:
    def __init__(
        self, 
        tiempo_llegada,
        tiempo_atencion,
        tiempo_inicio_atencion=0
    ):
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_atencion = tiempo_atencion
        self.tiempo_inicio_atencion = tiempo_inicio_atencion