import pygame, sys
import CargaImagen.CargaImagen as Imagen

pygame.init()
tamano_ventana = (1200,720)
ventana = pygame.display.set_mode(tamano_ventana)

pygame.display.set_icon(Imagen.icono_ventana)
pygame.display.set_caption('PAC-MAN')

while True:

    for event in pygame.event.get(): #EVENTOS
        if event.type == pygame.QUIT: #CIERRA VENTANA
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: #CLICK
            if pygame.mouse.get_pressed()[0]: #SI PRESIONA CLICK IZQUIERDO
                if Imagen.btnJugar.rect.collidepoint(pygame.mouse.get_pos()): #CLICK DENTRO DEL SPRITE
                    print("entra a jugar")

    ventana.blit(Imagen.ImgFondo,[0,0]) # PARA EL FONDO    
    Imagen.img_group.draw(ventana) # DIBUJA TODOS LOS SPRITES
    
    pygame.display.flip() 