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

btnAtras = CargaImagen("imagenes/btnDevolver.png",100,40,1080,670,True)

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
TituloRegistroNombre = CargaImagen("imagenes/TituloRegistroNombre.png",250,60,320,280,False)
ImgGroupRegistroNombre = pygame.sprite.Group()
ImgGroupRegistroNombre.add(TituloInicial)
ImgGroupRegistroNombre.add(IconoTitulo)
ImgGroupRegistroNombre.add(TituloRegistroNombre)

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
ImgGroupSelecNivel.add(btnAtras)

def CargaFondoNivel(Direccion):
    ImgFondoNivel = pygame.image.load(Direccion)  
# CARGA ELEMENTOS DEL NIVEL 
    ImgFondoNivel = pygame.transform.scale(ImgFondoNivel, (1200, 720))
    return ImgFondoNivel

ImgGroupNivel = pygame.sprite.Group()


def CargaNivel(NumNivel,Direccion):
    ImgGroupNivel.empty()
    ImgGroupNivel.add(btnAtras)
    x = 15
    y = 15
    matriz = nivel.niveles[NumNivel-1]

    for i in range(21):
        x = 15
        for j in range(21):
            
            if matriz[i][j] == '█':
                MuroNiv = CargaImagen(Direccion,33,33,x,y,True)
                ImgGroupNivel.add(MuroNiv)
            x += 33
        y += 33