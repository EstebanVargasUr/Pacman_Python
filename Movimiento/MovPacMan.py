from sonidos.ControlSonidos import SonidoMover
import Grafo.Grafo as GR
import CargaImagen.CargaImagen as Imagen
import threading


def Camino(P, u, v):                        #Camino u⤳v dado por Floyd-Warshall
    lista = [v]                             #El camino termina en v
    while v != u:                           #Hasta no llegar a u
        v = P[u, v]                         #…retrocedemos un paso
        lista.append(v)                     
    lista.reverse()                         #Enlistamos el recorrido en reversa
    return lista

def RecorridoFloyd(Grafo,D,P,inicial,destino):
    Recorrido = list()
    for u in Grafo.nodes:
        for v in Grafo.nodes:
            if u != v and D[u, v] < float('inf'):
                lista = Camino(P, v, u)
                if str(lista[len(lista)-1]) == str(inicial) and str(lista[0]) == str(destino):
                    for i in range(len(lista)):
                        #print(lista[i],end=" ")
                        if i+1 <len(lista):
                            Recorrido.append(Grafo.direcciones[(lista[i],lista[i+1])])
                    return Recorrido

def Movimiento(Direccion,Laberinto,x,y):
    
    # print("-----------------------------------")
    # for i in range(21):
    #     for j in range(21):
    #         print(Laberinto[i][j],end="")
    #     print("")
    ThreadClyde = threading.Thread(target=SonidoMover,)
    ThreadClyde.start()    
    if Direccion == "arriba":
        if Laberinto[x-1][y] == ' ' or Laberinto[x-1][y] == ".":
            Laberinto[x-1][y] = '$'
            Laberinto[x][y] = ' '
            return False

        elif Laberinto[x-1][y] == "O": 
            Laberinto[x-1][y] = '$'
            Laberinto[x][y] = ' '
            return True    

    elif Direccion == "abajo":
        if Laberinto[x+1][y] == " " or Laberinto[x+1][y] == ".":
            Laberinto[x+1][y] = '$'
            Laberinto[x][y] = ' '
            return False

        elif Laberinto[x+1][y] == "O": 
            Laberinto[x+1][y] = '$'
            Laberinto[x][y] = ' '
            return True 

    if Direccion == "derecha":
        if Laberinto[x][y+1] == ' ' or Laberinto[x][y+1] == '.':
            Laberinto[x][y+1] = '$'
            Laberinto[x][y] = ' '
            return False

        elif Laberinto[x][y+1] == "O": 
            Laberinto[x][y+1] = '$'
            Laberinto[x][y] = ' '
            return True 

    elif Direccion == "izquierda":
        if Laberinto[x][y-1] == " " or Laberinto[x][y-1] == ".":
            Laberinto[x][y-1] = '$'
            Laberinto[x][y] = ' '
            return False
            
        elif Laberinto[x][y-1] == "O": 
            Laberinto[x][y-1] = '$'
            Laberinto[x][y] = ' '
            return True 
            
    return False

def VerificaMovimiento(Direccion,Laberinto,x,y):
    if Direccion == "arriba":
        if Laberinto[x-1][y] == " " or Laberinto[x-1][y] == "." or Laberinto[x-1][y] == "O":
            return True
        else: return False     
    if Direccion == "abajo":
        if Laberinto[x+1][y] == " " or Laberinto[x+1][y] == "." or Laberinto[x+1][y] == "O":
            return True
        else: return False
    if Direccion == "derecha" and y+1<21:
        if Laberinto[x][y+1] == ' ' or Laberinto[x][y+1] == '.' or Laberinto[x][y+1] == 'O':
            return True
        else: return False
    if Direccion == "izquierda" and y-1>=0:
        if Laberinto[x][y-1] == ' ' or Laberinto[x][y-1] == "." or Laberinto[x][y-1] == "O":
            return True
        else: return False

def MovimientoFantasma(ImagenF,Fantasma,Algoritmo,ContCasillas,Fila,Columna,MatrizV,UltimoVerticePacMan,VerticeFantasma,GrafoNivel,Recorrido,SumaX,SumaY,Direccion,D,P):
    if ContCasillas == 33:    
        if SumaX == 1:
            Columna += 1
        if SumaX == -1:
            Columna-=1
        if SumaY == 1:
            Fila +=1
        if SumaY == -1:
            Fila -=1

        if Fantasma != "Clyde" or Fantasma == "Clyde" and len(Recorrido)==0 or Algoritmo == "Dijsktra":
            if MatrizV[Fila][Columna] !='#' and MatrizV[Fila][Columna] !=' ':
                VerticeFantasma = MatrizV[Fila][Columna]
                Recorrido = DeterminaAlgoritmo(Algoritmo,GrafoNivel,VerticeFantasma,UltimoVerticePacMan,D,P)
        elif MatrizV[Fila][Columna] !='#' and MatrizV[Fila][Columna] !=' ':
            Recorrido.pop(len(Recorrido)-1)
            VerticeFantasma = MatrizV[Fila][Columna]
           
        ContCasillas = 0           
    else:
        ContCasillas+=1
    Imagen.ActualizaFantasma(Fantasma,ImagenF.rect.x+SumaX,ImagenF.rect.y+SumaY,Direccion)
    return Recorrido, ContCasillas, Fila , Columna , VerticeFantasma

def DeterminaAlgoritmo(Algoritmo,GrafoNivel,VerticeFantasma,Destino,D,P):
    if Algoritmo == "Dijsktra":
        Recorrido = GR.Dijsktra(GrafoNivel,VerticeFantasma,Destino)
        return Recorrido
    if Algoritmo == "Floyd":
        Recorrido = RecorridoFloyd(GrafoNivel,D,P,VerticeFantasma,Destino)
        return Recorrido

