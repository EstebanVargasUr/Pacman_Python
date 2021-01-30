import pygame, sys
import CargaImagen.CargaImagen as Imagen
import CreaNivel.MapRand as Nivel
import Movimiento.MovPacMan as MovPacMan
import CreaNivel.LecturaEscritura as RW
import Grafo.Grafo as GR
import threading
import random
import time

class Juego():

    def __init__(self):
        pygame.init()
        tamano_ventana = (1200,720)
        self.ventana = pygame.display.set_mode(tamano_ventana)

        pygame.display.set_icon(Imagen.icono_ventana)
        pygame.display.set_caption('PAC-MAN')
        
        self.niveles = list()
        self.NumNivel= ""
        self.datosJugador= RW.fileRead("CreaNivel/DatosJugador/jugador.txt")
        self.MatrizVertice = []
        self.MatrizTunel = []
        self.GrafoNivel = GR.Graph() 
        self.Escena = "MenuPrincipal"
        self.Puntos = 0
        self.cont = 0
        self.PoderPellet = False
        self.ConteoActivo = False
        self.Vidas = 0
        self.Victoria = False
        self.PoderAdquirido = False
        self.contPoder = 0
        self.PoderActivo = False
        self.PoderFinalizado = False

        self.Dificultad = "Dificil"
        self.AlgoritmosFantasmas = ["","","",""]

        self.MatrizDistancias , self.MatrizCaminos = dict() , dict() 

        self.CuadroTexto = pygame.Rect(500, 360, 200, 42)
        self.color_inactive = pygame.Color('white')
        self.color_active = pygame.Color('white')
        self.color = self.color_inactive
        self.active = False
        self.NombreJugador = ''
        self.font = pygame.font.Font(None, 42)
        self.font2 = pygame.font.Font(None, 57)
        self.TituloJugador =""
        self.LblJugador =""
        self.TituloPuntos=""
        self.LblPuntos=""
        self.TituloVidas=""
        self.LblVidas=""
        self.VelocidadPacMan = 1
        self.LimiteCasillasPacMan = 34


        self.DireccionPacman = "inicio"
        self.DireccionPacman2 = ""
        self.Permitido = False
        self.FilaPacMan = 13 # FILA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
        self.ColPacMan = 10  # COLUMNA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
        self.PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
        self.PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
        self.UltimoVerticePacMan = ''
        self.SigVerticePacMan = ''
        self.ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
        self.Jugador = Imagen.Jugador # PERMITE OBTENER LA UBICACION
        self.NivelSeleccionado = False
        self.ClickBtnNivel = False
        #Variables para fantasmas
        self.ClickBtnNivel = False
        #Blinky
        self.RecorridoBlinky = []
        self.ContCasillasBlinky = 0
        self.VerticeBlinky = ''
        self.FilaBlinky = 9
        self.ColBlinky = 8
        self.BlinkyMuerto = False
        self.CargandoBlinky = False
        
        #Pinky
        self.RecorridoPinky = []
        self.ContCasillasPinky = 0
        self.VerticePinky = ''
        self.FilaPinky = 9
        self.ColPinky = 12
        self.AlgoritmoPinky = ""
        self.PinkyMuerto = False
        self.CargandoPinky = False

        #Clyde
        self.RecorridoClyde = []
        self.ContCasillasClyde = 0
        self.VerticeClyde = ''
        self.FilaClyde = 11
        self.ColClyde = 12
        self.ClydeMuerto = False
        self.AlgoritmoClyde = ""
        self.CargandoClyde = False
        
        #Inky
        self.RecorridoInky = []
        self.ContCasillasInky = 0
        self.VerticeInky = ''
        self.FilaInky = 11
        self.ColInky = 8
        self.InkyMuerto = False
        self.CargandoInky = False

        self.numRand= 1
        self.posicion= str(self.numRand)

        self.NivelesDesbloqueados= False
        self.PuntajeSinPerder=0
        self.Partida1=0
        self.Partida2=0
        self.Partida3=0
        self.Partida4=0
        self.Partida5=0
        self.Partida6=0
        self.Partida7=0
        self.Partida8=0
        self.Partida9=0
        self.Partida10=0
        self.Puntos1=0
        self.Puntos2=0
        self.Puntos3=0
        self.Puntos4=0
        self.Puntos5=0
        self.Puntos6=0
        self.Puntos7=0
        self.Puntos8=0
        self.Puntos9=0
        self.Puntos10=0
        self.tiempoJugado=0
        self.tiempoBandera= False
        self.Top10= list()
        self.BanderaPuntajeTop=False
    def LimpiarPantalla(self):
        self.ventana.fill((0,0,0)) # LIMPIA PANTALLA
    
        if self.NivelSeleccionado == True:
            self.PosXPacMan = self.Jugador.rect.x
            self.PosYPacMan = self.Jugador.rect.y
    def LimpiarFantasmas(self):
        #Blinky
        self.RecorridoBlinky = []
        self.ContCasillasBlinky = 0
        self.VerticeBlinky = ''
        self.FilaBlinky = 9
        self.ColBlinky = 8
        self.BlinkyMuerto = False
        self.CargandoBlinky = False
        Imagen.ActualizaFantasma("Blinky",277,311,"abajo")
        #Pinky
        self.RecorridoPinky = []
        self.ContCasillasPinky = 0
        self.VerticePinky = ''
        self.FilaPinky = 9
        self.ColPinky = 12
        self.PinkyMuerto = False
        self.CargandoPinky = False
        Imagen.ActualizaFantasma("Pinky",413,311,"abajo")
        #Inky
        self.RecorridoInky = []
        self.ContCasillasInky = 0
        self.VerticeInky = ''
        self.FilaInky = 11
        self.ColInky = 8
        self.InkyMuerto = False
        self.CargandoInky = False
        Imagen.ActualizaFantasma("Inky",277,379,"abajo")
        #Clyde
        self.RecorridoClyde = []
        self.ContCasillasClyde = 0
        self.VerticeClyde = ''
        self.FilaClyde = 11
        self.ColClyde = 12
        self.ClydeMuerto = False
        self.CargandoClyde = False
        Imagen.ActualizaFantasma("Clyde",413,379,"abajo")

    #CUENTA EL TIEMPO DE 10 SEGUNDOS DE INMUNIDAD AL COMERSE UN POWER PELLET
    def contador(self):
        self.cont = 0
        while self.cont < 10: 
            time.sleep(1)
            #print(self.cont)
            self.cont +=1
        self.ConteoActivo = False
    
    def tiempoTranscurrido(self):
        while self.tiempoBandera!=False: 
            time.sleep(1)
            self.tiempoJugado +=1


    def ContadorPoder(self):
        self.contPoder = 0
        while self.contPoder < 6: 
            time.sleep(1)
            self.contPoder +=1
        self.PoderFinalizado = True
        
        
    def LimpiarNivel(self):
        self.Victoria = False
        self.DireccionPacman = "inicio"
        self.DireccionPacman2 = ""
        self.Permitido = False
        self.FilaPacMan = 13 # FILA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
        self.ColPacMan = 10  # COLUMNA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
        self.PosXPacMan = 343  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
        self.PosYPacMan = 445  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
        Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
        self.UltimoVerticePacMan = ''
        self.SigVerticePacMan = ''
        self.ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
        self.Jugador = Imagen.Jugador # PERMITE OBTENER LA UBICACION
        self.NivelSeleccionado = False
        self.LimpiarFantasmas()
    def IniciarFantasmas(self):

        if self.ClickBtnNivel == True:
            self.ClickBtnNivel = False

            self.AlgoritmosFantasmas.clear()
            if self.Dificultad == "Dificil":
                self.AlgoritmosFantasmas.append("Dijsktra")
                self.AlgoritmosFantasmas.append("Dijsktra")
                self.AlgoritmosFantasmas.append("Dijsktra")
                self.AlgoritmosFantasmas.append("Floyd")
            else:
                for i in range(4):
                    Algorirtmo = random.randint(1, 2)
                    if Algorirtmo == 1 or i == 2:
                        self.AlgoritmosFantasmas.append("Dijsktra")
                    else:
                        self.AlgoritmosFantasmas.append("Floyd")

            if "Floyd" in self.AlgoritmosFantasmas:
                self.MatrizDistancias,self.MatrizCaminos = GR.floyd_warshall(self.GrafoNivel)

            print(self.AlgoritmosFantasmas)

        #Blinky
        self.VerticeBlinky = self.MatrizVertice[9][8]
        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.UltimoVerticePacMan = self.MatrizVertice[13][i]
                break
        self.RecorridoBlinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[0],self.GrafoNivel,self.VerticeBlinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)

        #Pinky
        self.VerticePinky = self.MatrizVertice[9][12]
        self.AlgoritmoPinky = self.AlgoritmosFantasmas[1]
        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.SigVerticePacMan = self.MatrizVertice[13][i]
                break
        self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[1],self.GrafoNivel,self.VerticePinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)

        #Inky
        self.VerticeInky = self.MatrizVertice[11][8]
        self.numRand=random.randint(1, len(self.GrafoNivel.nodes))

        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.UltimoVerticePacMan = self.MatrizVertice[13][i]
                break
        self.RecorridoInky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[2],self.GrafoNivel,self.VerticeInky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)

        #Clyde
        self.VerticeClyde = self.MatrizVertice[11][12]
        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.UltimoVerticePacMan = self.MatrizVertice[13][i]
                break
        Destino = random.randint(1, len(self.GrafoNivel.nodes))
        self.RecorridoClyde = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[3],self.GrafoNivel,self.VerticeClyde,str(Destino),self.MatrizDistancias,self.MatrizCaminos)

    def EvaluarVictoria(self):
        if self.Escena=='Nivel10':
                self.NumNivel='10'
        else:
            self.NumNivel = self.Escena[len(self.Escena)-1]

        m = self.niveles[int(self.NumNivel)-1]
        for i in range(21):
            for j in range(21):
                if m[i][j] == '.':
                    self.Victoria = False
                    break
                else:
                    self.Victoria = True
            if self.Victoria == False:
                break      
        if self.Victoria:
            if self.NumNivel == "1": self.Puntos += 100
            elif self.NumNivel == "2": self.Puntos += 200
            elif self.NumNivel == "3": self.Puntos += 300
            elif self.NumNivel == "4": self.Puntos += 400
            elif self.NumNivel == "5": self.Puntos += 500
            elif self.NumNivel == "6": self.Puntos += 600
            elif self.NumNivel == "7": self.Puntos += 700
            elif self.NumNivel == "8": self.Puntos += 800
            elif self.NumNivel == "9": self.Puntos += 900
            elif self.NumNivel == "10": self.Puntos += 1000


    def CompruebaPoder(self):
        cont = 0
        if self.BlinkyMuerto:
            cont +=1
        if self.PinkyMuerto:
            cont +=1
        if self.InkyMuerto:
            cont +=1
        if self.ClydeMuerto:
            cont +=1

        if cont > 1:
            self.PoderAdquirido = True
            


    #VERIFICA SI UN FANTASMA TOCA A PACMAN Y LE RESTA UNA VIDA
    def ComprobarDerrota(self):
        if self.FilaBlinky == self.FilaPacMan and self.ColBlinky == self.ColPacMan and not self.BlinkyMuerto:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaClyde == self.FilaPacMan and self.ColClyde == self.ColPacMan and not self.ClydeMuerto:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaInky == self.FilaPacMan and self.ColInky == self.ColPacMan and not self.InkyMuerto:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaPinky == self.FilaPacMan and self.ColPinky == self.ColPacMan and not self.PinkyMuerto:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()

    def ComerFantasma(self):
        if self.FilaBlinky == self.FilaPacMan and self.ColBlinky == self.ColPacMan and not self.BlinkyMuerto:
            self.BlinkyMuerto = True
            self.Puntos += 300
        if self.FilaClyde == self.FilaPacMan and self.ColClyde == self.ColPacMan and not self.ClydeMuerto:
            self.ClydeMuerto = True
            self.Puntos += 300
        if self.FilaInky == self.FilaPacMan and self.ColInky == self.ColPacMan and not self.InkyMuerto:
            self.InkyMuerto = True
            self.Puntos += 300
        if self.FilaPinky == self.FilaPacMan and self.ColPinky == self.ColPacMan and not self.PinkyMuerto:
            self.PinkyMuerto = True
            self.Puntos += 300

    def ReiniciaNivel(self):
        if self.Escena=='Nivel10':
            self.NumNivel='10'
        else:
            self.NumNivel = self.Escena[len(self.Escena)-1]

        self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = ' '
        self.niveles[int(self.NumNivel)-1][13][10] = "$"
        Matriz = self.niveles[int(self.NumNivel)-1]

        Matriz[1][1]='O'
        Matriz[19][1]='O'
        Matriz[1][19]='O'
        Matriz[19][19]='O'

        for i in range(21):
            for j in range(21):
                if j >= 15 or j <= 5:
                    if Matriz[i][j]==" ":
                        Matriz[i][j]="."
                if i >= 14 or i <= 6:
                    if Matriz[i][j]==" ":
                        Matriz[i][j]="."
                
    def IniciaNivel(self,Nivel):
        self.Escena = "Nivel"+str(Nivel)
        self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(Nivel,self.niveles)
        Imagen.CargaNivel(Nivel,self.niveles)
        Imagen.CargaPuntos(Nivel,self.niveles)
        self.Jugador = Imagen.ColocaPacMan(Nivel,self.niveles)
        self.NivelSeleccionado = True
        self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[Nivel-1])
        self.ClickBtnNivel = True

    def DeterminaRecorridosIguales(self):
        #if self.RecorridoPinky == None:
        #    self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[1],self.GrafoNivel,self.VerticePinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)
        if self.RecorridoPinky != None and len(self.RecorridoPinky) != 0:
            for i in range(20):
                for j in range(20):
                    if self.MatrizVertice[i][j] == self.VerticePinky:

                        for h in range(j+1,20):
                            if self.MatrizVertice[i][h] == "#":
                                break
                            if self.MatrizVertice[i][h] != " " and self.MatrizVertice[i][h] != "#":
                                self.VerticePinky = self.MatrizVertice[i][h]
                                if self.AlgoritmosFantasmas[1] == "Floyd":
                                    self.RecorridoPinky[-1] = 'derecha'
                                else:
                                    self.RecorridoPinky[0] = 'derecha'
                                return self.VerticePinky
                        for h in reversed(range(j-1)):
                            if self.MatrizVertice[i][h] == "#":
                                break
                            if self.MatrizVertice[i][h] != " " and self.MatrizVertice[i][h] != "#":
                                self.VerticePinky = self.MatrizVertice[i][h]
                                if self.AlgoritmosFantasmas[1] == "Floyd":
                                    self.RecorridoPinky[-1] = 'izquierda'
                                else:
                                    self.RecorridoPinky[0] = 'izquierda'
                                return self.VerticePinky
                        for h in range(i+1,20):
                            if self.MatrizVertice[h][j] == "#":
                                break
                            elif self.MatrizVertice[h][j] != " " and self.MatrizVertice[h][j] != "#":
                                self.VerticePinky = self.MatrizVertice[h][j]
                                if self.AlgoritmosFantasmas[1] == "Floyd":
                                    self.RecorridoPinky[-1] = 'abajo'
                                else:
                                    self.RecorridoPinky[0] = 'abajo'
                                return self.VerticePinky
                        for h in reversed(range(i-1)):
                            if self.MatrizVertice[h][j] == "#":
                                break
                            elif self.MatrizVertice[h][j] != " " and self.MatrizVertice[h][j] != "#":
                                self.VerticePinky = self.MatrizVertice[h][j]
                                if self.AlgoritmosFantasmas[1] == "Floyd":
                                    self.RecorridoPinky[-1] = 'arriba'
                                else:
                                    self.RecorridoPinky[0] = 'arriba'
                                return self.VerticePinky
    def determinaNivelPuntaje(self):
        if self.Escena=='Nivel1':
            self.Puntos1=self.Puntos1+10
        if self.Escena=='Nivel2':
            self.Puntos2=self.Puntos2+10
        if self.Escena=='Nivel3':   
            self.Puntos3=self.Puntos3+10
        if self.Escena=='Nivel4':    
            self.Puntos4=self.Puntos4+10
        if self.Escena=='Nivel5': 
            self.Puntos5=self.Puntos5+10
        if self.Escena=='Nivel6':     
            self.Puntos6=self.Puntos6+10
        if self.Escena=='Nivel7':   
            self.Puntos7=self.Puntos7+10
        if self.Escena=='Nivel8':   
            self.Puntos8=self.Puntos8+10
        if self.Escena=='Nivel9':  
            self.Puntos9=self.Puntos9+10
        if self.Escena=='Nivel10':    
            self.Puntos10=self.Puntos10+10

    def CargaEstadisticas(self):
        self.create_sound()
        for i in range(10):
            self.niveles.append(RW.fileRead("CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt"))
        self.datosJugador=RW.fileRead("CreaNivel/DatosJugador/jugador.txt")
        self.NombreJugador= self.datosJugador[0]
        self.Puntos= int(self.datosJugador[1])
        self.Vidas= int(self.datosJugador[2])
        self.NivelesDesbloqueados= self.datosJugador[3]
        self.PuntajeSinPerder= self.datosJugador[4]
        self.Partida1=int(self.datosJugador[5])
        self.Partida2=int(self.datosJugador[6])
        self.Partida3=int(self.datosJugador[7])
        self.Partida4=int(self.datosJugador[8])
        self.Partida5=int(self.datosJugador[9])
        self.Partida6=int(self.datosJugador[10])
        self.Partida7=int(self.datosJugador[11])
        self.Partida8=int(self.datosJugador[12])
        self.Partida9=int(self.datosJugador[13])
        self.Partida10=int(self.datosJugador[14])
        self.Puntos1=int(self.datosJugador[15])
        self.Puntos2=int(self.datosJugador[16])
        self.Puntos3=int(self.datosJugador[17])
        self.Puntos4=int(self.datosJugador[18])
        self.Puntos5=int(self.datosJugador[19])
        self.Puntos6=int(self.datosJugador[20])
        self.Puntos7=int(self.datosJugador[21])
        self.Puntos8=int(self.datosJugador[22])
        self.Puntos9=int(self.datosJugador[23])
        self.Puntos10=int(self.datosJugador[24])
        self.tiempoJugado=int(self.datosJugador[25])

    def SelectionSort(self,lista):
        for i in range(10,20): 
            minimo = i 
            for j in range(i+1, len(lista)): 
                if lista[minimo] <= lista[j]: 
                    minimo = j        
            lista[i], lista[minimo] = lista[minimo], lista[i]
            lista[i-10], lista[minimo-10] = lista[minimo-10], lista[i-10]  
    def entraTop(self):
        for i in range(10,20): 
            if int(self.Top10[i]) <= self.Puntos:
                self.BanderaPuntajeTop=True
    def verificaNombres(self):
        for i in range(0,10): 
            if str(self.Top10[i]) == self.NombreJugador:
                self.Top10[i+10]=self.Puntos
                self.Top10[i]=self.NombreJugador
                return True
    def Eventos(self):
        for event in pygame.event.get(): #EVENTOS
            if event.type == pygame.QUIT: #CIERRA VENTANA
                self.cont = 10
                self.contPoder = 6
                if len(self.niveles)!=0:
                    for i in range(10):
                        RW.fileWrite(self.niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                    self.datosJugador[1]=self.Puntos
                    self.datosJugador[2]=self.Vidas
                    self.datosJugador[3]=self.NivelesDesbloqueados
                    self.datosJugador[4]=self.PuntajeSinPerder
                    self.datosJugador[5]=self.Partida1
                    self.datosJugador[6]=self.Partida2
                    self.datosJugador[7]=self.Partida3
                    self.datosJugador[8]=self.Partida4
                    self.datosJugador[9]=self.Partida5
                    self.datosJugador[10]=self.Partida6
                    self.datosJugador[11]=self.Partida7
                    self.datosJugador[12]=self.Partida8
                    self.datosJugador[13]=self.Partida9
                    self.datosJugador[14]=self.Partida10
                    self.datosJugador[15]=self.Puntos1
                    self.datosJugador[16]=self.Puntos2
                    self.datosJugador[17]=self.Puntos3
                    self.datosJugador[18]=self.Puntos4
                    self.datosJugador[19]=self.Puntos5
                    self.datosJugador[20]=self.Puntos6
                    self.datosJugador[21]=self.Puntos7
                    self.datosJugador[22]=self.Puntos8
                    self.datosJugador[23]=self.Puntos9
                    self.datosJugador[24]=self.Puntos10
                    self.datosJugador[25]=self.tiempoJugado
                    RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                self.tiempoBandera=False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN: #CLICK
                if pygame.mouse.get_pressed()[0]: #SI PRESIONA CLICK IZQUIERDO
                    if self.Escena == "MenuPrincipal":
                        if Imagen.btnJugar.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "SelectorPartida" 
                        if Imagen.btnJugador.rect.collidepoint(pygame.mouse.get_pos()):
                            self.Escena = "Jugador"
                        if Imagen.btnAjustes.rect.collidepoint(pygame.mouse.get_pos()):
                            self.Escena = "Ajustes"
                        if Imagen.btnSalir.rect.collidepoint(pygame.mouse.get_pos()):
                            if len(self.niveles)!=0:
                                for i in range(10):
                                    RW.fileWrite(self.niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                                self.datosJugador[1]=self.Puntos
                                self.datosJugador[2]=self.Vidas
                                self.datosJugador[3]=self.NivelesDesbloqueados
                                self.datosJugador[4]=self.PuntajeSinPerder
                                self.datosJugador[5]=self.Partida1
                                self.datosJugador[6]=self.Partida2
                                self.datosJugador[7]=self.Partida3
                                self.datosJugador[8]=self.Partida4
                                self.datosJugador[9]=self.Partida5
                                self.datosJugador[10]=self.Partida6
                                self.datosJugador[11]=self.Partida7
                                self.datosJugador[12]=self.Partida8
                                self.datosJugador[13]=self.Partida9
                                self.datosJugador[14]=self.Partida10
                                self.datosJugador[15]=self.Puntos1
                                self.datosJugador[16]=self.Puntos2
                                self.datosJugador[17]=self.Puntos3
                                self.datosJugador[18]=self.Puntos4
                                self.datosJugador[19]=self.Puntos5
                                self.datosJugador[20]=self.Puntos6
                                self.datosJugador[21]=self.Puntos7
                                self.datosJugador[22]=self.Puntos8
                                self.datosJugador[23]=self.Puntos9
                                self.datosJugador[24]=self.Puntos10
                                self.datosJugador[25]=self.tiempoJugado
                                RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                            self.tiempoBandera=False
                            self.cont=10
                            #self.contPoder=6
                            sys.exit()
                    elif self.Escena == "SelectorPartida":
                        if Imagen.btnNuevaPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "RegistraNombre"
                            self.NombreJugador=""
                            self.Puntos=0
                            self.Vidas=6
                            self.NivelesDesbloqueados=False
                            self.Partida1=0
                            self.Partida2=0
                            self.Partida3=0
                            self.Partida4=0
                            self.Partida5=0
                            self.Partida6=0
                            self.Partida7=0
                            self.Partida8=0
                            self.Partida9=0
                            self.Partida10=0
                            self.Puntos1=0
                            self.Puntos2=0
                            self.Puntos3=0
                            self.Puntos4=0
                            self.Puntos5=0
                            self.Puntos6=0
                            self.Puntos7=0
                            self.Puntos8=0
                            self.Puntos9=0
                            self.Puntos10=0
                            self.tiempoJugado=0
                            self.niveles.clear()
                            for i in range(10):
                                self.niveles.append(Nivel.laberinto(10,10))
                                RW.fileWrite(self.niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                                
                        if Imagen.btnCargarPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            game.CargaEstadisticas()
                            if self.Vidas==0:
                                self.Escena='GameOver'
                            else:
                                self.Escena = "SelectorNivel"

                    elif self.Escena == "RegistraNombre":
                        # If the user clicked on the input_box rect.
                        if self.CuadroTexto.collidepoint(event.pos):
                            # Toggle the active variable.
                            self.active = not self.active
                        else:
                            self.active = False
                            # Change the current color of the input box.
                            self.color = self.color_active if self.active else self.color_inactive
                    elif self.Escena == "GameOver":
                        if Imagen.btnAbandonar.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena='MenuPrincipal'
                    elif self.Escena == "Ajustes":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "MenuPrincipal"
                        if Imagen.btnDesbloquea.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.NivelesDesbloqueados=True
                            self.datosJugador[3]=self.NivelesDesbloqueados
                            RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                        if Imagen.btnMedio.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Dificultad = "Medio"
                        if Imagen.btnDificil.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Dificultad = "Dificil"
                    elif self.Escena == "Jugador":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "MenuPrincipal"
                        if Imagen.btnTop.rect.collidepoint(pygame.mouse.get_pos()):
                            self.Escena= "Top"
                            self.Top10=RW.fileRead("CreaNivel/DatosJugador/top10.txt")
                            self.entraTop()
                            if self.BanderaPuntajeTop == True:
                                if self.verificaNombres() != True:
                                    self.Top10[9]=self.NombreJugador
                                    self.Top10[19]=self.Puntos
                                self.SelectionSort(self.Top10)
                                RW.fileWrite(self.Top10,"CreaNivel/DatosJugador/top10.txt")
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "MenuPrincipal"
                    elif self.Escena == "Top":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "MenuPrincipal"
                    elif self.Escena == "SelectorNivel":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.datosJugador[1]=self.Puntos
                            self.datosJugador[2]=self.Vidas
                            self.datosJugador[3]=self.NivelesDesbloqueados
                            self.datosJugador[4]=self.PuntajeSinPerder
                            self.datosJugador[5]=self.Partida1
                            self.datosJugador[6]=self.Partida2
                            self.datosJugador[7]=self.Partida3
                            self.datosJugador[8]=self.Partida4
                            self.datosJugador[9]=self.Partida5
                            self.datosJugador[10]=self.Partida6
                            self.datosJugador[11]=self.Partida7
                            self.datosJugador[12]=self.Partida8
                            self.datosJugador[13]=self.Partida9
                            self.datosJugador[14]=self.Partida10
                            self.datosJugador[15]=self.Puntos1
                            self.datosJugador[16]=self.Puntos2
                            self.datosJugador[17]=self.Puntos3
                            self.datosJugador[18]=self.Puntos4
                            self.datosJugador[19]=self.Puntos5
                            self.datosJugador[20]=self.Puntos6
                            self.datosJugador[21]=self.Puntos7
                            self.datosJugador[22]=self.Puntos8
                            self.datosJugador[23]=self.Puntos9
                            self.datosJugador[24]=self.Puntos10
                            self.datosJugador[25]=self.tiempoJugado
                            RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                            self.Escena = "MenuPrincipal"
                        if Imagen.btnSelecNiv1.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.IniciaNivel(1)
                            self.Partida1=self.Partida1+1
                        if Imagen.btnSelecNiv2.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 1500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(2)
                                self.Partida2=self.Partida2+1
                        if Imagen.btnSelecNiv3.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 2500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(3)
                                self.Partida3=self.Partida3+1
                        if Imagen.btnSelecNiv4.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 3500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(4)
                                self.Partida4=self.Partida4+1
                        if Imagen.btnSelecNiv5.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 4500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(5)
                                self.Partida5=self.Partida5+1
                        if Imagen.btnSelecNiv6.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 5500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(6)
                                self.Partida6=self.Partida6+1
                        if Imagen.btnSelecNiv7.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 6500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(7)
                                self.Partida7=self.Partida7+1
                        if Imagen.btnSelecNiv8.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 7500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(8)
                                self.Partida8=self.Partida8+1
                        if Imagen.btnSelecNiv9.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 8500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(9)
                                self.Partida9=self.Partida9+1
                        if Imagen.btnSelecNiv10.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            if self.Puntos >= 9500 or self.NivelesDesbloqueados ==True:
                                self.IniciaNivel(10)
                                self.Partida10=self.Partida10+1
                    elif self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.LimpiarNivel()
                            self.Escena = "SelectorNivel"
                        if Imagen.btnHome.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.ReiniciaNivel()
                            self.LimpiarNivel()
                            self.Escena = "MenuPrincipal"
                        if Imagen.btnNiveles.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.ReiniciaNivel()
                            self.LimpiarNivel()
                            self.Escena = "SelectorNivel"
                        if Imagen.btnSiguiente.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.ReiniciaNivel()
                            self.LimpiarNivel()
                            if self.Escena=='Nivel10':
                                self.Escena = "SelectorNivel"
                                self.IniciaNivel(10)
                            else:
                                self.NumNivel = str(1+int(self.Escena[5]))
                                self.Escena = "Nivel"+self.NumNivel
                                self.IniciaNivel(int(self.NumNivel))
                        if Imagen.btnPoder.rect.collidepoint(pygame.mouse.get_pos()) and self.PoderAdquirido == True: #CLICK DENTRO DEL SPRITE
                            self.PoderAdquirido = False
                            self.PoderActivo = True
                            
            if event.type == pygame.KEYDOWN: # EVENTOS DE TECLADO
                if self.Escena == "RegistraNombre":
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            if self.NombreJugador != '':
                                self.Escena = "SelectorNivel"
                                self.datosJugador.append(str(self.NombreJugador))
                                self.datosJugador.append(self.Puntos)
                                self.datosJugador.append(self.Vidas)
                                self.datosJugador.append(self.NivelesDesbloqueados)
                                self.datosJugador.append(self.PuntajeSinPerder)
                                self.datosJugador.append(self.Partida1)
                                self.datosJugador.append(self.Partida2)
                                self.datosJugador.append(self.Partida3)
                                self.datosJugador.append(self.Partida4)
                                self.datosJugador.append(self.Partida5)
                                self.datosJugador.append(self.Partida6)
                                self.datosJugador.append(self.Partida7)
                                self.datosJugador.append(self.Partida8)
                                self.datosJugador.append(self.Partida9)
                                self.datosJugador.append(self.Partida10)
                                self.datosJugador.append(self.Puntos1)
                                self.datosJugador.append(self.Puntos2)
                                self.datosJugador.append(self.Puntos3)
                                self.datosJugador.append(self.Puntos4)
                                self.datosJugador.append(self.Puntos5)
                                self.datosJugador.append(self.Puntos6)
                                self.datosJugador.append(self.Puntos7)
                                self.datosJugador.append(self.Puntos8)
                                self.datosJugador.append(self.Puntos9)
                                self.datosJugador.append(self.Puntos10)
                                self.datosJugador.append(self.tiempoJugado)
                                RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                        elif event.key == pygame.K_BACKSPACE:
                            self.NombreJugador = self.NombreJugador[:-1]
                        else:
                            self.NombreJugador += event.unicode
                if self.Escena == "SelectorNivel":
                    if event.key == pygame.K_ESCAPE:
                        self.Escena = "MenuPrincipal"
                if self.Escena == "Ajustes":
                    if event.key == pygame.K_ESCAPE:
                        self.Escena = "MenuPrincipal"
                if self.Escena == "Jugador":
                    if event.key == pygame.K_ESCAPE:
                        self.Escena = "MenuPrincipal"
                if self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
                    if event.key == pygame.K_ESCAPE:
                        self.LimpiarNivel()
                        self.Escena = "SelectorNivel"
                    if self.Escena=='Nivel10':
                        self.NumNivel='10'
                    else:
                        self.NumNivel = self.Escena[5]
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if MovPacMan.VerificaMovimiento("arriba",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= self.LimiteCasillasPacMan:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=self.VelocidadPacMan
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=self.VelocidadPacMan
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=self.VelocidadPacMan
                            if self.DireccionPacman != "arriba":
                                self.DireccionPacman = "arriba"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "arriba"
                            self.Permitido = True
                        
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if MovPacMan.VerificaMovimiento("abajo",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= self.LimiteCasillasPacMan:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=self.VelocidadPacMan
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=self.VelocidadPacMan
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=self.VelocidadPacMan
                            if self.DireccionPacman != "abajo":
                                self.DireccionPacman = "abajo"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "abajo"
                            self.Permitido = True

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                        if MovPacMan.VerificaMovimiento("derecha",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= self.LimiteCasillasPacMan:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=self.VelocidadPacMan
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=self.VelocidadPacMan
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=self.VelocidadPacMan
                            if self.DireccionPacman != "derecha":
                                self.DireccionPacman = "derecha"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "derecha"
                            self.Permitido = True
                        
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if MovPacMan.VerificaMovimiento("izquierda",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= self.LimiteCasillasPacMan:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=self.VelocidadPacMan
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=self.VelocidadPacMan
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=self.VelocidadPacMan
                            if self.DireccionPacman != "izquierda":
                                self.DireccionPacman = "izquierda"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "izquierda"
                            self.Permitido = True   

                    if event.key == pygame.K_f and self.PoderAdquirido == True:
                        self.PoderAdquirido = False
                        self.PoderActivo = True
                   

    def CargarGraficaNivel(self):
        if self.ClickBtnNivel == True:
            self.IniciarFantasmas()

        if self.Escena == "Ajustes":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupAjustes.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
        if self.Escena == "Jugador":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupEstadisiticas.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
            self.LblPuntos = self.font.render(str(self.Puntos), True, 'white')
            self.ventana.blit(self.LblPuntos, (400, 150))
            self.LblVidas= self.font.render(str(6-self.Vidas), True, 'white')
            self.ventana.blit(self.LblVidas, (1100, 155))
            puntajeSinPerder= self.font.render(str(self.PuntajeSinPerder), True, 'white')
            self.ventana.blit(puntajeSinPerder, (440, 240))
            tiempo= self.font.render(str(self.tiempoJugado), True, 'white')
            self.ventana.blit(tiempo, (1070, 240))
            partida1= self.font.render(str(self.Partida1), True, 'white')
            partida2= self.font.render(str(self.Partida2), True, 'white')
            partida3= self.font.render(str(self.Partida3), True, 'white')
            partida4= self.font.render(str(self.Partida4), True, 'white')
            partida5= self.font.render(str(self.Partida5), True, 'white')
            partida6= self.font.render(str(self.Partida6), True, 'white')
            partida7= self.font.render(str(self.Partida7), True, 'white')
            partida8= self.font.render(str(self.Partida8), True, 'white')
            partida9= self.font.render(str(self.Partida9), True, 'white')
            partida10= self.font.render(str(self.Partida10), True, 'white')
            self.ventana.blit(partida1, (170, 395))
            self.ventana.blit(partida2, (360, 395))
            self.ventana.blit(partida3, (560, 395))
            self.ventana.blit(partida4, (760, 395))
            self.ventana.blit(partida5, (960, 395))
            self.ventana.blit(partida6, (170, 555))
            self.ventana.blit(partida7, (360, 555))
            self.ventana.blit(partida8, (560, 555))
            self.ventana.blit(partida9, (760, 555))
            self.ventana.blit(partida10, (960, 555))
            puntos1= self.font.render(str(self.Puntos1), True, 'white')
            puntos2= self.font.render(str(self.Puntos2), True, 'white')
            puntos3= self.font.render(str(self.Puntos3), True, 'white')
            puntos4= self.font.render(str(self.Puntos4), True, 'white')
            puntos5= self.font.render(str(self.Puntos5), True, 'white')
            puntos6= self.font.render(str(self.Puntos6), True, 'white')
            puntos7= self.font.render(str(self.Puntos7), True, 'white')
            puntos8= self.font.render(str(self.Puntos8), True, 'white')
            puntos9= self.font.render(str(self.Puntos9), True, 'white')
            puntos10= self.font.render(str(self.Puntos10), True, 'white')
            self.ventana.blit(puntos1, (170, 355))
            self.ventana.blit(puntos2, (360, 355))
            self.ventana.blit(puntos3, (560, 355))
            self.ventana.blit(puntos4, (760, 355))
            self.ventana.blit(puntos5, (960, 355))
            self.ventana.blit(puntos6, (170, 515))
            self.ventana.blit(puntos7, (360, 515))
            self.ventana.blit(puntos8, (560, 515))
            self.ventana.blit(puntos9, (760, 515))
            self.ventana.blit(puntos10, (960, 515))
        if self.Escena == "Top":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupTop.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
            jugador1= self.font.render(str(self.Top10[0]), True, 'white')
            jugador2= self.font.render(str(self.Top10[1]), True, 'white')
            jugador3= self.font.render(str(self.Top10[2]), True, 'white')
            jugador4= self.font.render(str(self.Top10[3]), True, 'white')
            jugador5= self.font.render(str(self.Top10[4]), True, 'white')
            jugador6= self.font.render(str(self.Top10[5]), True, 'white')
            jugador7= self.font.render(str(self.Top10[6]), True, 'white')
            jugador8= self.font.render(str(self.Top10[7]), True, 'white')
            jugador9= self.font.render(str(self.Top10[8]), True, 'white')
            jugador10= self.font.render(str(self.Top10[9]), True, 'white')
            self.ventana.blit(jugador1, (470, 120))
            self.ventana.blit(jugador2, (470, 180))
            self.ventana.blit(jugador3, (470, 240))
            self.ventana.blit(jugador4, (470, 300))
            self.ventana.blit(jugador5, (470, 360))
            self.ventana.blit(jugador6, (470, 420))
            self.ventana.blit(jugador7, (470, 480))
            self.ventana.blit(jugador8, (470, 540))
            self.ventana.blit(jugador9, (470, 600))
            self.ventana.blit(jugador10, (470, 660))
            pts1= self.font.render(str(self.Top10[10]), True, 'white')
            pts2= self.font.render(str(self.Top10[11]), True, 'white')
            pts3= self.font.render(str(self.Top10[12]), True, 'white')
            pts4= self.font.render(str(self.Top10[13]), True, 'white')
            pts5= self.font.render(str(self.Top10[14]), True, 'white')
            pts6= self.font.render(str(self.Top10[15]), True, 'white')
            pts7= self.font.render(str(self.Top10[16]), True, 'white')
            pts8= self.font.render(str(self.Top10[17]), True, 'white')
            pts9= self.font.render(str(self.Top10[18]), True, 'white')
            pts10= self.font.render(str(self.Top10[19]), True, 'white')
            self.ventana.blit(pts1, (670, 120))
            self.ventana.blit(pts2, (670, 180))
            self.ventana.blit(pts3, (670, 240))
            self.ventana.blit(pts4, (670, 300))
            self.ventana.blit(pts5, (670, 360))
            self.ventana.blit(pts6, (670, 420))
            self.ventana.blit(pts7, (670, 480))
            self.ventana.blit(pts8, (670, 540))
            self.ventana.blit(pts9, (670, 600))
            self.ventana.blit(pts10, (670, 660))
        if self.Escena == "MenuPrincipal":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupMenu.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
        if self.Escena == "SelectorPartida":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupSelecPartida.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
        if self.Escena == "RegistraNombre":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupRegistroNombre.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
            txt_surface = self.font.render(self.NombreJugador, True, self.color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            self.CuadroTexto.w = width
            # Blit the text.
            self.ventana.blit(txt_surface, (self.CuadroTexto.x+5, self.CuadroTexto.y+5))
            pygame.draw.rect(self.ventana, self.color, self.CuadroTexto, 2)
        if self.Escena == "SelectorNivel":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupSelecNivel.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
        
        if self.Escena == "Nivel1":
            self.ventana.blit(Imagen.ImgFondoNivel1, [0,0])
        if self.Escena == "Nivel2":
            self.ventana.blit(Imagen.ImgFondoNivel2, [0,0])
        if self.Escena == "Nivel3":
            self.ventana.blit(Imagen.ImgFondoNivel3, [0,0])
        if self.Escena == "Nivel4":
            self.ventana.blit(Imagen.ImgFondoNivel4, [0,0])
        if self.Escena == "Nivel5":
            self.ventana.blit(Imagen.ImgFondoNivel5, [0,0])
        if self.Escena == "Nivel6":
            self.ventana.blit(Imagen.ImgFondoNivel6, [0,0])
        if self.Escena == "Nivel7":
            self.ventana.blit(Imagen.ImgFondoNivel7, [0,0])
        if self.Escena == "Nivel8":
            self.ventana.blit(Imagen.ImgFondoNivel8, [0,0])
        if self.Escena == "Nivel9":
            self.ventana.blit(Imagen.ImgFondoNivel9, [0,0])
        if self.Escena == "Nivel10":
            self.ventana.blit(Imagen.ImgFondoNivel10, [0,0])
        if self.Escena == "GameOver":
            self.ventana.blit(Imagen.ImgFondoMenu, [0,0])
            Imagen.ImgGroupGameOver.draw(self.ventana)
            self.LblPuntos = self.font2.render(str(self.Puntos), True, 'white')
            self.LblVidas = self.font2.render('0', True, 'white')
            self.ventana.blit(self.LblPuntos, (550, 257))
            self.ventana.blit(self.LblVidas, (550, 325))


    def CalcualarSigVerticePacMan(self):
        if self.DireccionPacman == "arriba":
            for i in reversed(range(self.FilaPacMan)):
                if self.MatrizVertice[i][self.ColPacMan] != " " and self.MatrizVertice[i][self.ColPacMan] != "#":
                    self.SigVerticePacMan = self.MatrizVertice[i][self.ColPacMan]
                    return True
        elif self.DireccionPacman == "abajo":
            for i in range(self.FilaPacMan+1,20):
                if self.MatrizVertice[i][self.ColPacMan] != " " and self.MatrizVertice[i][self.ColPacMan] != "#":
                    self.SigVerticePacMan = self.MatrizVertice[i][self.ColPacMan]
                    return True

        elif self.DireccionPacman == "derecha":
            for i in range(self.ColPacMan+1,20):
                if self.MatrizVertice[self.FilaPacMan][i] != " " and self.MatrizVertice[self.FilaPacMan][i] != "#":
                    self.SigVerticePacMan = self.MatrizVertice[self.FilaPacMan][i]
                    return True

        elif self.DireccionPacman == "izquierda":
            for i in reversed(range(self.ColPacMan)):
                if self.MatrizVertice[self.FilaPacMan][i] != " " and self.MatrizVertice[self.FilaPacMan][i] != "#":
                    self.SigVerticePacMan = self.MatrizVertice[self.FilaPacMan][i]
                    return True
        self.SigVerticePacMan = self.UltimoVerticePacMan
        return False        
     
    def MovimientoBlinky(self):
        self.CargandoBlinky = True

        if self.ColBlinky == 10 and self.FilaBlinky == 9:
            self.BlinkyMuerto = False

        if self.RecorridoBlinky != None:
            if len(self.RecorridoBlinky) < 14 and self.ConteoActivo:
                self.UltimoVerticePacMan = str(random.randint(1, len(self.GrafoNivel.nodes)))
        
        Aux = ""
        if self.BlinkyMuerto == True:
            Aux = self.MatrizVertice[9][10]
            if self.ContCasillasBlinky == 0:
                self.AlgoritmoBlinky = "Dijsktra"
        else:
            Aux = self.UltimoVerticePacMan
            if self.ContCasillasBlinky == 0:
                self.AlgoritmoBlinky = self.AlgoritmosFantasmas[0]

        if self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != Aux or self.VerticeBlinky != Aux:
            if self.RecorridoBlinky == None and self.AlgoritmosFantasmas[0] == "Floyd" or len(self.RecorridoBlinky) == 0 and self.VerticeBlinky != '':
                self.RecorridoBlinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[0],self.GrafoNivel,self.VerticeBlinky,Aux,self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoBlinky != None and len(self.RecorridoBlinky)!=0: 
                if self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'derecha' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'derecha':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,Aux,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'izquierda' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'izquierda':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,Aux,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'abajo' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'abajo':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,Aux,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'arriba' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'arriba':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,Aux,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)
        
        self.CargandoBlinky = False

    def MovimientoPinky(self,RecorridoIgual):
        self.CargandoPinky = True

        if self.ColPinky == 10 and self.FilaPinky == 9:
            self.PinkyMuerto = False

        if self.RecorridoPinky != None:
            if len(self.RecorridoPinky) < 14 and self.ConteoActivo:
                self.SigVerticePacMan = str(random.randint(1, len(self.GrafoNivel.nodes)))

        Aux = ""
        if self.PinkyMuerto == True:
            if self.MatrizVertice[self.FilaPinky][self.ColPinky] != " " and  self.MatrizVertice[self.FilaPinky][self.ColPinky] != "#" and self.ContCasillasPinky == 0:
                self.AlgoritmoPinky = "Dijsktra"
                if self.RecorridoPinky != None:
                    self.RecorridoPinky.clear()
            
            Aux = self.MatrizVertice[9][10]
        else:
            Aux = self.SigVerticePacMan
            if self.AlgoritmoPinky != self.AlgoritmosFantasmas[1] and self.ContCasillasPinky == 0:
                self.AlgoritmoPinky = self.AlgoritmosFantasmas[1]
                if self.RecorridoPinky != None:
                    self.RecorridoPinky.clear()

        if self.AlgoritmoPinky == "Floyd" and self.VerticePinky != Aux or self.VerticePinky != Aux:
            if self.RecorridoPinky == None and self.AlgoritmoPinky == "Floyd" or self.RecorridoPinky != None and len(self.RecorridoPinky) == 0 and self.VerticePinky != '':
                self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmoPinky,self.GrafoNivel,self.VerticePinky,Aux,self.MatrizDistancias,self.MatrizCaminos)
            
            if not self.PinkyMuerto and RecorridoIgual == True and not self.ConteoActivo:
                self.DeterminaRecorridosIguales()
                RecorridoIgual = False

            if self.RecorridoPinky != None and len(self.RecorridoPinky) != 0: 
                if self.AlgoritmoPinky == "Dijsktra" and self.RecorridoPinky[0] == 'derecha' or self.AlgoritmoPinky == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'derecha':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmoPinky,self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,Aux,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoPinky == "Dijsktra" and self.RecorridoPinky[0] == 'izquierda' or self.AlgoritmoPinky == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'izquierda':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmoPinky,self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,Aux,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoPinky == "Dijsktra" and self.RecorridoPinky[0] == 'abajo' or self.AlgoritmoPinky == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'abajo':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmoPinky,self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,Aux,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoPinky == "Dijsktra" and self.RecorridoPinky[0] == 'arriba' or self.AlgoritmoPinky == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'arriba':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmoPinky,self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,Aux,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)
        
        self.CargandoPinky = False

    def MovimientoInky(self):
        self.CargandoInky = True

        if self.ColInky == 10 and self.FilaInky == 9:
            self.InkyMuerto = False
        
        Aux = ""
        if self.InkyMuerto == True:
            Aux = self.MatrizVertice[9][10]
        else:
            Aux = self.posicion

        if self.VerticeInky != self.UltimoVerticePacMan:
            if self.VerticeInky==self.posicion:
                self.numRand=random.randint(1, len(self.GrafoNivel.nodes))
                self.InkyLista=[str(self.numRand),self.VerticeBlinky,self.VerticePinky,self.VerticeClyde,self.UltimoVerticePacMan]
                self.rand=random.randint(0, 4)
                self.posicion= self.InkyLista[self.rand]
            if len(self.RecorridoInky) == 0:
                self.RecorridoInky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[2],self.GrafoNivel,self.VerticeInky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoInky[0] == 'derecha':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,Aux,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'izquierda':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,Aux,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'abajo':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,Aux,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'arriba':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,Aux,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)
        
        self.CargandoInky = False

    def MovimientoClyde(self):
        self.CargandoClyde = True

        Destino = random.randint(1, len(self.GrafoNivel.nodes))

        if self.ColClyde == 10 and self.FilaClyde == 9:
            self.ClydeMuerto = False
        
        Aux = ""
        if self.ClydeMuerto == True:
            if self.MatrizVertice[self.FilaClyde][self.ColClyde] != " " and  self.MatrizVertice[self.FilaClyde][self.ColClyde] != "#" and self.ContCasillasClyde == 0:
                if self.AlgoritmoClyde == "Floyd":
                    self.RecorridoClyde.clear()
                self.AlgoritmoClyde = "Dijsktra"
            if self.AlgoritmoClyde == "Dijsktra":
                Aux = self.MatrizVertice[9][10]     
            
                
        else:
            Aux = str(Destino)
            if self.ContCasillasClyde == 0:
                self.AlgoritmoClyde = self.AlgoritmosFantasmas[3]

        if self.AlgoritmoClyde == "Floyd" or self.VerticeClyde != Aux:
            if self.RecorridoClyde == None and self.AlgoritmoClyde == "Floyd" or len(self.RecorridoClyde) == 0 and self.VerticeClyde != '':
                self.RecorridoClyde = MovPacMan.DeterminaAlgoritmo(self.AlgoritmoClyde,self.GrafoNivel,self.VerticeClyde,str(Destino),self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoClyde != None or self.AlgoritmoClyde == "Dijsktra": 
                icono = ""
                if self.ConteoActivo and self.ClydeMuerto or not self.ConteoActivo and self.ClydeMuerto:
                    icono = "regreso"
                elif self.ConteoActivo and not self.ClydeMuerto:
                    icono = "peligro"
                elif self.AlgoritmoClyde == "Floyd":
                    icono = self.RecorridoClyde[-1]
                else:
                    icono = self.RecorridoClyde[0]
                if self.AlgoritmoClyde == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'derecha' or self.AlgoritmoClyde == "Dijsktra" and self.RecorridoClyde[0] == 'derecha':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmoClyde,self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,Aux,self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,1,0,icono,self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoClyde == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'izquierda' or self.AlgoritmoClyde == "Dijsktra" and self.RecorridoClyde[0] == 'izquierda':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmoClyde,self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,Aux,self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,-1,0,icono,self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoClyde == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'abajo' or self.AlgoritmoClyde == "Dijsktra" and self.RecorridoClyde[0] == 'abajo':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmoClyde,self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,Aux,self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,0,1,icono,self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmoClyde == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'arriba' or self.AlgoritmoClyde == "Dijsktra" and self.RecorridoClyde[0] == 'arriba':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmoClyde,self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,Aux,self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,0,-1,icono,self.MatrizDistancias,self.MatrizCaminos)
        
        self.CargandoClyde = False

    def Movimientos(self):
        if self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
            if self.PoderActivo == True and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " " and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " " and self.ContCasillas == 0:
                self.PoderActivo = False
                self.VelocidadPacMan = 2
                self.LimiteCasillasPacMan = 17
                ThreadContPoder = threading.Thread(target=self.ContadorPoder,)
                ThreadContPoder.start()
            if self.PoderFinalizado == True and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " " and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " " and self.ContCasillas == 0:
                self.PoderFinalizado = False
                self.VelocidadPacMan = 1
                self.LimiteCasillasPacMan = 34
            
            if not self.ConteoActivo:
                self.ComprobarDerrota()
            else:
                self.ComerFantasma()
                if self.PoderActivo == False and self.VelocidadPacMan == 1:
                    self.CompruebaPoder()

            if self.Escena=='Nivel10':
                self.NumNivel='10'
            else:
                self.NumNivel = self.Escena[5]
            self.MatrizTunel = self.niveles[int(self.NumNivel)-1]
            if self.Permitido == True and MovPacMan.VerificaMovimiento(self.DireccionPacman2,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                self.DireccionPacman = self.DireccionPacman2
                self.DireccionPacman2 = ""
                self.Permitido = False
            #PARA QUE PACMAN PASE POR LOS TUNELES
            if self.MatrizTunel[self.FilaPacMan][0]=='$':
                self.PosXPacMan=683
                self.ColPacMan=20
                self.MatrizTunel[self.FilaPacMan][0]=' '
                self.MatrizTunel[self.FilaPacMan][self.ColPacMan]=='$'
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
            elif self.MatrizTunel[self.FilaPacMan][20]=='$':
                self.PosXPacMan=0
                self.ColPacMan=0
                self.MatrizTunel[self.FilaPacMan][20]=' '
                self.MatrizTunel[self.FilaPacMan][self.ColPacMan]=='$'
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
            #PARA CUANDO PIERDE
            if self.Vidas==0:
                self.DireccionPacman = "inicio"
                self.PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                self.PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                self.ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
                self.datosJugador[0]=self.NombreJugador
                self.datosJugador[1]=self.Puntos
                self.datosJugador[2]=self.Vidas
                self.datosJugador[3]=self.NivelesDesbloqueados
                self.datosJugador[4]=self.PuntajeSinPerder
                RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                self.LimpiarNivel()
                self.Escena='GameOver'
            #PARA SACAR EL PUNTAJE MAYOR SIN HABER PERDIDO VIDAS
            if self.Vidas==6:
                self.PuntajeSinPerder= self.Puntos
            if self.DireccionPacman == "derecha" and self.Victoria == False:
                if MovPacMan.VerificaMovimiento("derecha",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == self.LimiteCasillasPacMan:
                        if self.MatrizTunel[self.FilaPacMan][self.ColPacMan+1]=='.':
                            self.Puntos+=10
                            self.determinaNivelPuntaje()
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.ColPacMan+=1
                        self.ContCasillas = 0
                    else:
                        self.PosXPacMan = self.PosXPacMan+self.VelocidadPacMan
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "izquierda" and self.Victoria == False:
                if MovPacMan.VerificaMovimiento("izquierda",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == self.LimiteCasillasPacMan:
                        if self.MatrizTunel[self.FilaPacMan][self.ColPacMan-1]=='.':
                            self.Puntos+=10
                            self.determinaNivelPuntaje()
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.ColPacMan-=1
                        self.ContCasillas = 0
                    else:
                        self.PosXPacMan = self.PosXPacMan-self.VelocidadPacMan
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "arriba" and self.Victoria == False:
                if MovPacMan.VerificaMovimiento("arriba",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == self.LimiteCasillasPacMan:
                        if self.MatrizTunel[self.FilaPacMan-1][self.ColPacMan]=='.':
                            self.Puntos+=10
                            self.determinaNivelPuntaje()
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.FilaPacMan-=1
                        self.ContCasillas = 0
                    else:
                        self.PosYPacMan = self.PosYPacMan-self.VelocidadPacMan
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "abajo" and self.Victoria == False:
                if MovPacMan.VerificaMovimiento("abajo",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == self.LimiteCasillasPacMan:
                        if self.MatrizTunel[self.FilaPacMan+1][self.ColPacMan]=='.':
                            self.Puntos+=10
                            self.determinaNivelPuntaje()
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.FilaPacMan+=1
                        self.ContCasillas = 0
                        
                    else:
                        self.PosYPacMan = self.PosYPacMan+self.VelocidadPacMan
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            #Actualiza el ultimo vertice que ha visitado el PacMan en el tablero    
            if self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != "#" and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " " and not self.ConteoActivo:
                self.UltimoVerticePacMan = self.MatrizVertice[self.FilaPacMan][self.ColPacMan]
                self.CalcualarSigVerticePacMan()

            #INICIA EL CONTEO PARA COMERSE A LOS FANTASMAS DESPUES DE CONSUMIR UN POWER PELLET
            if self.ConteoActivo == False and self.PoderPellet == True:
                #print("inicio conteo")
                self.ConteoActivo = True
                self.PoderPellet = False
                self.SigVerticePacMan = str(random.randint(1, len(self.GrafoNivel.nodes)))
                self.UltimoVerticePacMan = str(random.randint(1, len(self.GrafoNivel.nodes)))
                x = threading.Thread(target=self.contador,)
                x.start() 
            if self.ConteoActivo == True and self.PoderPellet == True:
                self.PoderPellet = False
                self.cont = 0


            Imagen.mover.draw(self.ventana)
            Imagen.mover.update(0.1,self.DireccionPacman)

            Imagen.ImgGroupNivel.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
            Imagen.ImgGroupPuntos.draw(self.ventana)
            Imagen.ImgGroupFantasmas.draw(self.ventana)
            self.TituloJugador = self.font.render("Jugador: ", True, 'white')
            self.ventana.blit(self.TituloJugador, (800, 20))
            self.LblJugador = self.font.render(self.NombreJugador, True, 'white')
            self.ventana.blit(self.LblJugador, (930, 20))

            self.TituloPuntos = self.font.render("Puntos: ", True, 'white')
            self.ventana.blit(self.TituloPuntos, (800, 60))
            self.LblPuntos = self.font.render(str(self.Puntos), True, 'white')
            self.ventana.blit(self.LblPuntos, (920, 60))

            self.TituloVidas = self.font.render("Vidas: ", True, 'white')
            self.ventana.blit(self.TituloVidas, (800, 100))
            self.LblVidas = self.font.render(str(self.Vidas), True, 'white')
            self.ventana.blit(self.LblVidas, (900, 100))

            if self.PoderAdquirido == True:
                Imagen.btnPoderG.draw(self.ventana)

            #Movimiento del Fantasma
            if self.Victoria == False and self.Vidas != 0:
                RecorridoIgual = False
                
                if self.ColPinky == self.ColBlinky and self.FilaPinky == self.FilaBlinky and self.ContCasillasPinky == 0 and self.ContCasillasBlinky == 0:
                    RecorridoIgual = True
                if self.ColPinky == self.ColBlinky and self.FilaPinky == self.FilaBlinky and self.ContCasillasPinky == 33 and self.ContCasillasBlinky == 0:
                    RecorridoIgual = True
                if self.ColPinky == self.ColBlinky and self.FilaPinky == self.FilaBlinky and self.ContCasillasPinky == 0 and self.ContCasillasBlinky == 33:
                    RecorridoIgual = True
                if self.RecorridoPinky == self.RecorridoBlinky and self.ContCasillasPinky == 0 and self.ContCasillasBlinky == 0:
                    RecorridoIgual = True

                #Blinky
                if not self.CargandoBlinky:
                    ThreadBlinky = threading.Thread(target=self.MovimientoBlinky,)
                    ThreadBlinky.start()
                #Pinky
                if not self.CargandoPinky:
                    ThreadPinky = threading.Thread(target=self.MovimientoPinky, args=(RecorridoIgual,))
                    ThreadPinky.start()
                #Inky
                if not self.CargandoInky:
                    ThreadInky = threading.Thread(target=self.MovimientoInky,)
                    ThreadInky.start()
                #Clyde
                if not self.CargandoClyde:
                    ThreadClyde = threading.Thread(target=self.MovimientoClyde,)
                    ThreadClyde.start()

                self.EvaluarVictoria()

            if self.Victoria == True:
                Imagen.ImgGroupVictoria.draw(self.ventana)

        self.peligroFantasmas()

    def peligroFantasmas(self):
        if self.ConteoActivo:
            Imagen.ActualizaFantasma("Inky",Imagen.ImgInky.rect.x,Imagen.ImgInky.rect.y,"peligro")
            Imagen.ActualizaFantasma("Pinky",Imagen.ImgPinky.rect.x,Imagen.ImgPinky.rect.y,"peligro")
            Imagen.ActualizaFantasma("Clyde",Imagen.ImgClyde.rect.x,Imagen.ImgClyde.rect.y,"peligro")
            Imagen.ActualizaFantasma("Blinky",Imagen.ImgBlinky.rect.x,Imagen.ImgBlinky.rect.y,"peligro")
        if self.PinkyMuerto == True:
            Imagen.ActualizaFantasma("Pinky",Imagen.ImgPinky.rect.x,Imagen.ImgPinky.rect.y,"regreso")
        if self.BlinkyMuerto == True:
            Imagen.ActualizaFantasma("Blinky",Imagen.ImgBlinky.rect.x,Imagen.ImgBlinky.rect.y,"regreso")
        if self.InkyMuerto == True:
            Imagen.ActualizaFantasma("Inky",Imagen.ImgInky.rect.x,Imagen.ImgInky.rect.y,"regreso")
        if self.ClydeMuerto == True:
            Imagen.ActualizaFantasma("Clyde",Imagen.ImgClyde.rect.x,Imagen.ImgClyde.rect.y,"regreso")
            


        
        

#Inicializa el programa
game = Juego()   
game.__init__()
game.CargaEstadisticas()
game.tiempoBandera=True
Thread= threading.Thread(target=game.tiempoTranscurrido,)
Thread.start()

while True:

    game.LimpiarPantalla()

    game.Eventos()

    game.CargarGraficaNivel()

    game.Movimientos()

    pygame.display.flip() 
