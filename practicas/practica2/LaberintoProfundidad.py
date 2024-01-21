import queue

# Define el laberinto (matriz 10x10)
laberinto = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

# Función para imprimir el laberinto
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(map(str, fila)))

# Función para moverse por el laberinto utilizando DFS
def moverse_en_laberinto(laberinto, inicio, fin):
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    pila = []
    pila.append(inicio)

    while pila:
        actual = pila.pop()
        if actual == fin:
            return True

        x, y = actual
        for dx, dy in movimientos:
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < len(laberinto) and 0 <= nuevo_y < len(laberinto[0]) and not visitado[nuevo_x][nuevo_y] and laberinto[nuevo_x][nuevo_y] == 0:
                pila.append((nuevo_x, nuevo_y))
                visitado[nuevo_x][nuevo_y] = True
                laberinto[nuevo_x][nuevo_y] = 5  # Movimiento del número 5
                imprimir_laberinto(laberinto)
                print("----------------------------------------------------")
    return False

# Punto de inicio y destino (ajustados a índices válidos)
inicio = (0, 0)
fin = (9, 9)

# Intentamos mover el número 5 desde el inicio al destino
if moverse_en_laberinto(laberinto, inicio, fin):
    print("¡Camino encontrado!")
else:
    print("No se encontró un camino válido.")

# Imprimimos el laberinto final
imprimir_laberinto(laberinto)
