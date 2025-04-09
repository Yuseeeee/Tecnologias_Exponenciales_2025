# Creamos un tablero 10x10 lleno de ceros (o el valor que quieras)
n = 10

tablero = [[0 for _ in range(n)] for _ in range(n)]
cantidad_barcos =   10
disparos = 15
# Mostramos el tablero
import random
columnarandom = random.randint(0,n-1)
filarandom = random.randint(0,n-1)
tablero [columnarandom][filarandom] = 1
for fila in tablero:
    print(" ".join(str(x) for x in fila)) 
print(fila)
print(columnarandom)
print(filarandom)