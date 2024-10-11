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

Análisis  de datos cifrados usando números complejos
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
    choice = input("Ingrese su elección (1/2/3): ")
    return int(choice)

def generate_data(n_samples, data_type):
    if data_type == 1:
        # Simulación de consumo de energía
        return np.abs(np.cos(np.linspace(0, 4 * np.pi, n_samples)) + np.random.normal(0, 0.1, n_samples))
    elif data_type == 2:
        # Simulación de tiempos de respuesta
        return np.abs(np.sin(np.linspace(0, 4 * np.pi, n_samples)) + np.random.normal(0, 0.1, n_samples))
    elif data_type == 3:
        # Simulación de variaciones aleatorias
        return np.random.normal(0, 1, n_samples)
    else:
        print("Selección no válida, usando variaciones aleatorias por defecto.")
        return np.random.normal(0, 1, n_samples)

show_intro()
data_type = get_data_type()

# Generación y procesamiento de los datos
n_samples = 1024
time_series = generate_data(n_samples, data_type)

# Transformación a números complejos: Amplitud como parte real, derivada como parte imaginaria
amplitude = np.abs(time_series)
phase = np.angle(fft(time_series))
complex_data = amplitude * np.exp(1j * phase)

# Análisis de Fourier para obtener el espectro de frecuencias
freq_data = fft(complex_data)
frequencies = np.fft.fftfreq(len(freq_data))
magnitude = np.abs(freq_data)

# Visualización de los datos en el plano complejo y su espectro de frecuencias
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(amplitude, phase, 'o', markersize=2)
plt.title("Plano Complejo de Amplitud vs Fase")
plt.xlabel("Amplitud")
plt.ylabel("Fase")

plt.subplot(1, 2, 2)
plt.plot(frequencies, magnitude, label='Datos de Frecuencia')
plt.axhline(y=np.mean(magnitude), color='red', linestyle='--', label='Media')
plt.title("Espectro de Frecuencias")
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.legend()

plt.tight_layout()
plt.show()

