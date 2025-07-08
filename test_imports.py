#!/usr/bin/env python3
"""
Script de prueba para verificar que todos los imports funcionan correctamente
"""

print("Iniciando test de imports...")

try:
    print("1. Importando models.Simulacion...")
    from models.Simulacion import Simulacion
    print("   ✓ models.Simulacion importado correctamente")
    
    print("2. Importando models.LectorCSV...")
    from models.LectorCSV import LectorCSV
    print("   ✓ models.LectorCSV importado correctamente")
    
    print("3. Verificando archivo variables.csv...")
    import os
    if os.path.exists("variables.csv"):
        print("   ✓ variables.csv encontrado")
    else:
        print("   ✗ variables.csv NO encontrado")
    
    print("4. Probando creación de objetos...")
    lector = LectorCSV("variables.csv")
    print("   ✓ LectorCSV creado correctamente")
    
    sim = Simulacion(cant_corridas=1, cant_servidores=1, lector=lector)
    print("   ✓ Simulacion creada correctamente")
    
    print("\n¡Todos los tests pasaron exitosamente!")
    
except Exception as e:
    print(f"\n✗ Error encontrado: {e}")
    import traceback
    traceback.print_exc()

print("\nPresiona Enter para cerrar...")
input()
