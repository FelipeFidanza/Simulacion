from models.Simulacion import Simulacion
from models.LectorCSV import LectorCSV

if __name__ == "__main__":

    for i in range(5, 0, -1):
        lector = LectorCSV("variables.csv")
        sim = Simulacion(cant_corridas=1250, cant_servidores=i, lector=lector)
        sim.iniciar_simulacion()

    input()
