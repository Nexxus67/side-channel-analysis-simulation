# 🔮 Análisis  de Datos Cifrados 🔐

 Este script convierte datos en el plano complejo para analizar sus características y posibles vulnerabilidades en esquemas de cifrado. 

## 📜 Descripción del Proyecto

Este script genera datos simulados relacionados con procesos criptográficos y los analiza en el plano complejo, permitiendo:
- 📊 Convertir datos en números complejos para detectar patrones inusuales.
- 🧩 Realizar una Transformada de Fourier para obtener el espectro de frecuencias.
- 🔍 Visualizar relaciones entre amplitud y fase, y analizar el impacto en el cifrado.

### 🎥 Ejemplo de Visualización

![Plano Complejo y espectro de frecuencia](https://i.imgur.com/576OkKA.png) 


### Interpretación de los Gráficos

1. **Plano Complejo de Amplitud vs Fase**
   - **Ejes**:
     - **Eje X (Amplitud)**: Representa la magnitud de los datos simulados. Valores más altos indican mayor amplitud.
     - **Eje Y (Fase)**: Representa la fase de las señales, lo que puede ayudar a entender la posición en el ciclo de la onda.
   - **Interpretación**:
     - Los puntos en el gráfico indican la relación entre la amplitud y la fase de las señales simuladas.
     - Si observas un patrón o agrupaciones de puntos, esto puede indicar correlaciones o comportamientos similares entre diferentes muestras de datos.
     - La dispersión de puntos puede mostrar variabilidad en los datos, que podría ser relevante para el análisis de patrones ocultos en datos cifrados.

2. **Espectro de Frecuencias**
   - **Ejes**:
     - **Eje X (Frecuencia)**: Representa las frecuencias de las señales en el dominio de Fourier. Puede incluir valores negativos y positivos debido a la naturaleza de la transformada de Fourier.
     - **Eje Y (Magnitud)**: Muestra la amplitud de cada frecuencia. Valores más altos indican componentes de frecuencia más fuertes en la señal.
   - **Interpretación**:
     - Las picos en el gráfico indican frecuencias dominantes en los datos. Un pico alto sugiere que esa frecuencia tiene un impacto significativo en la señal.
     - La forma del espectro puede revelar características sobre los datos. Por ejemplo, un espectro con muchos picos puede indicar ruido o variabilidad, mientras que uno con picos bien definidos puede sugerir señales más estables o predecibles.
     - Observando las frecuencias que tienen mayor magnitud, se puede inferir sobre patrones en los datos y potencialmente identificar debilidades en esquemas de cifrado si ciertas frecuencias son anómalas.


## 🚀 Comenzando

### Requisitos

- Python 3.x
- Librerías: `numpy`, `matplotlib`, `scipy`

Para instalarlas, ejecuta:

```bash
pip install numpy matplotlib scipy
```

### Ejecución del Script

1. Clona el repositorio:

    ```bash
    git clone [https://github.com/tu_usuario/nombre_del_repositorio.git](https://github.com/Nexxus67/side-channel-analysis-simulation)
    cd side-channel-analysis-simulation
    ```

2. Ejecuta el script:

    ```bash
    python side-channel-simulation.py
    ```

### Selección de Datos Simulados

Al ejecutar el script, se te pedirá que elijas el tipo de datos a simular:
1. Consumo de Energía
2. Tiempos de Respuesta
3. Variaciones Aleatorias

## 🧠 Filosofía y Objetivo

El objetivo es explorar nuevas fronteras en la seguridad informática a través de las matemáticas complejas. Este proyecto se enfoca en analizar posibles puntos débiles en cifrados usando transformaciones complejas y análisis de frecuencia.

## 📬 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script o deseas añadir nuevas funcionalidades, mandá PR.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

