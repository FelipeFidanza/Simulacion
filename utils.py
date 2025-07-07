import matplotlib.pyplot as plt

def segundos_a_hhmmss(segundos):
    segundos = int(segundos)
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"

def armar_grafico(resultados):
    dias = list(range(1, len(resultados) + 1))
    tiempo_ocioso = []
    for resultado in resultados:
        tiempo_ocioso.append(resultado["corrida"]["Porcentaje de tiempo ocioso"])

    clientes_atendidos = []
    for resultado in resultados:
        clientes_atendidos.append(resultado["corrida"]["Clientes atendidos"])

    fig, ax1 = plt.subplots(figsize=(10,6))

    # Barras para clientes atendidos (eje izquierdo)
    color1 = 'tab:blue'
    ax1.set_xlabel('Día')
    ax1.set_ylabel('Clientes atendidos', color=color1)
    bars = ax1.bar(dias,clientes_atendidos, color=color1, alpha=0.7, label='Clientes atendidos')
    ax1.tick_params(axis='y', labelcolor=color1)

    # Línea para tiempo ocioso (eje derecho)
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('Tiempo ocioso (min)', color=color2)
    line = ax2.plot(dias, tiempo_ocioso, color=color2, marker='o', label='Tiempo ocioso')
    ax2.tick_params(axis='y', labelcolor=color2)

    # Títulos y leyenda
    plt.title('Evolución diaria de clientes atendidos y tiempo ocioso')
    fig.tight_layout()
    plt.show()