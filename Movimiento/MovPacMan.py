def Movimiento(Direccion,Lista,x,y):
    Laberinto = Lista[0]
    
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
    if Direccion == "derecha":
        if Laberinto[x][y+1] == ' ' or Laberinto[x][y+1] == '.' or Laberinto[x][y+1] == 'O':
            return True
        else: return False
    if Direccion == "izquierda":
        if Laberinto[x][y-1] == ' ' or Laberinto[x][y-1] == "." or Laberinto[x][y-1] == "O":
            return True
        else: return False