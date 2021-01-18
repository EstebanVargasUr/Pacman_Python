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
NivelesJugador = False # PARA VERIFICAR SI AL JUGADOR YA SE LE CREARON LOS NIVELES

CuadroTexto = pygame.Rect(500, 360, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
NombreJugador = ''
font = pygame.font.Font(None, 32)
done = False
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
                    if Imagen.btnSelecNiv1.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                        Escena = "Nivel1"
                        Imagen.CargaNivel(1)
        if event.type == pygame.KEYDOWN: # EVENTOS DE TECLADO
            if Escena == "RegistraNombre":
                if active:
                    if event.key == pygame.K_RETURN:
                        print(NombreJugador)
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
        ventana.blit(Imagen.ImgFondoNivel1,[0,0]) # PARA EL FONDO    
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES
    if Escena == "Nivel2":
        ventana.blit(Imagen.ImgFondoNivel2,[0,0]) # PARA EL FONDO   
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES 
    if Escena == "Nivel3":
        ventana.blit(Imagen.ImgFondoNivel3,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel4":
        ventana.blit(Imagen.ImgFondoNivel4,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel5":
        ventana.blit(Imagen.ImgFondoNivel5,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel6":
        ventana.blit(Imagen.ImgFondoNivel6,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel7":
        ventana.blit(Imagen.ImgFondoNivel7,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel8":
        ventana.blit(Imagen.ImgFondoNivel8,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel9":
        ventana.blit(Imagen.ImgFondoNivel9,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    
    if Escena == "Nivel10":
        ventana.blit(Imagen.ImgFondoNivel10,[0,0]) # PARA EL FONDO
        Imagen.ImgGroupNivel1.draw(ventana) # DIBUJA TODOS LOS SPRITES    

    if Escena == "Salir":
        sys.exit()
    
    pygame.display.flip() 