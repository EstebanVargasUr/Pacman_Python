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

ImgFondoNivel1 = pygame.image.load("imagenes/FondoNivel1.png")  
ImgFondoNivel1 = pygame.transform.scale(ImgFondoNivel1, (1200, 720))
ImgFondoNivel2 = pygame.image.load("imagenes/FondoNivel2.png")  
ImgFondoNivel2 = pygame.transform.scale(ImgFondoNivel2, (1200, 720))
ImgFondoNivel3 = pygame.image.load("imagenes/FondoNivel3.png")  
ImgFondoNivel3 = pygame.transform.scale(ImgFondoNivel3, (1200, 720))
ImgFondoNivel4 = pygame.image.load("imagenes/FondoNivel4.png")  
ImgFondoNivel4 = pygame.transform.scale(ImgFondoNivel4, (1200, 720))
ImgFondoNivel5 = pygame.image.load("imagenes/FondoNivel5.png")  
ImgFondoNivel5 = pygame.transform.scale(ImgFondoNivel5, (1200, 720))
ImgFondoNivel6 = pygame.image.load("imagenes/FondoNivel6.png")  
ImgFondoNivel6 = pygame.transform.scale(ImgFondoNivel6, (1200, 720))
ImgFondoNivel7 = pygame.image.load("imagenes/FondoNivel7.png")  
ImgFondoNivel7 = pygame.transform.scale(ImgFondoNivel7, (1200, 720))
ImgFondoNivel8 = pygame.image.load("imagenes/FondoNivel8.png")  
ImgFondoNivel8 = pygame.transform.scale(ImgFondoNivel8, (1200, 720))
ImgFondoNivel9 = pygame.image.load("imagenes/FondoNivel9.png")  
ImgFondoNivel9 = pygame.transform.scale(ImgFondoNivel9, (1200, 720))
ImgFondoNivel10 = pygame.image.load("imagenes/FondoNivel10.png")  
ImgFondoNivel10 = pygame.transform.scale(ImgFondoNivel10, (1200, 720))

TituloInicial = CargaImagen("imagenes/tituloPacMan.png",0,0,420,50,False)

btnJugar = CargaImagen("imagenes/icono_ventana.png",100,100,550,250,True)

img_group = pygame.sprite.Group()
img_group.add(btnJugar)
img_group.add(TituloInicial)
