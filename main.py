import pygame, sys
import CargaImagen.CargaImagen as Imagen
import CreaNivel.MapRand as Nivel
import Movimiento.MovPacMan as MovPacMan
import CreaNivel.LecturaEscritura as RW

pygame.init()
tamano_ventana = (1200,720)
ventana = pygame.display.set_mode(tamano_ventana)

pygame.display.set_icon(Imagen.icono_ventana)
pygame.display.set_caption('PAC-MAN')

niveles = list()
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
                        Escena = "Salir"
                elif Escena == "SelectorPartida":
                    if Imagen.btnNuevaPartida.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "RegistraNombre"
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
                        Imagen.CargaNivel(1,niveles)
                        Imagen.CargaPuntos(1,niveles)
                        Jugador = Imagen.ColocaPacMan(1,niveles)
                        NivelSeleccionado = True
                    if Imagen.btnSelecNiv2.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel2"
                        Imagen.CargaNivel(2,niveles)
                        Imagen.CargaPuntos(2,niveles)
                        Imagen.ColocaPacMan(2,niveles)
                    if Imagen.btnSelecNiv3.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel3"
                        Imagen.CargaNivel(3,niveles)
                        Imagen.CargaPuntos(3,niveles)
                        Imagen.ColocaPacMan(3,niveles)
                    if Imagen.btnSelecNiv4.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel4"
                        Imagen.CargaNivel(4,niveles)
                        Imagen.CargaPuntos(4,niveles)
                        Imagen.ColocaPacMan(4,niveles)
                    if Imagen.btnSelecNiv5.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel5"
                        Imagen.CargaNivel(5,niveles)
                        Imagen.CargaPuntos(5,niveles)
                        Imagen.ColocaPacMan(5,niveles)
                    if Imagen.btnSelecNiv6.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel6"
                        Imagen.CargaNivel(6,niveles)
                        Imagen.CargaPuntos(6,niveles)
                        Imagen.ColocaPacMan(6,niveles)
                    if Imagen.btnSelecNiv7.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel7"
                        Imagen.CargaNivel(7,niveles)
                        Imagen.CargaPuntos(7,niveles)
                        Imagen.ColocaPacMan(7,niveles)
                    if Imagen.btnSelecNiv8.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel8"
                        Imagen.CargaNivel(8,niveles)
                        Imagen.CargaPuntos(8,niveles)
                        Imagen.ColocaPacMan(8,niveles)
                    if Imagen.btnSelecNiv9.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel9"
                        Imagen.CargaNivel(9,niveles)
                        Imagen.CargaPuntos(9,niveles)
                        Imagen.ColocaPacMan(9,niveles)
                    if Imagen.btnSelecNiv10.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel10"
                        Imagen.CargaNivel(10,niveles)
                        Imagen.CargaPuntos(10,niveles)
                        Imagen.ColocaPacMan(10,niveles)
                elif Escena == "Nivel1" or Escena == "Nivel2" or Escena == "Nivel3" or Escena == "Nivel4" or Escena == "Nivel5" or Escena == "Nivel6" or Escena == "Nivel7" or Escena == "Nivel8" or Escena == "Nivel9" or Escena == "Nivel10":
                    if Imagen.btnAtras.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
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
                    
                NumNivel = Escena[5]
                if event.key == pygame.K_UP:
                    if MovPacMan.VerificaMovimiento("arriba",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan) or event.key == pygame.K_w and Nivel.VerificaMovimiento("arriba",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
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
                    
                if event.key == pygame.K_DOWN:
                    if MovPacMan.VerificaMovimiento("abajo",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan) or event.key == pygame.K_s and Nivel.VerificaMovimiento("abajo",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
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

                if event.key == pygame.K_RIGHT: 
                    if MovPacMan.VerificaMovimiento("derecha",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan) or event.key == pygame.K_d and Nivel.VerificaMovimiento("derecha",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
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
                    
                if event.key == pygame.K_LEFT:
                    if MovPacMan.VerificaMovimiento("izquierda",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan) or event.key == pygame.K_a and Nivel.VerificaMovimiento("izquierda",niveles[int(NumNivel)-1],FilaPacMan,ColPacMan): 
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
                    MovPacMan.Movimiento(DireccionPacman,niveles,FilaPacMan,ColPacMan)
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
                    MovPacMan.Movimiento(DireccionPacman,niveles,FilaPacMan,ColPacMan)
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
                    MovPacMan.Movimiento(DireccionPacman,niveles,FilaPacMan,ColPacMan)
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
                    MovPacMan.Movimiento(DireccionPacman,niveles,FilaPacMan,ColPacMan)
                    FilaPacMan+=1
                    ContCasillas = 0
                else:
                    PosYPacMan = PosYPacMan+2
                    ContCasillas += 1
            Imagen.ActualizaPacMan(Jugador,PosXPacMan,PosYPacMan)
            Imagen.ActualizaPts(int(NumNivel),niveles)
            
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

        
    if Escena == "Salir":
        sys.exit()

    pygame.display.flip() 