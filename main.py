from models.Simulacion import Simulacion
from models.LectorCSV import LectorCSV


if __name__ == "__main__":
    lector = LectorCSV("variables.csv")
    sim = Simulacion(cant_corridas=20, cant_servidores=5, lector=lector)
    sim.iniciar_simulacion()
