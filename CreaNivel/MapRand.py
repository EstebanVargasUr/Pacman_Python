import random
# Crear un laberinto aleatorio en Python3 usando el algoritmo de
# recorrido en profundidad. El propósito de este programa es mostrar las
# características del lenguaje.
# 
# Autor: Mario Abarca
# Fecha: 2017/09/07

from random import shuffle, randint     # Números pseudoaleatorios
from itertools import product           # Producto cartesiano

niveles = list()

def laberinto(m, n):
    def vecinos(i, j):                  # Conjunto de celdas aledañas a (i, j)
        if 0 < i: yield i - 1, j
        if i < m - 1: yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < n - 1: yield i, j + 1

    def visitar(i, j):                  # Alg. de recorrido en profundidad:
        X.add((i, j))                   # Marcar celda actual como visitada
        N = list(vecinos(i, j)); shuffle(N)  # Desordenar celdas vecinas
        for h, k in N:                  # Para cada celda vecina
            if (h, k) in X: continue    # ...que no haya sido visitada:
            A[i + h + 1][j + k + 1] = ' '  # Tumbar el muro que las separa
            visitar(h, k)               # Visitar vecina recursivamente

    A = [['█']*(2*n + 1) for i in range(2*m + 1)]  # Tablero
    for i, j in product(range(1, 2*m + 1, 2), range(1, 2*n + 1, 2)):
        A[i][j] = ' '                   # Poner celdas blancas
    X = set()                           # Conjunto de celdas visitadas
    visitar(randint(0, m - 1), randint(0, n - 1))  # Inicio en celda aleatoria

    caminos = 0
    filaLlena = True
    for i in range(m*2):
        caminos = 0
        filaLlena = True
        for h in range(n*2):
            
            if h+1 != 20 and h+1 != 0 and A[i][h+1] == '█' and A[i][h+2] == ' ' and A[i][h+3] == ' ':
                A[i][h+1] = ' '
                
            caminos = 0
            if A[i][h] == ' ':
                if A[i+1][h] == '█':
                    caminos += 1
                if A[i-1][h] == '█':
                     caminos += 1
                if A[i][h+1] == '█':
                    caminos += 1
                if A[i][h-1] == '█':
                    caminos += 1

                if caminos > 2:
                    if A[i+1][h] == '█' and i+1 != 20 and i+1 != 0:
                        A[i+1][h] = ' '
                    if A[i-1][h] == '█' and i-1 != 20 and i-1 != 0:
                        A[i-1][h] = ' '
                    if A[i][h+1] == '█' and h+1 != 20 and h+1 != 0:
                        A[i][h+1] = ' '
                    if A[i][h-1] == '█' and h-1 != 20 and h-1 != 0:
                        A[i][h-1] = ' '
            if i == 0 or i == 20 or A[i][h] == ' ':
                filaLlena = False
            if filaLlena:
                A[i][1] = ' '
    A[7][6] = ' '
    A[13][6] = ' '
    A[7][14] = ' '
    A[13][14] = ' '

    for i in range(7,14):
        if i != 10:
            A[8][i] = '█'
        else:
            A[8][i] = ' '
        A[7][i] = ' '
    for i in range(7,14):
        A[12][i] = '█'
        A[13][i] = ' '
    for i in range(8,13):
        A[i][7] = '█'
        A[i][6] = ' '
        if A[i][5] == ' ' and A[i][4] == '█':
            A[i][5] = '█'

    for i in range(9,12):
        for j in range(8,13):
            A[i][j] = ' '

    bandera = False
    numero = 0
    while bandera == False:
        numero = random.randint(1, 20) #Toma un numero al azar (1 , 2 o 3) 
        if A[numero][1] == ' ':
            bandera = True

    A[numero][0] = ' '
    A[numero][20] = ' '

    for i in range(m*2):
        for h in range(n*2):
            A[i][20-h] = A[i][h]

    niveles.append(A)
    return A