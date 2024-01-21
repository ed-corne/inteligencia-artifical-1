# Practica 2- Puzzle búsqueda en amplitud 
# Integrantes: Cornejo Chavez Edwin Joel
            #  Veloz Alcaraz Axel Abraham
            #  Espinoza Sucilla Samuel

from collections import deque
import random

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

# Función para generar un estado inicial aleatorio
def generar_estado_inicial():
    fichas = list(range(1, 9)) + [0]
    random.shuffle(fichas)
    return fichas

# Función para resolver el 8-puzzle utilizando búsqueda en amplitud
def resolver_puzzle(estado_inicial, estado_objetivo):
    frontera = deque()
    visitados = set()

    frontera.append(estado_inicial)
    visitados.add(tuple(estado_inicial))

    while frontera:
        estado_actual = frontera.popleft()

        if son_iguales(estado_actual, estado_objetivo):
            return estado_actual

        for direccion in ['arriba', 'abajo', 'izquierda', 'derecha']:
            nuevo_estado = mover_ficha(estado_actual, direccion)
            if tuple(nuevo_estado) not in visitados:
                frontera.append(nuevo_estado)
                visitados.add(tuple(nuevo_estado))

# Estado objetivo
estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Generar estado inicial aleatorio
estado_inicial = generar_estado_inicial()

print("Estado inicial:")
for i in range(0, 9, 3):
    print(estado_inicial[i:i+3])

solucion = resolver_puzzle(estado_inicial, estado_objetivo)

if solucion:
    print("\nSolución encontrada:")
    for i in range(0, 9, 3):
        print(solucion[i:i+3])
else:
    print("\nNo se encontró solución.")
