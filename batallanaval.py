import random

# Constantes
N = 10
CANTIDAD_BARCOS = 10
DISPAROS = 15

# Crear el tablero vacío
tablero = [[0 for _ in range(N)] for _ in range(N)]

# Colocar barcos en posiciones aleatorias sin repetir
posiciones_ocupadas = set()

while len(posiciones_ocupadas) < CANTIDAD_BARCOS:
    fila = random.randint(0, N - 1)
    columna = random.randint(0, N - 1)
    if (fila, columna) not in posiciones_ocupadas:
        posiciones_ocupadas.add((fila, columna))
        tablero[fila][columna] = 1

# Juego: disparos del usuario
aciertos = 0
fallos = 0
disparos_realizados = set()


for intento in range(DISPAROS):
    print(f"\nDisparo {intento + 1} de {DISPAROS}")
    
    # Ingresar coordenadas
    while True:
        try:
            fila = int(input(f"Ingresa la fila (0 a {N-1}): "))
            columna = int(input(f"Ingresa la columna (0 a {N-1}): "))
            if (fila, columna) in disparos_realizados:
                print("Ya disparaste ahí. Probá otra coordenada.")
            elif 0 <= fila < N and 0 <= columna < N:
                break
            else:
                print("Coordenadas fuera del tablero. Probá de nuevo.")
        except ValueError:
            print("Solo se pueden números enteros")

    disparos_realizados.add((fila, columna))

    # Verificamos si acertó
    if tablero[fila][columna] == 1:
        print("Hundido")
        tablero[fila][columna] = "X"  
        aciertos += 1
    else:
        print("Agua")
        tablero[fila][columna] = "-"  
        fallos += 1

# Mostrar resultados
print("Resultados:")
print(f"Aciertos: {aciertos}")
print(f"Fallos: {fallos}\n")


# Mostrar tablero final
print("Tablero final:")
for fila in tablero:
    print(" ".join(str(x) for x in fila))