import pygame, sys
import CargaImagen.CargaImagen as Imagen
import CreaNivel.MapRand as Nivel

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
while True:

    ventana.fill((0,0,0)) # LIMPIA PANTALLA

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
                        Imagen.CargaNivel(1,"imagenes/ImgNiveles/Muro1.png")
                        Imagen.CargaPuntos(1,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(1)
                    if Imagen.btnSelecNiv2.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel2"
                        Imagen.CargaNivel(2,"imagenes/ImgNiveles/Muro2.png")
                        Imagen.CargaPuntos(2,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(2)
                    if Imagen.btnSelecNiv3.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel3"
                        Imagen.CargaNivel(3,"imagenes/ImgNiveles/Muro3.png")
                        Imagen.CargaPuntos(3,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(3)
                    if Imagen.btnSelecNiv4.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel4"
                        Imagen.CargaNivel(4,"imagenes/ImgNiveles/Muro4.png")
                        Imagen.CargaPuntos(4,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(4)
                    if Imagen.btnSelecNiv5.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel5"
                        Imagen.CargaNivel(5,"imagenes/ImgNiveles/Muro5.png")
                        Imagen.CargaPuntos(5,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(5)
                    if Imagen.btnSelecNiv6.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel6"
                        Imagen.CargaNivel(6,"imagenes/ImgNiveles/Muro6.png")
                        Imagen.CargaPuntos(6,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(6)
                    if Imagen.btnSelecNiv7.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel7"
                        Imagen.CargaNivel(7,"imagenes/ImgNiveles/Muro7.png")
                        Imagen.CargaPuntos(7,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(7)
                    if Imagen.btnSelecNiv8.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel8"
                        Imagen.CargaNivel(8,"imagenes/ImgNiveles/Muro8.png")
                        Imagen.CargaPuntos(8,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(8)
                    if Imagen.btnSelecNiv9.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel9"
                        Imagen.CargaNivel(9,"imagenes/ImgNiveles/Muro9.png")
                        Imagen.CargaPuntos(9,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(9)
                    if Imagen.btnSelecNiv10.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel10"
                        Imagen.CargaNivel(10,"imagenes/ImgNiveles/Muro10.png")
                        Imagen.CargaPuntos(10,"imagenes/ImgNiveles/PuntoNivel2.png","imagenes/ImgNiveles/PowerPelletNiv2.png")
                        Imagen.moverPacMan(10)
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
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel1.png"),[0,0]) # PARA EL FONDO   
    if Escena == "Nivel2":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel2.png"),[0,0])
    if Escena == "Nivel3":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel3.png"),[0,0])
    if Escena == "Nivel4":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel4.png"),[0,0])
    if Escena == "Nivel5":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel5.png"),[0,0])
    if Escena == "Nivel6":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel6.png"),[0,0])
    if Escena == "Nivel7":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel7.png"),[0,0])
    if Escena == "Nivel8":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel8.png"),[0,0])
    if Escena == "Nivel9":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel9.png"),[0,0])
    if Escena == "Nivel10":
        ventana.blit(Imagen.CargaFondoNivel("imagenes/FondoNivel10.png"),[0,0])

    if Escena == "Nivel1" or Escena == "Nivel2" or Escena == "Nivel3" or Escena == "Nivel4" or Escena == "Nivel5" or Escena == "Nivel6" or Escena == "Nivel7" or Escena == "Nivel8" or Escena == "Nivel9" or Escena == "Nivel10":
        Imagen.mover.draw(ventana)
        Imagen.mover.update(0.1,"derecha")
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