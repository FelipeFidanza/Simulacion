from models.Simulacion import Simulacion
from models.LectorCSV import LectorCSV
import os
import sys

def get_resource_path(relative_path):
    """Obtiene la ruta correcta del archivo, tanto en modo desarrollo como en ejecutable"""
    try:
        # PyInstaller crea un directorio temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # En modo desarrollo, usa el directorio actual
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":

    for i in range(5, 0, -1):  
        csv_path = get_resource_path("variables.csv")
        lector = LectorCSV(csv_path)
        sim = Simulacion(cant_corridas=20, cant_servidores=i, lector=lector)
        sim.iniciar_simulacion()

    input()
    