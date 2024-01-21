# Proyecto Final Busqueda con Información
# Integrantes: Cornejo Chavez Edwin Joel
            #  Veloz Alcaraz Axel Abraham
            #  Espinoza Sucilla Samuel
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de Rosenbrock
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# Definición de la función de Ackley
def ackley(x):
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt((1/n) * sum(x**2))) - \
           np.exp((1/n) * sum(np.cos(2 * np.pi * x))) + 20 + np.exp(1)

# Implementación del algoritmo PSO con registro de valores
def pso_with_plot(objective_func, num_particles, num_dimensions, max_iterations, bounds, nameAlgorithm, graficate):
    # Inicialización de partículas
    particles_position = np.random.rand(num_particles, num_dimensions) * \
                         (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]
    particles_velocity = np.random.rand(num_particles, num_dimensions)

    # Mejores posiciones personales y globales
    pbest_position = particles_position.copy()
    gbest_position = particles_position[np.argmin([objective_func(p) for p in particles_position])]

    # Mejores valores personales y globales
    pbest_value = [objective_func(p) for p in particles_position]
    gbest_value = min(pbest_value)

    # Parámetros del PSO
    w = 0.5  # Peso inercial
    c1 = 1.5  # Coeficiente de aceleración personal
    c2 = 1.5  # Coeficiente de aceleración global

    # Lista para almacenar los valores de la función objetivo en cada iteración
    objective_values = []

    # Iteraciones del PSO
    for iteration in range(max_iterations):
        for i in range(num_particles):
            # Actualización de velocidad y posición
            r1, r2 = np.random.rand(2)
            particles_velocity[i] = w * particles_velocity[i] + \
                                     c1 * r1 * (pbest_position[i] - particles_position[i]) + \
                                     c2 * r2 * (gbest_position - particles_position[i])
            particles_position[i] += particles_velocity[i]

            # Límites de las partículas
            particles_position[i] = np.clip(particles_position[i], bounds[:, 0], bounds[:, 1])

            # Actualización de pbest y gbest
            current_value = objective_func(particles_position[i])
            if current_value < pbest_value[i]:
                pbest_value[i] = current_value
                pbest_position[i] = particles_position[i]

            if current_value < gbest_value:
                gbest_value = current_value
                gbest_position = particles_position[i]

        # Almacena el mejor valor de la iteración actual
        objective_values.append(gbest_value)
        print(f"Iteration {iteration + 1}/{max_iterations}: Best Value = {gbest_value}")

    # Graficar la evolución de los valores de la función objetivo
    if(graficate):
        plt.plot(range(1, max_iterations + 1), objective_values)
        plt.title('PSO para ' + nameAlgorithm)
        plt.xlabel('Iteración')
        plt.ylabel('Valor de la Función Objetivo')
        plt.show()

    return gbest_position, gbest_value

# Parámetros del PSO
num_particles = 30
num_dimensions = 2
max_iterations = 50
bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])  # Límites para las dos dimensiones

# Ejecución del PSO para la función de Rosenbrock con gráfico
print("\nPSO para Rosenbrock:")
best_position_rosenbrock, best_value_rosenbrock = pso_with_plot(rosenbrock, num_particles, num_dimensions, max_iterations, bounds, 'rosenbrock', True)
print(f"\nBest Position: {best_position_rosenbrock}")
print(f"Best Value: {best_value_rosenbrock}")

# Ejecución del PSO para la función de Ackley con gráfico
print("\nPSO para Ackley:")
best_position_ackley, best_value_ackley = pso_with_plot(ackley, num_particles, num_dimensions, max_iterations, bounds, 'ackley', True)
print(f"\nBest Position: {best_position_ackley}")
print(f"Best Value: {best_value_ackley}")


#ejecutar 20 veses

# Parámetros comunes
num_executions = 20
best_values_rosenbrock = np.zeros(num_executions)
best_values_ackley = np.zeros(num_executions)

# Ejecuciones para Rosenbrock
for i in range(num_executions):
    best_solution_rosenbrock, best_value_rosenbrock = pso_with_plot(rosenbrock, num_particles, num_dimensions, max_iterations, bounds, 'rosenbrock', False)
    best_values_rosenbrock[i] = best_value_rosenbrock

# Ejecuciones para Ackley
for i in range(num_executions):
    best_solution_ackley, best_value_ackley = pso_with_plot(ackley, num_particles, num_dimensions, max_iterations, bounds, 'ackley', False)
    best_values_ackley[i] = best_value_ackley

# Cálculo del promedio y la desviación estándar para Rosenbrock
average_rosenbrock = np.mean(best_values_rosenbrock)
std_dev_rosenbrock = np.std(best_values_rosenbrock)

# Cálculo del promedio y la desviación estándar para Ackley
average_ackley = np.mean(best_values_ackley)
std_dev_ackley = np.std(best_values_ackley)

# Encontrar el índice del mejor resultado para Rosenbrock
best_index_rosenbrock = np.argmin(best_values_rosenbrock)
best_value_rosenbrock = best_values_rosenbrock[best_index_rosenbrock]
# Encontrar el índice del mejor resultado para Ackley
best_index_ackley = np.argmin(best_values_ackley)
best_value_ackley = best_values_ackley[best_index_ackley]

# Resultados
print('\nResultados despues de Ejecutar  20 veces\n')
print(f"\nMejor Resultado para Rosenbrock - Iteración {best_index_rosenbrock + 1}/{num_executions}: {best_value_rosenbrock}")
print(f"Rosenbrock - Promedio: {average_rosenbrock}, Desviación Estándar: {std_dev_rosenbrock}")
print(f"\nMejor Resultado para Ackley - Iteración {best_index_ackley + 1}/{num_executions}: {best_value_ackley}")
print(f"Ackley - Promedio: {average_ackley}, Desviación Estándar: {std_dev_ackley}")