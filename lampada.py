import time
import random


# Simulação dos estados das lâmpadas
def initialize_lights():
    # 0: Desligada, 1: Ligada
    # Atribuir aleatoriamente qual interruptor controla qual lâmpada
    lights = {
        'interruptor_1': random.choice([1, 0]),
        'interruptor_2': random.choice([1, 0]),
        'interruptor_3': random.choice([1, 0])
    }
    return lights


def check_lights(lights, states):
    for interruptor, estado in lights.items():
        states[interruptor] = 'ligada' if estado == 1 else 'desligada'


def simulate_lights(lights, delay=5):
    # Simula o atraso para o primeiro interruptor esquentar a lâmpada
    time.sleep(delay)
    return lights


def identify_lights(lights):
    # Lógica para identificar qual lâmpada está controlada por qual interruptor
    states = {}
    check_lights(lights, states)
    print("Estados das lâmpadas:")
    for interruptor, estado in states.items():
        print(f"{interruptor}: {estado}")

    print("\nSimulando interrupção de um interruptor e acionamento do outro...")
    simulate_lights(lights)
    # Adicione aqui a lógica para simular a detecção dos estados das lâmpadas
    print("Simulação completa. As lâmpadas foram verificadas.")


# Executando a simulação
lights = initialize_lights()
identify_lights(lights)
