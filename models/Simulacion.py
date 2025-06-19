class Simulacion:
    def __init__(
        self,
        cant_corridas,
    ):
        self.cant_corridas = cant_corridas
    
    def iniciar_corrida(self):
        pass

    def iniciar_simulacion(self):
        for corrida in range(1, self.cant_corridas + 1):
            self.iniciar_corrida()