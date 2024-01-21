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

# Implementación del algoritmo de Evolución Diferencial (DE) con registro de valores
def differential_evolution_with_plot(nameAlgorithm, graficate, objective_func, population_size, num_dimensions, bounds, max_iterations, differential_weight=0.8, crossover_prob=0.7):
    # Inicialización de la población
    population = np.random.rand(population_size, num_dimensions) * (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]

    # Lista para almacenar los mejores valores de la función objetivo en cada iteración
    best_values = []

    for iteration in range(max_iterations):
        for i in range(population_size):
            # Selección de tres individuos distintos
            candidates = [idx for idx in range(population_size) if idx != i]
            a, b, c = np.random.choice(candidates, 3, replace=False)

            # Mutación
            mutant_vector = population[a] + differential_weight * (population[b] - population[c])

            # Cruzamiento
            crossover_mask = np.random.rand(num_dimensions) < crossover_prob
            trial_vector = np.where(crossover_mask, mutant_vector, population[i])

            # Evaluación de la función objetivo
            target_value = objective_func(population[i])
            trial_value = objective_func(trial_vector)

            # Selección
            if trial_value < target_value:
                population[i] = trial_vector

        # Almacena el mejor valor de la iteración actual
        best_index = np.argmin([objective_func(individual) for individual in population])
        best_value = objective_func(population[best_index])
        best_values.append(best_value)
        print(f"Iteration {iteration + 1}/{max_iterations}: Best Value = {best_value}")
    if(graficate):
        # Graficar la evolución de los mejores valores de la función objetivo
        plt.plot(range(1, max_iterations + 1), best_values)
        plt.title('Differential Evolution para ' + nameAlgorithm)
        plt.xlabel('Iteración')
        plt.ylabel('Mejor Valor')
        plt.show()

    # Encontrar la mejor solución después de todas las iteraciones
    best_index = np.argmin([objective_func(individual) for individual in population])
    best_solution = population[best_index]
    best_value = objective_func(best_solution)

    return best_solution, best_value

# Parámetros del DE
population_size = 30
num_dimensions = 2
max_iterations = 50
bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])  # Límites para las dos dimensiones

# Ejecución del DE para la función de Rosenbrock con gráfico
print("\nDifferential Evolution para Rosenbrock:")
best_solution_rosenbrock, best_value_rosenbrock = differential_evolution_with_plot('rosenbrock',True, rosenbrock, population_size, num_dimensions, bounds, max_iterations)
print(f"\nBest Solution: {best_solution_rosenbrock}")
print(f"Best Value: {best_value_rosenbrock}")

# Ejecución del DE para la función de Ackley con gráfico
print("\nDifferential Evolution para Ackley:")
best_solution_ackley, best_value_ackley = differential_evolution_with_plot('ackley', True, ackley, population_size, num_dimensions, bounds, max_iterations)
print(f"\nBest Solution: {best_solution_ackley}")
print(f"Best Value: {best_value_ackley}")

#Ejecutar 20 veses 

# Parámetros comunes
num_executions = 20
best_values_rosenbrock = np.zeros(num_executions)
best_values_ackley = np.zeros(num_executions)

# Ejecuciones para Rosenbrock
for i in range(num_executions):
    best_solution_rosenbrock, best_value_rosenbrock = differential_evolution_with_plot('rosenbrock', False, rosenbrock, population_size, num_dimensions, bounds, max_iterations)
    best_values_rosenbrock[i] = best_value_rosenbrock

# Ejecuciones para Ackley
for i in range(num_executions):
    best_solution_ackley, best_value_ackley = differential_evolution_with_plot('ackley', False, ackley, population_size, num_dimensions, bounds, max_iterations)
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

