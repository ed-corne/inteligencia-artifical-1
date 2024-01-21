# Practica 2 Puzzle búsqueda en profundidad y profundidad iterativa
# Integrantes: Cornejo Chavez Edwin Joel
            #  Veloz Alcaraz Axel Abraham
            #  Espinoza Sucilla Samuel
from collections import deque
import random

# Estado objetivo
estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def generar_estado_inicial():
    fichas = list(range(1, 9)) + [0]
    random.shuffle(fichas)
    return fichas

# Función para verificar si dos estados son iguales
def son_iguales(estado1, estado2):
    return estado1 == estado2

# Función para mover una ficha en el estado
def mover_ficha(estado, direccion):
    nuevo_estado = estado[:]
    espacio_vacio = nuevo_estado.index(0)
    if direccion == 'arriba' and espacio_vacio > 2:
        nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 3] = nuevo_estado[espacio_vacio - 3], nuevo_estado[espacio_vacio]
    elif direccion == 'abajo' and espacio_vacio < 6:
        nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 3] = nuevo_estado[espacio_vacio + 3], nuevo_estado[espacio_vacio]
    elif direccion == 'izquierda' and espacio_vacio % 3 > 0:
        nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 1] = nuevo_estado[espacio_vacio - 1], nuevo_estado[espacio_vacio]
    elif direccion == 'derecha' and espacio_vacio % 3 < 2:
        nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 1] = nuevo_estado[espacio_vacio + 1], nuevo_estado[espacio_vacio]
    return nuevo_estado

# Función para resolver el 8-puzzle utilizando búsqueda en profundidad (DFS)
def dfs(estado_actual, estado_objetivo, profundidad_maxima):
    if profundidad_maxima < 0:
        return None
    if son_iguales(estado_actual, estado_objetivo):
        return [estado_actual]

    for direccion in ['arriba', 'abajo', 'izquierda', 'derecha']:
        nuevo_estado = mover_ficha(estado_actual, direccion)
        resultado = dfs(nuevo_estado, estado_objetivo, profundidad_maxima - 1)
        if resultado:
            return [estado_actual] + resultado

# Función para resolver el 8-puzzle utilizando búsqueda en profundidad iterativa (IDDFS)
def iddfs(estado_inicial, estado_objetivo):
    profundidad_maxima = 0
    while True:
        resultado = dfs(estado_inicial, estado_objetivo, profundidad_maxima)
        if resultado:
            return resultado
        profundidad_maxima += 1

# Generar estado inicial aleatorio
estado_inicial = generar_estado_inicial()

print("Estado inicial:")
for i in range(0, 9, 3):
    print(estado_inicial[i:i+3])

solucion = iddfs(estado_inicial, estado_objetivo)

if solucion:
    print("\nSolución encontrada:")
    for i in range(0, 9, 3):
        print(solucion[i:i+3])
else:
    print("\nNo se encontró solución.")

