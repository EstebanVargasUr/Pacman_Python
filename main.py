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
        self.datosJugador= list()
        self.MatrizVertice = []
        self.MatrizTunel = []
        self.GrafoNivel = GR.Graph() 
        self.Escena = "MenuPrincipal"
        self.Puntos = 0
        self.cont = 0
        self.PoderPellet = False
        self.ConteoActivo = False
        self.Vidas = 0

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
        
        #Pinky
        self.RecorridoPinky = []
        self.ContCasillasPinky = 0
        self.VerticePinky = ''
        self.FilaPinky = 9
        self.ColPinky = 12

        #Clyde
        self.RecorridoClyde = []
        self.ContCasillasClyde = 0
        self.VerticeClyde = ''
        self.FilaClyde = 11
        self.ColClyde = 12

        #Inky
        self.RecorridoInky = []
        self.ContCasillasInky = 0
        self.VerticeInky = ''
        self.FilaInky = 11
        self.ColInky = 8

        self.numRand=random.randint(1, 60)
        self.posicion= str(self.numRand)


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
        Imagen.ActualizaFantasma("Blinky",277,311,"abajo")
        #Pinky
        self.RecorridoPinky = []
        self.ContCasillasPinky = 0
        self.VerticePinky = ''
        self.FilaPinky = 9
        self.ColPinky = 12
        Imagen.ActualizaFantasma("Pinky",413,311,"abajo")
        #Inky
        self.RecorridoInky = []
        self.ContCasillasInky = 0
        self.VerticeInky = ''
        self.FilaInky = 11
        self.ColInky = 8
        Imagen.ActualizaFantasma("Inky",277,379,"abajo")
        #Clyde
        self.RecorridoClyde = []
        self.ContCasillasClyde = 0
        self.VerticeClyde = ''
        self.FilaClyde = 11
        self.ColClyde = 12
        Imagen.ActualizaFantasma("Clyde",413,379,"abajo")

    #CUENTA EL TIEMPO DE 10 SEGUNDOS DE INMUNIDAD AL COMERSE UN POWER PELLET
    def contador(self):
        self.cont = 0
        while self.cont < 10: 
            time.sleep(1)
            print(self.cont)
            self.cont +=1
        self.ConteoActivo = False

    def LimpiarNivel(self):
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

            print(self.AlgoritmosFantasmas)

            if "Floyd" in self.AlgoritmosFantasmas:
                self.MatrizDistancias,self.MatrizCaminos = GR.floyd_warshall(self.GrafoNivel)

        #Blinky
        self.VerticeBlinky = self.MatrizVertice[9][8]
        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.UltimoVerticePacMan = self.MatrizVertice[13][i]
                break
        self.RecorridoBlinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[0],self.GrafoNivel,self.VerticeBlinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)

        #Pinky
        self.VerticePinky = self.MatrizVertice[9][12]
        for i in range(10, 20):
            if self.MatrizVertice[13][i] != " " and self.MatrizVertice[13][i] != "#":
                self.SigVerticePacMan = self.MatrizVertice[13][i]
                break
        self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[1],self.GrafoNivel,self.VerticePinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)

        #Inky
        self.VerticeInky = self.MatrizVertice[11][8]
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


    #VERIFICA SI UN FANTASMA TOCA A PACMAN Y LE RESTA UNA VIDA
    def ComprobarDerrota(self):
        if self.FilaBlinky == self.FilaPacMan and self.ColBlinky == self.ColPacMan:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaClyde == self.FilaPacMan and self.ColClyde == self.ColPacMan:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaInky == self.FilaPacMan and self.ColInky == self.ColPacMan:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()
        elif self.FilaPinky == self.FilaPacMan and self.ColPinky == self.ColPacMan:
            self.niveles[int(self.NumNivel)-1][self.FilaPacMan][self.ColPacMan] = " "
            self.niveles[int(self.NumNivel)-1][13][10] = "$"
            self.Vidas=self.Vidas-1
            self.LimpiarNivel()
            self.IniciarFantasmas()


    def DeterminaRecorridosIguales(self):
        if len(self.RecorridoPinky) == 0:
            self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[1],self.GrafoNivel,self.VerticePinky,self.UltimoVerticePacMan)
        else:
            for i in range(20):
                for j in range(20):
                    if self.MatrizVertice[i][j] == self.VerticePinky:

                        for h in range(j+1,20):
                            if self.MatrizVertice[i][h] == "#":
                                break
                            if self.MatrizVertice[i][h] != " " and self.MatrizVertice[i][h] != "#":
                                self.VerticePinky = self.MatrizVertice[i][h]
                                self.RecorridoPinky[0] = 'derecha'
                                return self.VerticePinky
                        for h in reversed(range(j-1)):
                            if self.MatrizVertice[i][h] == "#":
                                break
                            if self.MatrizVertice[i][h] != " " and self.MatrizVertice[i][h] != "#":
                                self.VerticePinky = self.MatrizVertice[i][h]
                                self.RecorridoPinky[0] = 'izquierda'
                                return self.VerticePinky
                        for h in range(i+1,20):
                            if self.MatrizVertice[h][j] == "#":
                                break
                            elif self.MatrizVertice[h][j] != " " and self.MatrizVertice[h][j] != "#":
                                self.VerticePinky = self.MatrizVertice[h][j]
                                self.RecorridoPinky[0] = 'abajo'
                                return self.VerticePinky
                        for h in reversed(range(i-1)):
                            if self.MatrizVertice[h][j] == "#":
                                break
                            elif self.MatrizVertice[h][j] != " " and self.MatrizVertice[h][j] != "#":
                                self.VerticePinky = self.MatrizVertice[h][j]
                                self.RecorridoPinky[0] = 'arriba'
                                return self.VerticePinky
                        
    def Eventos(self):
        for event in pygame.event.get(): #EVENTOS
            if event.type == pygame.QUIT: #CIERRA VENTANA
                if len(self.niveles)!=0:
                    for i in range(10):
                        RW.fileWrite(self.niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                    self.datosJugador[1]=self.Puntos
                    self.datosJugador[2]=self.Vidas
                    RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
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
                                RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                            sys.exit()
                    elif self.Escena == "SelectorPartida":
                        if Imagen.btnNuevaPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "RegistraNombre"
                            self.NombreJugador=""
                            self.Puntos=0
                            self.Vidas=6
                            self.niveles.clear()
                            for i in range(10):
                                self.niveles.append(Nivel.laberinto(10,10))
                                RW.fileWrite(self.niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                                
                        if Imagen.btnCargarPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            for i in range(10):
                                self.niveles.append(RW.fileRead("CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt"))
                            self.datosJugador=RW.fileRead("CreaNivel/DatosJugador/jugador.txt")
                            self.NombreJugador= self.datosJugador[0]
                            self.Puntos= int(self.datosJugador[1])
                            self.Vidas= int(self.datosJugador[2])
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
                        if Imagen.btnMedio.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Dificultad = "Medio"
                        if Imagen.btnDificil.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Dificultad = "Dificil"
                    elif self.Escena == "SelectorNivel":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "MenuPrincipal"
                        if Imagen.btnSelecNiv1.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel1"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(1,self.niveles)
                            Imagen.CargaNivel(1,self.niveles)
                            Imagen.CargaPuntos(1,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(1,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[0])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv2.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel2"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(2,self.niveles)
                            Imagen.CargaNivel(2,self.niveles)
                            Imagen.CargaPuntos(2,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(2,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[1])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv3.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel3"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(3,self.niveles)
                            Imagen.CargaNivel(3,self.niveles)
                            Imagen.CargaPuntos(3,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(3,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[2])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv4.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel4"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(4,self.niveles)
                            Imagen.CargaNivel(4,self.niveles)
                            Imagen.CargaPuntos(4,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(4,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[3])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv5.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel5"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(5,self.niveles)
                            Imagen.CargaNivel(5,self.niveles)
                            Imagen.CargaPuntos(5,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(5,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[4])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv6.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel6"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(6,self.niveles)
                            Imagen.CargaNivel(6,self.niveles)
                            Imagen.CargaPuntos(6,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(6,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[5])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv7.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel7"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(7,self.niveles)
                            Imagen.CargaNivel(7,self.niveles)
                            Imagen.CargaPuntos(7,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(7,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[6])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv8.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel8"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(8,self.niveles)
                            Imagen.CargaNivel(8,self.niveles)
                            Imagen.CargaPuntos(8,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(8,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[7])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv9.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel9"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(9,self.niveles)
                            Imagen.CargaNivel(9,self.niveles)
                            Imagen.CargaPuntos(9,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(9,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[8])
                            self.ClickBtnNivel = True
                        if Imagen.btnSelecNiv10.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.Escena = "Nivel10"
                            self.FilaPacMan, self.ColPacMan =Imagen.EncontrarPacMan(10,self.niveles)
                            Imagen.CargaNivel(10,self.niveles)
                            Imagen.CargaPuntos(10,self.niveles)
                            self.Jugador = Imagen.ColocaPacMan(10,self.niveles)
                            self.NivelSeleccionado = True
                            self.MatrizVertice,self.GrafoNivel =  GR.CreaGrafo(self.niveles[9])
                            self.ClickBtnNivel = True
                    elif self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
                        if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                            self.DireccionPacman = "inicio"
                            self.PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                            self.PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                            self.ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
                            self.LimpiarNivel()
                            self.Escena = "SelectorNivel"
            if event.type == pygame.KEYDOWN: # EVENTOS DE TECLADO
                if self.Escena == "RegistraNombre":
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.Escena = "SelectorNivel"
                            self.datosJugador.append(str(self.NombreJugador))
                            self.datosJugador.append(self.Puntos)
                            self.datosJugador.append(self.Vidas)
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
                if self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
                    if event.key == pygame.K_ESCAPE:
                        self.LimpiarNivel()
                        self.Escena = "SelectorNivel"
                        self.DireccionPacman = "inicio"
                        self.FilaPacMan = 13 # FILA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
                        self.ColPacMan = 10  # COLUMNA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
                        self.PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                        self.PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                        self.ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
                    if self.Escena=='Nivel10':
                        self.NumNivel='10'
                    else:
                        self.NumNivel = self.Escena[5]
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if MovPacMan.VerificaMovimiento("arriba",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= 17:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=2
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=2
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=2
                            if self.DireccionPacman != "arriba":
                                self.DireccionPacman = "arriba"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "arriba"
                            self.Permitido = True
                        
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if MovPacMan.VerificaMovimiento("abajo",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= 17:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=2
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=2
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=2
                            if self.DireccionPacman != "abajo":
                                self.DireccionPacman = "abajo"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "abajo"
                            self.Permitido = True

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                        if MovPacMan.VerificaMovimiento("derecha",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= 17:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=2
                                    if self.DireccionPacman == "izquierda":
                                        self.PosXPacMan +=2
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=2
                            if self.DireccionPacman != "derecha":
                                self.DireccionPacman = "derecha"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "derecha"
                            self.Permitido = True
                        
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if MovPacMan.VerificaMovimiento("izquierda",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan): 
                            if self.ContCasillas <= 17:
                                for i in range(self.ContCasillas):
                                    if self.DireccionPacman == "derecha":
                                        self.PosXPacMan -=2
                                    if self.DireccionPacman == "arriba":
                                        self.PosYPacMan +=2
                                    if self.DireccionPacman == "abajo":
                                        self.PosYPacMan -=2
                            if self.DireccionPacman != "izquierda":
                                self.DireccionPacman = "izquierda"
                                self.ContCasillas = 0
                        else:
                            self.DireccionPacman2 = "izquierda"
                            self.Permitido = True        



    def CargarGraficaNivel(self):
        if self.ClickBtnNivel == True:
            self.IniciarFantasmas()

        if self.Escena == "Ajustes":
            self.ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
            Imagen.ImgGroupAjustes.draw(self.ventana) # DIBUJA TODOS LOS SPRITES
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
        if self.AlgoritmosFantasmas[0] == "Floyd" or self.VerticeBlinky != self.SigVerticePacMan:
            if self.RecorridoBlinky == None and self.AlgoritmosFantasmas[0] == "Floyd" or len(self.RecorridoBlinky) == 0 and self.VerticeBlinky != '':
                self.RecorridoBlinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[0],self.GrafoNivel,self.VerticeBlinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoBlinky != None: 
                if self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'derecha' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'derecha':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'izquierda' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'izquierda':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'abajo' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'abajo':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[0] == "Dijsktra" and self.RecorridoBlinky[0] == 'arriba' or self.AlgoritmosFantasmas[0] == "Floyd" and self.VerticeBlinky != '' and self.RecorridoBlinky[len(self.RecorridoBlinky)-1] == 'arriba':
                    self.RecorridoBlinky, self.ContCasillasBlinky , self.FilaBlinky , self.ColBlinky , self.VerticeBlinky = MovPacMan.MovimientoFantasma(Imagen.ImgBlinky,"Blinky",self.AlgoritmosFantasmas[0],self.ContCasillasBlinky,self.FilaBlinky,self.ColBlinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticeBlinky,self.GrafoNivel,self.RecorridoBlinky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)

    def MovimientoPinky(self,RecorridoIgual):
        if self.AlgoritmosFantasmas[1] == "Floyd" or self.VerticePinky != self.SigVerticePacMan:
            if self.RecorridoPinky == None and self.AlgoritmosFantasmas[1] == "Floyd" or len(self.RecorridoPinky) == 0 and self.VerticePinky != '':
                self.RecorridoPinky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[1],self.GrafoNivel,self.VerticePinky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)
            if RecorridoIgual == True:
                self.DeterminaRecorridosIguales()
                RecorridoIgual = False
            if self.RecorridoPinky != None: 
                if self.AlgoritmosFantasmas[1] == "Dijsktra" and self.RecorridoPinky[0] == 'derecha' or self.AlgoritmosFantasmas[1] == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'derecha':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmosFantasmas[1],self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[1] == "Dijsktra" and self.RecorridoPinky[0] == 'izquierda' or self.AlgoritmosFantasmas[1] == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'izquierda':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmosFantasmas[1],self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[1] == "Dijsktra" and self.RecorridoPinky[0] == 'abajo' or self.AlgoritmosFantasmas[1] == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'abajo':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmosFantasmas[1],self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[1] == "Dijsktra" and self.RecorridoPinky[0] == 'arriba' or self.AlgoritmosFantasmas[1] == "Floyd" and self.VerticePinky != '' and self.RecorridoPinky[len(self.RecorridoPinky)-1] == 'arriba':
                    self.RecorridoPinky, self.ContCasillasPinky , self.FilaPinky , self.ColPinky , self.VerticePinky = MovPacMan.MovimientoFantasma(Imagen.ImgPinky,"Pinky",self.AlgoritmosFantasmas[1],self.ContCasillasPinky,self.FilaPinky,self.ColPinky,self.MatrizVertice,self.UltimoVerticePacMan,self.VerticePinky,self.GrafoNivel,self.RecorridoPinky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)
    
    def MovimientoInky(self):
        if self.VerticeInky != self.UltimoVerticePacMan:
            if self.VerticeInky==self.posicion:
                self.numRand=random.randint(0, 60)
                self.InkyLista=[str(self.numRand),self.VerticeBlinky,self.VerticePinky,self.VerticeClyde,self.UltimoVerticePacMan]
                self.rand=random.randint(0, 4)
                self.posicion= self.InkyLista[self.rand]
            if len(self.RecorridoInky) == 0:
                self.RecorridoInky = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[2],self.GrafoNivel,self.VerticeInky,self.UltimoVerticePacMan,self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoInky[0] == 'derecha':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,self.posicion,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'izquierda':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,self.posicion,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'abajo':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,self.posicion,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
            elif self.RecorridoInky[0] == 'arriba':
                self.RecorridoInky, self.ContCasillasInky , self.FilaInky , self.ColInky , self.VerticeInky = MovPacMan.MovimientoFantasma(Imagen.ImgInky,"Inky",self.AlgoritmosFantasmas[2],self.ContCasillasInky,self.FilaInky,self.ColInky,self.MatrizVertice,self.posicion,self.VerticeInky,self.GrafoNivel,self.RecorridoInky,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)

    def MovimientoClyde(self):
        if self.AlgoritmosFantasmas[3] == "Floyd" or self.VerticeClyde != self.SigVerticePacMan:
            if self.RecorridoClyde == None and self.AlgoritmosFantasmas[3] == "Floyd" or len(self.RecorridoClyde) == 0 and self.VerticeClyde != '':
                Destino = random.randint(1, len(self.GrafoNivel.nodes))
                self.RecorridoClyde = MovPacMan.DeterminaAlgoritmo(self.AlgoritmosFantasmas[3],self.GrafoNivel,self.VerticeClyde,str(Destino),self.MatrizDistancias,self.MatrizCaminos)
            if self.RecorridoClyde != None or self.AlgoritmosFantasmas[3] == "Dijsktra": 
                Destino = random.randint(1, len(self.GrafoNivel.nodes))
                if self.AlgoritmosFantasmas[3] == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'derecha' or self.AlgoritmosFantasmas[3] == "Dijsktra" and self.RecorridoClyde[0] == 'derecha':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmosFantasmas[3],self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,str(Destino),self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,1,0,"derecha",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[3] == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'izquierda' or self.AlgoritmosFantasmas[3] == "Dijsktra" and self.RecorridoClyde[0] == 'izquierda':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmosFantasmas[3],self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,str(Destino),self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,-1,0,"izquierda",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[3] == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'abajo' or self.AlgoritmosFantasmas[3] == "Dijsktra" and self.RecorridoClyde[0] == 'abajo':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmosFantasmas[3],self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,str(Destino),self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,0,1,"abajo",self.MatrizDistancias,self.MatrizCaminos)
                elif self.AlgoritmosFantasmas[3] == "Floyd" and self.VerticeClyde != '' and self.RecorridoClyde[len(self.RecorridoClyde)-1] == 'arriba' or self.AlgoritmosFantasmas[3] == "Dijsktra" and self.RecorridoClyde[0] == 'arriba':
                    self.RecorridoClyde, self.ContCasillasClyde , self.FilaClyde , self.ColClyde , self.VerticeClyde = MovPacMan.MovimientoFantasma(Imagen.ImgClyde,"Clyde",self.AlgoritmosFantasmas[3],self.ContCasillasClyde,self.FilaClyde,self.ColClyde,self.MatrizVertice,str(Destino),self.VerticeClyde,self.GrafoNivel,self.RecorridoClyde,0,-1,"arriba",self.MatrizDistancias,self.MatrizCaminos)


    def Movimientos(self):
        if self.Escena == "Nivel1" or self.Escena == "Nivel2" or self.Escena == "Nivel3" or self.Escena == "Nivel4" or self.Escena == "Nivel5" or self.Escena == "Nivel6" or self.Escena == "Nivel7" or self.Escena == "Nivel8" or self.Escena == "Nivel9" or self.Escena == "Nivel10":
            if not self.ConteoActivo:
                self.ComprobarDerrota()
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
                RW.fileWrite(self.datosJugador,"CreaNivel/DatosJugador/jugador.txt")
                self.LimpiarNivel()
                self.Escena='GameOver'
            if self.DireccionPacman == "derecha":
                if MovPacMan.VerificaMovimiento("derecha",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == 17:
                        if self.MatrizTunel[self.FilaPacMan][self.ColPacMan+1]=='.':
                            self.Puntos+=10
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.ColPacMan+=1
                        self.ContCasillas = 0
                    else:
                        self.PosXPacMan = self.PosXPacMan+2
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "izquierda":
                if MovPacMan.VerificaMovimiento("izquierda",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == 17:
                        if self.MatrizTunel[self.FilaPacMan][self.ColPacMan-1]=='.':
                            self.Puntos+=10
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.ColPacMan-=1
                        self.ContCasillas = 0
                    else:
                        self.PosXPacMan = self.PosXPacMan-2
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "arriba":
                if MovPacMan.VerificaMovimiento("arriba",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == 17:
                        if self.MatrizTunel[self.FilaPacMan-1][self.ColPacMan]=='.':
                            self.Puntos+=10
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.FilaPacMan-=1
                        self.ContCasillas = 0
                    else:
                        self.PosYPacMan = self.PosYPacMan-2
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            if self.DireccionPacman == "abajo":
                if MovPacMan.VerificaMovimiento("abajo",self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan):
                    if self.ContCasillas == 17:
                        if self.MatrizTunel[self.FilaPacMan+1][self.ColPacMan]=='.':
                            self.Puntos+=10
                        self.PoderPellet = MovPacMan.Movimiento(self.DireccionPacman,self.niveles[int(self.NumNivel)-1],self.FilaPacMan,self.ColPacMan)
                        self.FilaPacMan+=1
                        self.ContCasillas = 0
                        
                    else:
                        self.PosYPacMan = self.PosYPacMan+2
                        self.ContCasillas += 1
                Imagen.ActualizaPacMan(self.Jugador,self.PosXPacMan,self.PosYPacMan)
                Imagen.ActualizaPts(int(self.NumNivel),self.niveles)
            #Actualiza el ultimo vertice que ha visitado el PacMan en el tablero    
            if self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != "#" and self.MatrizVertice[self.FilaPacMan][self.ColPacMan] != " ":
                self.UltimoVerticePacMan = self.MatrizVertice[self.FilaPacMan][self.ColPacMan]
                self.CalcualarSigVerticePacMan()

            #INICIA EL CONTEO PARA COMERSE A LOS FANTASMAS DESPUES DE CONSUMIR UN POWER PELLET
            if self.ConteoActivo == False and self.PoderPellet == True:
                print("inicio conteo")
                self.ConteoActivo = True
                self.PoderPellet = False
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
        RecorridoIgual = False
        #Movimiento del Fantasma
        if self.RecorridoPinky == self.RecorridoBlinky and self.ContCasillasPinky == 0 and self.ContCasillasBlinky == 0:
            RecorridoIgual = True

        #Blinky
        ThreadBlinky = threading.Thread(target=self.MovimientoBlinky)
        ThreadBlinky.start()
        #Pinky
        ThreadPinky = threading.Thread(target=self.MovimientoPinky, args=(RecorridoIgual,))
        ThreadPinky.start()
        #Inky
        ThreadInky = threading.Thread(target=self.MovimientoInky)
        ThreadInky.start()
        #Clyde
        ThreadClyde = threading.Thread(target=self.MovimientoClyde())
        ThreadClyde.start()



        
        

#Inicializa el programa
game = Juego()   
game.__init__()

while True:

    game.LimpiarPantalla()

    game.Eventos()

    game.CargarGraficaNivel()

    game.Movimientos()

    pygame.display.flip() 
