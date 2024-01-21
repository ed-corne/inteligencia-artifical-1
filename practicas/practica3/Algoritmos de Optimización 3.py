import random
import matplotlib.pyplot as plt

# Definir los ingredientes disponibles y sus rangos de cantidad
ingredientes_disponibles = {
    'Harina': (100, 300),
    'Azúcar': (50, 150),
    'Mantequilla': (50, 200),
    'Huevos': (1, 3),
    'Chocolate': (0, 100),
    'Levadura': (1, 10),
}

# Función de aptitud: evalúa qué tan buena es una receta
def aptitud_receta(receta):
    sabor = receta['Azúcar'] + receta['Chocolate']
    textura = receta['Harina'] + receta['Mantequilla'] + receta['Levadura']
    return sabor + textura

# Algoritmo genético
def algoritmo_genetico_mejorado(ingredientes_disponibles, poblacion_tamano, generaciones):
    poblacion = [generar_receta(ingredientes_disponibles) for _ in range(poblacion_tamano)]
    mejores_aptitudes = []

    for generacion in range(generaciones):
        aptitudes = [aptitud_receta(receta) for receta in poblacion]
        mejores_aptitudes.append(max(aptitudes))

        mejores_recetas = [poblacion[i] for i in sorted(range(len(aptitudes)), key=lambda k: aptitudes[k], reverse=True)[:5]]

        poblacion = []
        for _ in range(poblacion_tamano):
            padre1, padre2 = random.sample(mejores_recetas, 2)
            hijo = {}
            for ingrediente in ingredientes_disponibles:
                hijo[ingrediente] = random.choice([padre1[ingrediente], padre2[ingrediente]])
                hijo[ingrediente] += random.uniform(-10, 10)
                hijo[ingrediente] = max(ingredientes_disponibles[ingrediente][0], min(hijo[ingrediente], ingredientes_disponibles[ingrediente][1]))
            poblacion.append(hijo)

        # Introduce nuevos individuos aleatorios para mantener la diversidad
        poblacion.extend([generar_receta(ingredientes_disponibles) for _ in range(poblacion_tamano // 5)])

        mejor_receta = max(poblacion, key=aptitud_receta)
        print(f"Generación {generacion}: {mejor_receta} (Aptitud: {aptitud_receta(mejor_receta)})")

    # Graficar resultados
    plt.plot(range(generaciones), mejores_aptitudes)
    plt.title('Mejor Aptitud por Generación')
    plt.xlabel('Generación')
    plt.ylabel('Aptitud')
    plt.show()

# Función para generar una receta aleatoria
def generar_receta(ingredientes_disponibles):
    return {ingrediente: random.uniform(ingredientes_disponibles[ingrediente][0], ingredientes_disponibles[ingrediente][1]) for ingrediente in ingredientes_disponibles}

# Parámetros del algoritmo genético
poblacion_tamano = 6
generaciones = 100

# Ejecutar el algoritmo genético con gráficos
algoritmo_genetico_mejorado(ingredientes_disponibles, poblacion_tamano, generaciones)