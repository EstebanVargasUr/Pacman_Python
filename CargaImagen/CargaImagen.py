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
class pacman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.spritesDerecha=[]
        self.spritesIzquierda=[]
        self.spritesFrente=[]
        self.spritesAtras=[]
        self.is_animating=False
        self.spritesDerecha.append(pygame.image.load('imagenes/derecha1.png'))
        self.spritesDerecha.append(pygame.image.load('imagenes/derecha2.png'))

        self.spritesIzquierda.append(pygame.image.load('imagenes/izquierda1.png'))
        self.spritesIzquierda.append(pygame.image.load('imagenes/izquierda2.png'))

        self.spritesFrente.append(pygame.image.load('imagenes/frente1.png'))
        self.spritesFrente.append(pygame.image.load('imagenes/frente2.png'))

        self.spritesAtras.append(pygame.image.load('imagenes/atras1.png'))
        self.spritesAtras.append(pygame.image.load('imagenes/atras2.png'))
        self.spriteActual=0

        self.image= self.spritesDerecha[self.spriteActual]
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect= self.image.get_rect()
        self.rect.topleft= [pos_x, pos_y]
        
    def animate(self):
        self.is_animating=True
    def update(self, speed, direccion):
        if self.is_animating==True:
            self.spriteActual+=speed
            if direccion=="derecha":
                if self.spriteActual>=len(self.spritesDerecha):
                    self.spriteActual=0
                self.image=self.spritesDerecha[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (35, 35))
            if direccion=="izquierda":
                if self.spriteActual>=len(self.spritesIzquierda):
                    self.spriteActual=0
                self.image=self.spritesIzquierda[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (35, 35))
            if direccion=="frente":
                if self.spriteActual>=len(self.spritesFrente):
                    self.spriteActual=0
                self.image=self.spritesFrente[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (35, 35))
            if direccion=="atras":
                if self.spriteActual>=len(self.spritesAtras):
                    self.spriteActual=0
                self.image=self.spritesAtras[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (35, 35))
            
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
ImgGroupPuntos = pygame.sprite.Group()
#CARGA PERSONAJES
mover= pygame.sprite.Group()
jugador=pacman(120,120)
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
def CargaPuntos(NumNivel,Direccion1,Direccion2):
    ImgGroupPuntos.empty()
    x = 27
    y = 27
    matriz = nivel.niveles[NumNivel-1]
    for i in range(21):
        x = 27
        for j in range(21):
            if matriz[i][j] == '.':
                PuntoNiv = CargaImagen(Direccion1,33,33,x,y,False)
                ImgGroupPuntos.add(PuntoNiv)
            if matriz[i][j] == 'O':
                PuntoNiv = CargaImagen(Direccion2,33,33,x-5,y-5,False)
                ImgGroupPuntos.add(PuntoNiv)
            x += 33
        y += 33
def moverPacMan(NumNivel):
    jugador= None
    mover.empty() 
    x = 15
    y = 15
    matriz = nivel.niveles[NumNivel-1]
    for i in range(21):
        x = 15
        for j in range(21):
            if matriz[i][j] == '$':
                jugador= pacman(x,y)
                mover.add(jugador)
            x += 33
        y += 33
    jugador.animate()