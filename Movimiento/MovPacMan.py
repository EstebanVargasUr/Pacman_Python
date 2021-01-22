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

def MovimientoFantasma(ContCasillas,Fila,Columna,MatrizV,UltimoVerticePacMan,VerticeFantasma,GrafoNivel,Recorrido,SumaX, SumaY,direccion):
    if ContCasillas == 33:
        
        if SumaX == 1:
            Columna += 1
        if SumaX == -1:
            Columna-=1
        if SumaY == 1:
            Fila +=1
        if SumaY == -1:
            Fila -=1

        if MatrizV[Fila][Columna] !='#' and MatrizV[Fila][Columna] !=' ':
            VerticeFantasma = MatrizV[Fila][Columna]
            Recorrido = DeterminaAlgoritmo("DijsktraCorto",GrafoNivel,VerticeFantasma,UltimoVerticePacMan)
           
        ContCasillas = 0           
    else:
        ContCasillas+=1
    Imagen.ActualizaFantasma(Imagen.ImgBlinky,Imagen.ImgBlinky.rect.x+SumaX,Imagen.ImgBlinky.rect.y+SumaY,direccion)
    return Recorrido, ContCasillas, Fila , Columna , VerticeFantasma

def DeterminaAlgoritmo(Algoritmo,GrafoNivel,VerticeFantasma,UltVertPacMan):
    if Algoritmo == "DijsktraCorto":
        Recorrido = GR.DijsktraCorto(GrafoNivel,VerticeFantasma,UltVertPacMan)
        return Recorrido
    elif Algoritmo == "DijsktraLargo":
        print()
    elif Algoritmo == "Floyd":
        print()
