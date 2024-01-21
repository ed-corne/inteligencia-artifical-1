# Practica 1- Simulador Aspiradora
# Integrantes: Cornejo Chavez Edwin Joel
            #  Veloz Alcaraz Axel Abraham
            #  Espinoza Sucilla Samuel

#¿Puede un agente reactivo ser racional bajo las condiciones del problema?
#   La racionalidad de un agente reactivo depende en gran medida del entorno y la adecuacion de sus reglas 
#   de decision a ese entorno. Puede ser racional en ciertas condiciones, pero su falta de capacidad para aprender 
#   y adaptarse a situaciones cambiantes limita su racionalidad en entornos mas complejos.

#¿Puede un agente reactivo ser racional bajo las condiciones del problema?
#   Un agente reactivo con capacidad de memoria limitada puede ser mas racional y eficiente en entornos
#    donde la historia y la memoria de estados pasados son relevantes para la toma de decisiones.


import random
import time

def crear_matriz_aleatoria():
    matriz = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def cambiar_valor(matriz, fila, columna):
    if matriz[fila][columna] == 0:
        print("Aspiradora limpiando en ({}, {})".format(fila, columna))
        matriz[fila][columna] = 1  # Marca como limpio
        mostrar_matriz(matriz)

def sumar_matriz(matriz):
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    return suma       

def sumanr(nr):
    if nr == 5:
        nr = 0
    return nr

# 1 = va hacia abajo la aspiradora, 2 = va hacia la derecha la aspiradora, 3 = va hacia la izquierda la aspiradora, 4 = va hacia arriba la aspiradora

def aspiradora(matriz, puntos):
    fila2 = 0
    columna2 = 0
    n = 0
    nr = 0
    fila = 3
    columna = 3
    #puntos = 50

    while n != puntos:  # Cambiamos la condición de parada
        nr = random.randint(1, 4)
        if nr == 1:
            fila2 = fila
            fila += 1
            if fila > 4:
                fila = fila2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 2:
            columna2 = columna
            columna += 1
            if columna > 4:
                columna = columna2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 3:
            columna2 = columna
            columna -= 1
            if columna < 0:
                columna = columna2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 4:
            fila2 = fila
            fila -= 1
            if fila < 0:
                fila = fila2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        n = n + 1
        print("Pasos: ", n)    


def main():
    matriz = crear_matriz_aleatoria()
    puntos = 50
    print("Iniciamos con ", puntos," puntos")
    print("Matriz inicial:")
    mostrar_matriz(matriz)
    input("Presiona Enter para comenzar la limpieza automática...")

    aspiradora(matriz, puntos)


    if sumar_matriz(matriz) == 25:
        print("Todas las celdas están limpias.")
        mostrar_matriz(matriz)
    else:
        print("Las celdas no se alcanzaron a limpiar todas")
        mostrar_matriz(matriz)

if __name__ == "__main__":
    main()

