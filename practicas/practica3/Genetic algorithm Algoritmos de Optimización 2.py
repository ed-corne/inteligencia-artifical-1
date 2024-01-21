# Practica 3- Algoritmos de Optimización 2
# Integrantes: Cornejo Chavez Edwin Joel
            #  Veloz Alcaraz Axel Abraham
            #  Espinoza Sucilla Samuel

import numpy as np

# Función de Rosenbrock
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# Función para inicializar la población
def initialize_population(pop_size, chromosome_length):
    return np.random.uniform(-5.0, 5.0, size=(pop_size, chromosome_length))

# Función para evaluar la aptitud (fitness) de cada individuo en la población
def calculate_fitness(population):
    return np.array([1.0 / (1.0 + rosenbrock(ind)) for ind in population])

# Función de selección de padres mediante torneo
def select_parents(population, fitness, num_parents):
    selected_indices = np.random.choice(len(population), size=num_parents, replace=False)
    parents = population[selected_indices]
    return parents

# Función de cruce (crossover)
def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring

# Función de mutación
def mutate(offspring_crossover):
    mutation_rate = 0.01

    for idx in range(offspring_crossover.shape[0]):
        random_value = np.random.random()
        if random_value < mutation_rate:
            random_index = np.random.randint(0, offspring_crossover.shape[1])
            offspring_crossover[idx, random_index] = offspring_crossover[idx, random_index] + np.random.uniform(-0.5, 0.5)

    return offspring_crossover

# Función principal del algoritmo genético
def genetic_algorithm(pop_size, chromosome_length, generations):
    population = initialize_population(pop_size, chromosome_length)

    for generation in range(generations):
        fitness = calculate_fitness(population)

        # Selección de padres
        num_parents = pop_size // 2
        parents = select_parents(population, fitness, num_parents)

        # Creación de la descendencia mediante cruce
        offspring_crossover = crossover(parents, offspring_size=(pop_size - parents.shape[0], chromosome_length))

        # Mutación de la descendencia
        offspring_mutation = mutate(offspring_crossover)

        # Reemplazo de la población anterior con la nueva población
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = offspring_mutation

        # Imprimir el mejor valor en cada generación
        print("Generación {}: Mejor valor de fitness = {}".format(generation, np.max(fitness)))

    # Devolver el mejor individuo al final del proceso
    best_idx = np.argmax(fitness)
    best_individual = population[best_idx]
    return best_individual

# Parámetros del algoritmo genético
pop_size = 100
chromosome_length = 5
generations = 100

# Ejecutar el algoritmo genético
best_solution = genetic_algorithm(pop_size, chromosome_length, generations)

print("\nMejor solución encontrada:")
print("Parámetros:", best_solution)
print("Valor de fitness:", 1.0 / (1.0 + rosenbrock(best_solution)))
