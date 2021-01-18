import pygame
import CreaNivel.MapRand as nivel

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

ImgFondoMenu = pygame.image.load("imagenes/FondoMenu.jpg")  
ImgFondoMenu = pygame.transform.scale(ImgFondoMenu, (1200, 720))

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

# MENU PRINCIPAL
TituloInicial = CargaImagen("imagenes/tituloPacMan.png",0,0,420,30,False)
IconoTitulo = CargaImagen("imagenes/iconoTitulo.png",500,500,350,-20,True)
btnJugar = CargaImagen("imagenes/btnIniciar.png",250,60,490,300,True)
btnJugador = CargaImagen("imagenes/btnJugador.png",250,60,490,380,True)
btnAjustes = CargaImagen("imagenes/btnAjustes.png",250,60,490,460,True)
btnSalir = CargaImagen("imagenes/btnSalir.png",250,60,490,540,True)

ImgGroupMenu = pygame.sprite.Group()
ImgGroupMenu.add(btnJugar)
ImgGroupMenu.add(btnJugador)
ImgGroupMenu.add(btnAjustes)
ImgGroupMenu.add(btnSalir)
ImgGroupMenu.add(TituloInicial)
ImgGroupMenu.add(IconoTitulo)

# MENU SELECTOR PARTIDA
btnNuevaPartida = CargaImagen("imagenes/btnNuevaPartida.png",250,60,490,300,True)
btnCargarPartida = CargaImagen("imagenes/btnCargarPartida.png",250,60,490,380,True)

ImgGroupSelecPartida = pygame.sprite.Group()
ImgGroupSelecPartida.add(btnNuevaPartida)
ImgGroupSelecPartida.add(btnCargarPartida)
ImgGroupSelecPartida.add(TituloInicial)
ImgGroupSelecPartida.add(IconoTitulo)

# REGISTRO DE NOMBRE DE JUGADOR
ImgGroupRegistroNombre = pygame.sprite.Group()
ImgGroupRegistroNombre.add(TituloInicial)
ImgGroupRegistroNombre.add(IconoTitulo)

# SELECTOR DE NIVEL
TituloSelectorNivel = CargaImagen("imagenes/TituloSelectorNivel.png",0,0,300,30,False)
btnSelecNiv1 = CargaImagen("imagenes/SelectorNiv1.png",250,60,30,150,False)
btnSelecNiv2 = CargaImagen("imagenes/SelectorNiv2.png",250,60,260,150,False)
btnSelecNiv3 = CargaImagen("imagenes/SelectorNiv3.png",250,60,490,150,False)
btnSelecNiv4 = CargaImagen("imagenes/SelectorNiv4.png",250,60,720,150,False)
btnSelecNiv5 = CargaImagen("imagenes/SelectorNiv5.png",250,60,950,150,False)
btnSelecNiv6 = CargaImagen("imagenes/SelectorNiv6.png",250,60,30,400,False)
btnSelecNiv7 = CargaImagen("imagenes/SelectorNiv7.png",250,60,260,400,False)
btnSelecNiv8 = CargaImagen("imagenes/SelectorNiv8.png",250,60,490,400,False)
btnSelecNiv9 = CargaImagen("imagenes/SelectorNiv9.png",250,60,720,400,False)
btnSelecNiv10 = CargaImagen("imagenes/SelectorNiv10.png",250,60,950,400,False)

ImgGroupSelecNivel = pygame.sprite.Group()
ImgGroupSelecNivel.add(TituloSelectorNivel)
ImgGroupSelecNivel.add(btnSelecNiv1)
ImgGroupSelecNivel.add(btnSelecNiv2)
ImgGroupSelecNivel.add(btnSelecNiv3)
ImgGroupSelecNivel.add(btnSelecNiv4)
ImgGroupSelecNivel.add(btnSelecNiv5)
ImgGroupSelecNivel.add(btnSelecNiv6)
ImgGroupSelecNivel.add(btnSelecNiv7)
ImgGroupSelecNivel.add(btnSelecNiv8)
ImgGroupSelecNivel.add(btnSelecNiv9)
ImgGroupSelecNivel.add(btnSelecNiv10)

ImgGroupNivel1 = pygame.sprite.Group()
# CARGA ELEMENTOS DEL NIVEL 1
def CargaNivel(NumNivel):
    x = 15
    y = 15

    matriz = nivel.niveles[NumNivel-1]

    for i in range(21):
        x = 15
        for j in range(21):
            
            if matriz[i][j] == '█':
                MuroNiv1 = CargaImagen("imagenes/ImgNiveles/Muro1.png",33,33,x,y,True)
                ImgGroupNivel1.add(MuroNiv1)
            x += 33
        y += 33