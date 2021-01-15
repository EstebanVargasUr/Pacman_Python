import pygame

class CargaImagen(pygame.sprite.Sprite):
    def __init__(self, direccion , anchura, altura, pos_x , pos_y, ajustar):
        super().__init__()
        
        self.image = pygame.image.load(direccion)
        
        if ajustar == True:
            self.image = pygame.transform.scale(self.image, (anchura, altura))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

icono_ventana = pygame.image.load("imagenes/icono_ventana.png")

ImgFondo = pygame.image.load("imagenes/Fondo0.jpg")  
ImgFondo = pygame.transform.scale(ImgFondo, (1200, 720))

TituloInicial = CargaImagen("imagenes/tituloPacMan.png",0,0,180,50,False)

btnJugar = CargaImagen("imagenes/icono_ventana.png",100,100,550,250,True)

img_group = pygame.sprite.Group()
img_group.add(btnJugar)
img_group.add(TituloInicial)
