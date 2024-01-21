import random
import time

# Función para crear una matriz aleatoria de 5x5 con celdas sucias (0) y limpias (1)
def crear_matriz_aleatoria():
    matriz = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    return matriz

# Función para mostrar la matriz en la consola
def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Función para cambiar el valor de una celda y simular la limpieza
def cambiar_valor(matriz, fila, columna):
    if matriz[fila][columna] == 0:
        print("Aspiradora limpiando en ({}, {})".format(fila, columna))
        matriz[fila][columna] = 1  # Marca como limpio
        mostrar_matriz(matriz)

# Función para sumar los valores de la matriz y verificar si todas las celdas están limpias
def sumar_matriz(matriz):
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    return suma

def puntuacion_agente(numMovimientos):
    return numMovimientos + 1;

# Función principal que simula el movimiento de la aspiradora
def aspiradora(matriz):
    fila2 = 0
    columna2 = 0
    n = 0
    fila = 3
    columna = 3
    numMovimientos = 0
    while n != 25:  # Cambiamos la condición de parada para verificar que todas las celdas se limpien
        nr = random.randint(1, 4)
        if nr == 1:  # Moverse hacian abajo
            fila2 = fila
            fila += 1
            if fila > 4: # Verificar si esta en el limite inferior
                fila = fila2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 2: # Moverse hacia la derecha
            columna2 = columna
            columna += 1
            if columna > 4:  # Verificar si esta en el limite derecho
                columna = columna2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 3: # Moverse hacia la Izquierda
            columna2 = columna
            columna -= 1
            if columna < 0: # Verificar si esta en el limite izquierdo
                columna = columna2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        elif nr == 4: # Moverse hacia arriba 
            fila2 = fila
            fila -= 1
            if fila < 0: # Verificar si esta en el limite superior
                fila = fila2
            else:
                cambiar_valor(matriz, fila, columna)
                time.sleep(1)
        n = sumar_matriz(matriz) # Actualizar el numero de habitaciones limpias
        numMovimientos = puntuacion_agente(numMovimientos)
    return numMovimientos

# Función principal del programa
def main():
    matriz = crear_matriz_aleatoria()

    print("Matriz inicial:")
    mostrar_matriz(matriz)

    input("Presiona Enter para comenzar la limpieza automática...")
    print("Numero de movimientos Totales" , aspiradora(matriz))

    print("Todas las celdas están limpias.")
    mostrar_matriz(matriz)

if __name__ == "__main__":
    main()
