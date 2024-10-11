import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import os
import sys

# Configuración de visualización
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
    options = {
        "1": "Consumo de Energía",
        "2": "Tiempos de Respuesta",
        "3": "Variaciones Aleatorias",
        "4": "Ataque de Canal Lateral"
    }
    print("\nSelecciona el tipo de datos a simular:")
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Ingrese su elección (1/2/3/4): ")
    if choice in options:
        return int(choice)
    print("Selección no válida. Inténtelo de nuevo.")
    return get_data_type()

def get_parameters():
    try:
        n_samples = int(input("Ingrese el número de muestras (ej. 1024): ") or 1024)
        noise_level = float(input("Ingrese el nivel de ruido (ej. 0.1): ") or 0.1)
        return n_samples, noise_level
    except ValueError:
        print("Entrada no válida. Intente de nuevo.")
        return get_parameters()

def generate_data(n_samples, data_type, noise_level):
    t = np.linspace(0, 4 * np.pi, n_samples)
    if data_type == 1:
        data = np.abs(np.cos(t) + np.random.normal(0, noise_level, n_samples))
    elif data_type == 2:
        data = np.abs(np.sin(t) + np.random.normal(0, noise_level, n_samples))
    elif data_type == 3:
        data = np.random.normal(0, noise_level, n_samples)
    elif data_type == 4:
        data = np.abs(np.sin(t) * np.cos(t / 2) + np.random.normal(0, noise_level, n_samples))
    return data

def plot_complex_plane(amplitude, phase):
    plt.subplot(1, 2, 1)
    plt.plot(amplitude, phase, 'o', markersize=2, color='cyan')
    plt.title("Plano Complejo de Amplitud vs Fase")
    plt.xlabel("Amplitud")
    plt.ylabel("Fase")
    plt.grid(True)

def plot_frequency_spectrum(frequencies, magnitude):
    plt.subplot(1, 2, 2)
    plt.plot(frequencies, magnitude, color='lime', linestyle='--', label='Datos de Frecuencia')
    plt.axhline(y=np.mean(magnitude), color='yellow', linestyle='-', linewidth=2, label='Media')
    plt.title("Espectro de Frecuencias")
    plt.xlabel("Frecuencia")
    plt.ylabel("Magnitud")
    plt.legend()
    plt.xlim(-0.5, 0.5)

def analyze_data(data):
    print("\nEstadísticas de los datos:")
    print(f"Media: {np.mean(data):.4f}")
    print(f"Desviación estándar: {np.std(data):.4f}")
    print(f"Máximo: {np.max(data):.4f}")
    print(f"Mínimo: {np.min(data):.4f}")

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
        plt.show(block=False)
        plt.pause(1)

        analyze_data(time_series)

        if input("\n¿Deseas realizar otra simulación? (s/n): ").strip().lower() != 's':
            plt.close()
            print("Gracias por usar el programa. Hasta la próxima.")
            break
        plt.clf()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
        sys.exit(0)

