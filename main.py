import pygame, sys
import CargaImagen.CargaImagen as Imagen
import CreaNivel.MapRand as Nivel
import Movimiento.MovPacMan as MovPacMan
import CreaNivel.LecturaEscritura as RW
import Grafo.Grafo as GR

pygame.init()
tamano_ventana = (1200,720)
ventana = pygame.display.set_mode(tamano_ventana)

pygame.display.set_icon(Imagen.icono_ventana)
pygame.display.set_caption('PAC-MAN')

niveles = list()
MatrizVertice = []
GrafoNivel = GR.Graph() 
Escena = "MenuPrincipal"
Puntos = 0

CuadroTexto = pygame.Rect(500, 360, 200, 42)
color_inactive = pygame.Color('white')
color_active = pygame.Color('white')
color = color_inactive
active = False
NombreJugador = ''
font = pygame.font.Font(None, 42)

DireccionPacman = "inicio"
DireccionPacman2 = ""
Permitido = False
FilaPacMan = 13 # FILA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
ColPacMan = 10  # COLUMNA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
UltimoVerticePacMan = ""
ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
Jugador = Imagen.Jugador # PERMITE OBTENER LA UBICACION
NivelSeleccionado = False

while True:

    ventana.fill((0,0,0)) # LIMPIA PANTALLA
    
    if NivelSeleccionado == True:
        PosXPacMan = Jugador.rect.x
        PosYPacMan = Jugador.rect.y

    for event in pygame.event.get(): #EVENTOS
        if event.type == pygame.QUIT: #CIERRA VENTANA
            if len(niveles)!=0:
                for i in range(10):
                    RW.fileWrite(niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: #CLICK
            if pygame.mouse.get_pressed()[0]: #SI PRESIONA CLICK IZQUIERDO
                if Escena == "MenuPrincipal":
                    if Imagen.btnJugar.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "SelectorPartida" 
                    if Imagen.btnJugador.rect.collidepoint(pygame.mouse.get_pos()):
                        Escena = "Jugador"
                    if Imagen.btnAjustes.rect.collidepoint(pygame.mouse.get_pos()):
                        Escena = "Ajustes"
                    if Imagen.btnSalir.rect.collidepoint(pygame.mouse.get_pos()):
                        if len(niveles)!=0:
                            for i in range(10):
                                RW.fileWrite(niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                        sys.exit()
                elif Escena == "SelectorPartida":
                    if Imagen.btnNuevaPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "RegistraNombre"
                        NombreJugador=""
                        Puntos=0
                        niveles.clear()
                        for i in range(10):
                            niveles.append(Nivel.laberinto(10,10))
                            RW.fileWrite(niveles[i],"CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt")
                            
                    if Imagen.btnCargarPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        for i in range(10):
                            niveles.append(RW.fileRead("CreaNivel/ListasNiveles/Nivel"+str(i+1)+".txt"))
                        Escena = "SelectorNivel"

                elif Escena == "RegistraNombre":
                     # If the user clicked on the input_box rect.
                    if CuadroTexto.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                        # Change the current color of the input box.
                        color = color_active if active else color_inactive
                elif Escena == "SelectorNivel":
                    if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "MenuPrincipal"
                    if Imagen.btnSelecNiv1.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel1"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(1,niveles)
                        Imagen.CargaNivel(1,niveles)
                        Imagen.CargaPuntos(1,niveles)
                        Jugador = Imagen.ColocaPacMan(1,niveles)
                        NivelSeleccionado = True
                        MatrizVertice,GrafoNivel =  GR.CreaGrafo(niveles[0])
                    if Imagen.btnSelecNiv2.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel2"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(2,niveles)
                        Imagen.CargaNivel(2,niveles)
                        Imagen.CargaPuntos(2,niveles)
                        Jugador = Imagen.ColocaPacMan(2,niveles)
                        NivelSeleccionado = True
                        MatrizVertice,GrafoNivel = GR.CreaGrafo(niveles[1])
                    if Imagen.btnSelecNiv3.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel3"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(3,niveles)
                        Imagen.CargaNivel(3,niveles)
                        Imagen.CargaPuntos(3,niveles)
                        Jugador = Imagen.ColocaPacMan(3,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv4.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel4"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(4,niveles)
                        Imagen.CargaNivel(4,niveles)
                        Imagen.CargaPuntos(4,niveles)
                        Jugador = Imagen.ColocaPacMan(4,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv5.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel5"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(5,niveles)
                        Imagen.CargaNivel(5,niveles)
                        Imagen.CargaPuntos(5,niveles)
                        Jugador = Imagen.ColocaPacMan(5,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv6.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel6"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(6,niveles)
                        Imagen.CargaNivel(6,niveles)
                        Imagen.CargaPuntos(6,niveles)
                        Jugador = Imagen.ColocaPacMan(6,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv7.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel7"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(7,niveles)
                        Imagen.CargaNivel(7,niveles)
                        Imagen.CargaPuntos(7,niveles)
                        Jugador = Imagen.ColocaPacMan(7,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv8.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel8"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(8,niveles)
                        Imagen.CargaNivel(8,niveles)
                        Imagen.CargaPuntos(8,niveles)
                        Jugador = Imagen.ColocaPacMan(8,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv9.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel9"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(9,niveles)
                        Imagen.CargaNivel(9,niveles)
                        Imagen.CargaPuntos(9,niveles)
                        Jugador = Imagen.ColocaPacMan(9,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv10.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel10"
                        FilaPacMan, ColPacMan =Imagen.EncontrarPacMan(10,niveles)
                        Imagen.CargaNivel(10,niveles)
                        Imagen.CargaPuntos(10,niveles)
                        Jugador = Imagen.ColocaPacMan(10,niveles)
                        NivelSeleccionado = True
                elif Escena == "Nivel1" or Escena == "Nivel2" or Escena == "Nivel3" or Escena == "Nivel4" or Escena == "Nivel5" or Escena == "Nivel6" or Escena == "Nivel7" or Escena == "Nivel8" or Escena == "Nivel9" or Escena == "Nivel10":
                    if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        DireccionPacman = "inicio"
                        PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                        PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                        ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
                        Escena = "SelectorNivel"
        if event.type == pygame.KEYDOWN: # EVENTOS DE TECLADO
            if Escena == "RegistraNombre":
                if active:
                    if event.key == pygame.K_RETURN:
                        Escena = "SelectorNivel"
                    elif event.key == pygame.K_BACKSPACE:
                        NombreJugador = NombreJugador[:-1]
                    else:
                        NombreJugador += event.unicode
            if Escena == "SelectorNivel":
                if event.key == pygame.K_ESCAPE:
                    Escena = "MenuPrincipal"
            if Escena == "Nivel1" or Escena == "Nivel2" or Escena == "Nivel3" or Escena == "Nivel4" or Escena == "Nivel5" or Escena == "Nivel6" or Escena == "Nivel7" or Escena == "Nivel8" or Escena == "Nivel9" or Escena == "Nivel10":
                if event.key == pygame.K_ESCAPE:
                    Escena = "SelectorNivel"
                    DireccionPacman = "inicio"
                    FilaPacMan = 13 # FILA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
                    ColPacMan = 10  # COLUMNA DE LA MATRIZ EN DONDE SE ENCUENTRA PAC MAN
                    PosXPacMan = 0  # POSCION EN X DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                    PosYPacMan = 0  # POSCION EN Y DE LA PANTALLA DONDE SE ENCUNETRA PAC MAN
                    ContCasillas = 0 # CONTADOR QUE PERMITE IDENTIFICAR CUANDO PAC MAN AVANZA A UNA NUEVA CASILLA
                if Escena=='Nivel10':
                    NumNivel='10'
                else:
                    NumNivel = Escena[5]
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if MovPacMan.VerificaMovimiento("arriba",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
                        if ContCasillas <= 17:
                            for i in range(ContCasillas):
                                if DireccionPacman == "derecha":
                                    PosXPacMan -=2
                                if DireccionPacman == "izquierda":
                                    PosXPacMan +=2
                                if DireccionPacman == "abajo":
                                    PosYPacMan -=2
                        if DireccionPacman != "arriba":
                            DireccionPacman = "arriba"
                            ContCasillas = 0
                    else:
                        DireccionPacman2 = "arriba"
                        Permitido = True
                    
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if MovPacMan.VerificaMovimiento("abajo",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
                        if ContCasillas <= 17:
                            for i in range(ContCasillas):
                                if DireccionPacman == "derecha":
                                    PosXPacMan -=2
                                if DireccionPacman == "izquierda":
                                    PosXPacMan +=2
                                if DireccionPacman == "arriba":
                                    PosYPacMan +=2
                        if DireccionPacman != "abajo":
                            DireccionPacman = "abajo"
                            ContCasillas = 0
                    else:
                        DireccionPacman2 = "abajo"
                        Permitido = True

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    if MovPacMan.VerificaMovimiento("derecha",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
                        if ContCasillas <= 17:
                            for i in range(ContCasillas):
                                if DireccionPacman == "arriba":
                                    PosYPacMan +=2
                                if DireccionPacman == "izquierda":
                                    PosXPacMan +=2
                                if DireccionPacman == "abajo":
                                    PosYPacMan -=2
                        if DireccionPacman != "derecha":
                            DireccionPacman = "derecha"
                            ContCasillas = 0
                    else:
                        DireccionPacman2 = "derecha"
                        Permitido = True
                    
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if MovPacMan.VerificaMovimiento("izquierda",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
                        if ContCasillas <= 17:
                            for i in range(ContCasillas):
                                if DireccionPacman == "derecha":
                                    PosXPacMan -=2
                                if DireccionPacman == "arriba":
                                    PosYPacMan +=2
                                if DireccionPacman == "abajo":
                                    PosYPacMan -=2
                        if DireccionPacman != "izquierda":
                            DireccionPacman = "izquierda"
                            ContCasillas = 0
                    else:
                        DireccionPacman2 = "izquierda"
                        Permitido = True            

    if Escena == "MenuPrincipal":
        ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupMenu.draw(ventana) # DIBUJA TODOS LOS SPRITES
    if Escena == "SelectorPartida":
        ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupSelecPartida.draw(ventana) # DIBUJA TODOS LOS SPRITES
    if Escena == "RegistraNombre":
        ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupRegistroNombre.draw(ventana) # DIBUJA TODOS LOS SPRITES
        txt_surface = font.render(NombreJugador, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        CuadroTexto.w = width
        # Blit the text.
        ventana.blit(txt_surface, (CuadroTexto.x+5, CuadroTexto.y+5))
        pygame.draw.rect(ventana, color, CuadroTexto, 2)
    if Escena == "SelectorNivel":
        ventana.blit(Imagen.ImgFondoMenu,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupSelecNivel.draw(ventana) # DIBUJA TODOS LOS SPRITES
    
    if Escena == "Nivel1":
        ventana.blit(Imagen.ImgFondoNivel1, [0,0])
    if Escena == "Nivel2":
        ventana.blit(Imagen.ImgFondoNivel2, [0,0])
    if Escena == "Nivel3":
        ventana.blit(Imagen.ImgFondoNivel3, [0,0])
    if Escena == "Nivel4":
        ventana.blit(Imagen.ImgFondoNivel4, [0,0])
    if Escena == "Nivel5":
        ventana.blit(Imagen.ImgFondoNivel5, [0,0])
    if Escena == "Nivel6":
        ventana.blit(Imagen.ImgFondoNivel6, [0,0])
    if Escena == "Nivel7":
        ventana.blit(Imagen.ImgFondoNivel7, [0,0])
    if Escena == "Nivel8":
        ventana.blit(Imagen.ImgFondoNivel8, [0,0])
    if Escena == "Nivel9":
        ventana.blit(Imagen.ImgFondoNivel9, [0,0])
    if Escena == "Nivel10":
        ventana.blit(Imagen.ImgFondoNivel10, [0,0])

    if Escena == "Nivel1" or Escena == "Nivel2" or Escena == "Nivel3" or Escena == "Nivel4" or Escena == "Nivel5" or Escena == "Nivel6" or Escena == "Nivel7" or Escena == "Nivel8" or Escena == "Nivel9" or Escena == "Nivel10":
        if Escena=='Nivel10':
            NumNivel='10'
        else:
            NumNivel = Escena[5]
        Matriz = niveles[int(NumNivel)-1]
        if Permitido == True and MovPacMan.VerificaMovimiento(DireccionPacman2,niveles[int(NumNivel)-1],FilaPacMan,ColPacMan):
            DireccionPacman = DireccionPacman2
            DireccionPacman2 = ""
            Permitido = False
        if DireccionPacman == "derecha":
            if MovPacMan.VerificaMovimiento("derecha",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan):
                if ContCasillas == 17:
                    if Matriz[FilaPacMan][ColPacMan+1]=='.':
                        Puntos+=1
                    MovPacMan.Movimiento(DireccionPacman,niveles[int(NumNivel)-1],FilaPacMan,ColPacMan)
                    ColPacMan+=1
                    ContCasillas = 0
                else:
                    PosXPacMan = PosXPacMan+2
                    ContCasillas += 1
            Imagen.ActualizaPacMan(Jugador,PosXPacMan,PosYPacMan)
            Imagen.ActualizaPts(int(NumNivel),niveles)
        if DireccionPacman == "izquierda":
            if MovPacMan.VerificaMovimiento("izquierda",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan):
                if ContCasillas == 17:
                    if Matriz[FilaPacMan][ColPacMan-1]=='.':
                        Puntos+=1
                    MovPacMan.Movimiento(DireccionPacman,niveles[int(NumNivel)-1],FilaPacMan,ColPacMan)
                    ColPacMan-=1
                    ContCasillas = 0
                else:
                    PosXPacMan = PosXPacMan-2
                    ContCasillas += 1
            Imagen.ActualizaPacMan(Jugador,PosXPacMan,PosYPacMan)
            Imagen.ActualizaPts(int(NumNivel),niveles)
        if DireccionPacman == "arriba":
            if MovPacMan.VerificaMovimiento("arriba",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan):
                if ContCasillas == 17:
                    if Matriz[FilaPacMan-1][ColPacMan]=='.':
                        Puntos+=1
                    MovPacMan.Movimiento(DireccionPacman,niveles[int(NumNivel)-1],FilaPacMan,ColPacMan)
                    FilaPacMan-=1
                    ContCasillas = 0
                else:
                    PosYPacMan = PosYPacMan-2
                    ContCasillas += 1
            Imagen.ActualizaPacMan(Jugador,PosXPacMan,PosYPacMan)
            Imagen.ActualizaPts(int(NumNivel),niveles)
        if DireccionPacman == "abajo":
            if MovPacMan.VerificaMovimiento("abajo",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan):
                if ContCasillas == 17:
                    if Matriz[FilaPacMan+1][ColPacMan]=='.':
                        Puntos+=1
                    MovPacMan.Movimiento(DireccionPacman,niveles[int(NumNivel)-1],FilaPacMan,ColPacMan)
                    FilaPacMan+=1
                    ContCasillas = 0
                else:
                    PosYPacMan = PosYPacMan+2
                    ContCasillas += 1
            Imagen.ActualizaPacMan(Jugador,PosXPacMan,PosYPacMan)
            Imagen.ActualizaPts(int(NumNivel),niveles)

        #Actualiza el ultimo vertice que ha visitado el PacMan en el tablero    
        if MatrizVertice[FilaPacMan][ColPacMan] != "#" or MatrizVertice[FilaPacMan][ColPacMan] != " ":
            UltimoVerticePacMan = MatrizVertice[FilaPacMan][ColPacMan]

        Imagen.mover.draw(ventana)
        Imagen.mover.update(0.1,DireccionPacman)

        Imagen.ImgGroupNivel.draw(ventana) # DIBUJA TODOS LOS SPRITES
        Imagen.ImgGroupPuntos.draw(ventana)
        TituloJugador = font.render("Jugador: ", True, 'white')
        ventana.blit(TituloJugador, (800, 20))
        LblJugador = font.render(NombreJugador, True, 'white')
        ventana.blit(LblJugador, (930, 20))

        TituloPuntos = font.render("Puntos: ", True, 'white')
        ventana.blit(TituloPuntos, (800, 50))
        LblPuntos = font.render(str(Puntos), True, 'white')
        ventana.blit(LblPuntos, (920, 50))

        #Movimineto del Fantasma
        if Imagen.ImgBlinky.rect.x > 0:
            Imagen.ActualizaFantasma(Imagen.ImgBlinky,Imagen.ImgBlinky.rect.x-1,Imagen.ImgBlinky.rect.y)

    pygame.display.flip() 