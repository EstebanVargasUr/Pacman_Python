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

while True:

    for event in pygame.event.get(): #EVENTOS
        if event.type == pygame.QUIT: #CIERRA VENTANA
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: #CLICK
            if pygame.mouse.get_pressed()[0]: #SI PRESIONA CLICK IZQUIERDO
                if Imagen.btnJugar.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                    Escena = "Nivel1"
                    if NivelesJugador == False:
                        NivelesJugador = True
                        for i in range(10):
                            niveles.append(Nivel.laberinto(12,12))
                        
    if Escena == "Nivel1":
        ventana.blit(Imagen.ImgFondoNivel1,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel2":
        ventana.blit(Imagen.ImgFondoNivel2,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel3":
        ventana.blit(Imagen.ImgFondoNivel3,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel4":
        ventana.blit(Imagen.ImgFondoNivel4,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel5":
        ventana.blit(Imagen.ImgFondoNivel5,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel6":
        ventana.blit(Imagen.ImgFondoNivel6,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel7":
        ventana.blit(Imagen.ImgFondoNivel7,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel8":
        ventana.blit(Imagen.ImgFondoNivel8,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel9":
        ventana.blit(Imagen.ImgFondoNivel9,[0,0]) # PARA EL FONDO    
    if Escena == "Nivel10":
        ventana.blit(Imagen.ImgFondoNivel10,[0,0]) # PARA EL FONDO    
    
    Imagen.img_group.draw(ventana) # DIBUJA TODOS LOS SPRITES
    
    pygame.display.flip() 