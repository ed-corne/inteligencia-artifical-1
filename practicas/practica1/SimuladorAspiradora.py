import random
import time

def crear_matriz_aleatoria():
    # Crea una matriz 5x5 con valores aleatorios de 0 y 1
    matriz = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    return matriz

def mostrar_matriz(matriz):
    # Muestra la matriz en la consola
    for fila in matriz:
        print(" ".join(map(str, fila)))

def cambiar_valor(matriz, fila, columna):
    # Cambia el valor de una celda de 0 a 1 o de 1 a 1 (la habitación ya está limpia)
    if matriz[fila][columna] == 0:
        matriz[fila][columna] = 1

def contar_unos(matriz):
    # Cuenta la cantidad de unos en la matriz (habitaciones limpias)
    contador = 0
    for fila in matriz:
        contador += fila.count(1)
    return contador

def procesar_matriz(matriz):
    # Recorre la matriz y simula la limpieza de las habitaciones
    for fila in range(5):
        for columna in range(5):
            cambiar_valor(matriz, fila, columna)
            print("---------------------------")
            mostrar_matriz(matriz)
            time.sleep(1)  # Pausa de 1 segundo para mostrar cada paso
            contador = contar_unos(matriz)
            print("Cantidad de unos en la matriz:", contador)

def main():
    matriz = crear_matriz_aleatoria()

    print("Matriz inicial:")
    mostrar_matriz(matriz)

    input("Presiona Enter para comenzar el proceso automático...")
    procesar_matriz(matriz)

    print("Matriz final:")
    mostrar_matriz(matriz)

    contador = contar_unos(matriz)
    print("Cantidad de unos en la matriz:", contador)

if __name__ == "__main__":
    main()
