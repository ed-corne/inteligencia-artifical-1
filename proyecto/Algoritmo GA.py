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

# Función de creación de la población inicial
def initialize_population(population_size, num_dimensions, bounds):
    return np.random.rand(population_size, num_dimensions) * \
           (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]

# Función de evaluación de la aptitud (fitness)
def evaluate_fitness(population, objective_func):
    return np.array([objective_func(individual) for individual in population])

# Operador de selección: Ruleta
def selection_roulette(population, fitness):
    probabilities = fitness / sum(fitness)
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]

# Operador de cruzamiento (crossover): Punto de corte
def crossover_single_point(parents):
    crossover_point = np.random.randint(1, len(parents[0]))
    children = np.concatenate([parents[:, :crossover_point], parents[:, crossover_point:]], axis=1)
    return children

# Operador de mutación: Mutación gaussiana
def mutate_gaussian(children, mutation_rate, mutation_std):
    mutation_mask = np.random.rand(*children.shape) < mutation_rate
    mutations = np.random.normal(0, mutation_std, size=children.shape)
    children = children + mutation_mask * mutations
    return children

# Implementación del algoritmo genético con registro de valores
def genetic_algorithm_with_plot(objective_func, population_size, num_dimensions, max_generations, bounds, nameAlgorithm, graficate):
    population = initialize_population(population_size, num_dimensions, bounds)

    # Lista para almacenar los mejores valores de la función objetivo en cada generación
    best_fitness_values = []

    for generation in range(max_generations):
        fitness = evaluate_fitness(population, objective_func)
        best_index = np.argmin(fitness)
        best_individual = population[best_index]
        best_fitness = fitness[best_index]

        # Almacena el mejor valor de la generación actual
        best_fitness_values.append(best_fitness)
        print(f"Generation {generation + 1}/{max_generations}: Best Fitness = {best_fitness}")

        # Selección de padres
        parents = selection_roulette(population, fitness)

        # Cruzamiento
        children = crossover_single_point(parents)

        # Mutación
        mutation_rate = 0.1
        mutation_std = 0.1
        children = mutate_gaussian(children, mutation_rate, mutation_std)

        # Reemplazo de la población
        population[:-1] = children[:population_size-1]
        population[-1] = best_individual  # Elitismo: se conserva el mejor individuo

    # Graficar la evolución de los mejores valores de la función objetivo
    if(graficate):
        plt.plot(range(1, max_generations + 1), best_fitness_values)
        plt.title('Genetic Algorithm para ' + nameAlgorithm)
        plt.xlabel('Generación')
        plt.ylabel('Mejor Fitness')
        plt.show()

    return best_individual, best_fitness

# Parámetros del GA
population_size = 30
num_dimensions = 2
max_generations = 50
bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])  # Límites para las dos dimensiones

# Ejecución del GA para la función de Rosenbrock con gráfico
print("\nGenetic Algorithm para Rosenbrock:")
best_individual_rosenbrock, best_fitness_rosenbrock = genetic_algorithm_with_plot(rosenbrock, population_size, num_dimensions, max_generations, bounds, 'rosenbrock', True)
print(f"\nBest Individual: {best_individual_rosenbrock}")
print(f"Best Fitness: {best_fitness_rosenbrock}")

# Ejecución del GA para la función de Ackley con gráfico
print("\nGenetic Algorithm para Ackley:")
best_individual_ackley, best_fitness_ackley = genetic_algorithm_with_plot(ackley, population_size, num_dimensions, max_generations, bounds, 'ackley', True)
print(f"\nBest Individual: {best_individual_ackley}")
print(f"Best Fitness: {best_fitness_ackley}")

#ejecutar 20 veses

# Parámetros comunes
num_executions = 20
best_values_rosenbrock = np.zeros(num_executions)
best_values_ackley = np.zeros(num_executions)

# Ejecuciones para Rosenbrock
for i in range(num_executions):
    best_solution_rosenbrock, best_value_rosenbrock = genetic_algorithm_with_plot(rosenbrock, population_size, num_dimensions, max_generations, bounds, 'rosenbrock', False)
    best_values_rosenbrock[i] = best_value_rosenbrock

# Ejecuciones para Ackley
for i in range(num_executions):
    best_solution_ackley, best_value_ackley = genetic_algorithm_with_plot(ackley, population_size, num_dimensions, max_generations, bounds, 'ackley', False)
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