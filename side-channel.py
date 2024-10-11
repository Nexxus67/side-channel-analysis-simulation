import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import os

plt.rcParams['text.color'] = 'lime'
plt.rcParams['axes.labelcolor'] = 'lime'
plt.rcParams['xtick.color'] = 'lime'
plt.rcParams['ytick.color'] = 'lime'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.facecolor'] = 'black'

ascii_art = r"""
__________        .__          ________  ________
\______   \_____  |  |   ____  \_____  \ \_____  \
 |    |  _/\__  \ |  |  /  _ \  /  ____/   _(__  <
 |    |   \ / __ \|  |_(  <_> )/       \  /       \
 |______  /(____  /____/\____/ \_______ \/______  /
        \/      \/                      \/      \/

Análisis de datos cifrados usando números complejos
-------------------------------------------------------------
Este script genera datos simulados de consumo de energía o tiempo de respuesta durante
operaciones criptográficas. Convierte estos datos en el plano complejo para buscar
patrones ocultos que podrían revelar debilidades en esquemas de cifrado.
"""

def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_art)
    print("Descripción del script:\n")
    print("Este programa simula datos de cifrado y analiza patrones en el plano complejo.\n")
    input("Presiona Enter para continuar...")

def get_data_type():
    print("\nSelecciona el tipo de datos a simular:")
    print("1. Consumo de Energía")
    print("2. Tiempos de Respuesta")
    print("3. Variaciones Aleatorias")
    print("4. Ataque de Canal Lateral")
    choice = input("Ingrese su elección (1/2/3/4): ")
    return int(choice)

def get_parameters():
    n_samples = int(input("Ingrese el número de muestras (ej. 1024): ") or 1024)
    noise_level = float(input("Ingrese el nivel de ruido (ej. 0.1): ") or 0.1)
    return n_samples, noise_level

def generate_data(n_samples, data_type, noise_level):
    if data_type == 1:
        return np.abs(np.cos(np.linspace(0, 4 * np.pi, n_samples)) + np.random.normal(0, noise_level, n_samples))
    elif data_type == 2:
        return np.abs(np.sin(np.linspace(0, 4 * np.pi, n_samples)) + np.random.normal(0, noise_level, n_samples))
    elif data_type == 3:
        return np.random.normal(0, noise_level, n_samples)
    elif data_type == 4:
        return np.abs(np.sin(np.linspace(0, 4 * np.pi, n_samples)) * np.cos(np.linspace(0, 2 * np.pi, n_samples)) + np.random.normal(0, noise_level, n_samples))
    else:
        print("Selección no válida, usando variaciones aleatorias por defecto.")
        return np.random.normal(0, noise_level, n_samples)

def plot_complex_plane(amplitude, phase):
    plt.subplot(1, 2, 1)
    plt.plot(amplitude, phase, 'o', markersize=2, color='cyan')
    plt.title("Plano Complejo de Amplitud vs Fase")
    plt.xlabel("Amplitud")
    plt.ylabel("Fase")
    plt.grid(True)

def plot_frequency_spectrum(frequencies, magnitude):
    plt.subplot(1, 2, 2)
    plt.plot(frequencies, magnitude, label='Datos de Frecuencia', color='magenta', linestyle='--')
    plt.axhline(y=np.mean(magnitude), color='red', linestyle='--', label='Media')
    plt.title("Espectro de Frecuencias")
    plt.xlabel("Frecuencia")
    plt.ylabel("Magnitud")
    plt.legend()
    plt.xlim(-0.5, 0.5)

def analyze_data(data):
    print("Estadísticas de los datos:")
    print(f"Media: {np.mean(data)}")
    print(f"Desviación estándar: {np.std(data)}")
    print(f"Máximo: {np.max(data)}")
    print(f"Mínimo: {np.min(data)}")

def main():
    show_intro()
    while True:
        data_type = get_data_type()
        n_samples, noise_level = get_parameters()
        time_series = generate_data(n_samples, data_type, noise_level)

        amplitude = np.abs(time_series)
        phase = np.angle(fft(time_series))
        complex_data = amplitude * np.exp(1j * phase)

        freq_data = fft(complex_data)
        frequencies = np.fft.fftfreq(len(freq_data))
        magnitude = np.abs(freq_data)

        plt.figure(figsize=(12, 6))
        plot_complex_plane(amplitude, phase)
        plot_frequency_spectrum(frequencies, magnitude)

        plt.tight_layout()
        plt.show(block=False)  # Mantiene el gráfico abierto
        plt.pause(1)

        analyze_data(time_series)

        if input("¿Deseas realizar otra simulación? (s/n): ").lower() != 's':
            break
        plt.clf()

if __name__ == "__main__":
    main()
