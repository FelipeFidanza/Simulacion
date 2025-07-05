import csv

class LectorCSV:
    def __init__(self, archivo_csv):
        self.intervalos_arribo = []
        self.tiempos_atencion = []
        self._leer_csv(archivo_csv)
        self.indice_actual = 0

    def _leer_csv(self, archivo_csv):
        with open(archivo_csv, newline='') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                if fila:  # Para evitar filas vacías
                    self.intervalos_arribo.append(float(fila[0]))
                    self.tiempos_atencion.append(float(fila[1]))                    


    def obtener_siguiente(self):
        if self.indice_actual < len(self.intervalos_arribo):
            intervalo = self.intervalos_arribo[self.indice_actual]
            tiempo_atencion = self.tiempos_atencion[self.indice_actual]
            self.indice_actual += 1
            
            return intervalo, tiempo_atencion
        else:
            raise IndexError("No hay más intervalos_arribo disponibles.")
