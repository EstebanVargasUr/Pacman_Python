import Grafo.Grafo as GR
import CargaImagen.CargaImagen as Imagen
def Movimiento(Direccion,Laberinto,x,y):
    
    # print("-----------------------------------")
    # for i in range(21):
    #     for j in range(21):
    #         print(Laberinto[i][j],end="")
    #     print("")
        
    if Direccion == "arriba":
        if Laberinto[x-1][y] == ' ' or Laberinto[x-1][y] == "." or Laberinto[x-1][y] == "O":
            Laberinto[x-1][y] = '$'
            Laberinto[x][y] = ' '
            return True
        else: return False     
    elif Direccion == "abajo":
        if Laberinto[x+1][y] == " " or Laberinto[x+1][y] == "." or Laberinto[x+1][y] == "O":
            Laberinto[x+1][y] = '$'
            Laberinto[x][y] = ' '
            return True
        else: return False
    if Direccion == "derecha":
        if Laberinto[x][y+1] == ' ' or Laberinto[x][y+1] == '.' or Laberinto[x][y+1] == 'O':
            Laberinto[x][y+1] = '$'
            Laberinto[x][y] = ' '
            return True
        else: return False
    elif Direccion == "izquierda":
        if Laberinto[x][y-1] == " " or Laberinto[x][y-1] == "." or Laberinto[x][y-1] == "O":
            Laberinto[x][y-1] = '$'
            Laberinto[x][y] = ' '
            return True
        else: return False
    else:
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

def MovimientoFantasma(ImagenF,Fantasma,Algoritmo,ContCasillas,Fila,Columna,MatrizV,UltimoVerticePacMan,VerticeFantasma,GrafoNivel,Recorrido,SumaX,SumaY,Direccion):
    if ContCasillas == 33:    
        if SumaX == 1:
            Columna += 1
        if SumaX == -1:
            Columna-=1
        if SumaY == 1:
            Fila +=1
        if SumaY == -1:
            Fila -=1

        if Fantasma != "Clyde" or Fantasma == "Clyde" and len(Recorrido)==1:
            if MatrizV[Fila][Columna] !='#' and MatrizV[Fila][Columna] !=' ':
                VerticeFantasma = MatrizV[Fila][Columna]
                Recorrido = DeterminaAlgoritmo(Algoritmo,GrafoNivel,VerticeFantasma,UltimoVerticePacMan)
        elif MatrizV[Fila][Columna] !='#' and MatrizV[Fila][Columna] !=' ':
            Recorrido.pop(len(Recorrido)-1)
            VerticeFantasma = MatrizV[Fila][Columna]
           
        ContCasillas = 0           
    else:
        ContCasillas+=1
    Imagen.ActualizaFantasma(Fantasma,ImagenF.rect.x+SumaX,ImagenF.rect.y+SumaY,Direccion)
    return Recorrido, ContCasillas, Fila , Columna , VerticeFantasma

def DeterminaAlgoritmo(Algoritmo,GrafoNivel,VerticeFantasma,UltVertPacMan):
    if Algoritmo == "Dijsktra":
        Recorrido = GR.Dijsktra(GrafoNivel,VerticeFantasma,UltVertPacMan)
        return Recorrido
    if Algoritmo == "Floyd":
        Recorrido = GR.floyd_warshall(GrafoNivel,VerticeFantasma)
        return Recorrido
