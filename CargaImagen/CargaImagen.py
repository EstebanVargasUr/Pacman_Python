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
class CargaSprite(pygame.sprite.Sprite):
    def __init__(self, imagen , anchura, altura, pos_x , pos_y, ajustar):
        super().__init__()
        
        self.image = imagen
        
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
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect= self.image.get_rect()
        self.rect.topleft= [pos_x, pos_y]
        
    def animate(self):
        self.is_animating=True
    def noanimate(self):
        self.is_animating=False
    def update(self, speed, direccion):
        if self.is_animating==True:
            self.spriteActual+=speed
            if direccion=="derecha":
                if self.spriteActual>=len(self.spritesDerecha):
                    self.spriteActual=0
                self.image=self.spritesDerecha[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (30, 30))
            if direccion=="izquierda":
                if self.spriteActual>=len(self.spritesIzquierda):
                    self.spriteActual=0
                self.image=self.spritesIzquierda[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (30, 30))
            if direccion=="arriba":
                if self.spriteActual>=len(self.spritesFrente):
                    self.spriteActual=0
                self.image=self.spritesFrente[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (30, 30))
            if direccion=="abajo":
                if self.spriteActual>=len(self.spritesAtras):
                    self.spriteActual=0
                self.image=self.spritesAtras[int(self.spriteActual)]
                self.image = pygame.transform.scale(self.image, (30, 30))
class Fantasma(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,rutaAbajo,rutaArriba,rutaIzquierda,rutaDerecha,peligro,regreso):
        super().__init__()
        self.sprites=[]
        self.sprites.append(pygame.image.load(rutaAbajo))
        self.sprites.append(pygame.image.load(rutaArriba))
        self.sprites.append(pygame.image.load(rutaIzquierda))
        self.sprites.append(pygame.image.load(rutaDerecha))
        self.sprites.append(pygame.image.load(peligro))
        self.sprites.append(pygame.image.load(regreso))
        self.image= self.sprites[0]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect= self.image.get_rect()
        self.rect.topleft= [pos_x, pos_y]
    def update(self, direccion):
        if direccion=="regreso":
            self.image=self.sprites[5]
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif direccion=="peligro":
            self.image=self.sprites[4]
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif direccion=="derecha":
            self.image=self.sprites[3]
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif direccion=="izquierda":
            self.image=self.sprites[2]
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif direccion=="arriba":
            self.image=self.sprites[1]
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif direccion=="abajo":
            self.image=self.sprites[0]
            self.image = pygame.transform.scale(self.image, (30, 30))

icono_ventana = pygame.image.load("imagenes/icono_ventana.png")
ImgFondoMenu = pygame.image.load("imagenes/FondoMenu.jpg")  
ImgFondoMenu = pygame.transform.scale(ImgFondoMenu, (1200, 720))
btnAtras = CargaImagen("imagenes/btnDevolver.png",100,40,1080,670,True)
btnPoder = CargaImagen("imagenes/SuperVelocidad.png",100,100,1090,550,True)
btnPoderG = pygame.sprite.Group()
btnPoderG.add(btnPoder)

#VICTORIA
btnHome = CargaImagen("imagenes/btnHome.png",80,80,390,315,True)
btnNiveles = CargaImagen("imagenes/btnNiveles.png",80,80,490,315,True)
btnSiguiente = CargaImagen("imagenes/btnSiguiente.png",80,80,590,315,True)
barraVictoria = CargaImagen("imagenes/BarraVictoria.png",441,120,350,300,True)
ImgGroupVictoria = pygame.sprite.Group()
ImgGroupVictoria.add(barraVictoria)
ImgGroupVictoria.add(btnHome)
ImgGroupVictoria.add(btnNiveles)
ImgGroupVictoria.add(btnSiguiente)

Jugador = pacman(0,0)
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

#GAME OVER
TituloGameOver = CargaImagen("imagenes/TituloGameOver.png",0,0,420,70,False)
IconoTit = CargaImagen("imagenes/iconoTitulo.png",500,500,350,-60,True)
Puntos = CargaImagen("imagenes/Puntos.png",0,0,370,250,False)
Vidas = CargaImagen("imagenes/Vidas.png",0,0,370,325,False)
btnAbandonar = CargaImagen("imagenes/btnAbandonar.png",280,80,490,530,True)

ImgGroupGameOver = pygame.sprite.Group()
ImgGroupGameOver.add(TituloGameOver)
ImgGroupGameOver.add(IconoTit)
ImgGroupGameOver.add(Puntos)
ImgGroupGameOver.add(Vidas)
ImgGroupGameOver.add(btnAbandonar)

#ESTADISTICAS
TituloEstadisticas = CargaImagen("imagenes/TituloEstadisticas.png",0,0,450,50,False)
PuntajeTotal = CargaImagen("imagenes/PuntosGanados.png",0,0,110,150,False)
PuntajeVida = CargaImagen("imagenes/PuntajeVida.png",0,0,110,210,False)
VidaPerdida = CargaImagen("imagenes/VidasPerdidasJ.png",0,0,830,150,False)
Nivel1 = CargaImagen("imagenes/Nivel1.png",0,0,150,320,False)
Nivel2 = CargaImagen("imagenes/Nivel2.png",0,0,350,320,False)
Nivel3 = CargaImagen("imagenes/Nivel3.png",0,0,550,320,False)
Nivel4 = CargaImagen("imagenes/Nivel4.png",0,0,750,320,False)
Nivel5 = CargaImagen("imagenes/Nivel5.png",0,0,950,320,False)
Nivel6 = CargaImagen("imagenes/Nivel6.png",0,0,150,470,False)
Nivel7 = CargaImagen("imagenes/Nivel7.png",0,0,350,470,False)
Nivel8 = CargaImagen("imagenes/Nivel8.png",0,0,550,470,False)
Nivel9 = CargaImagen("imagenes/Nivel9.png",0,0,750,470,False)
Nivel10 = CargaImagen("imagenes/Nivel10.png",0,0,950,470,False)
Pts1 = CargaImagen("imagenes/Pts.png",60,30,10,350,True)
Veces1 = CargaImagen("imagenes/Partidas.png",80,30,10,390,False)
Pts2 = CargaImagen("imagenes/Pts.png",60,30,10,510,True)
Veces2 = CargaImagen("imagenes/Partidas.png",80,30,10,550,False)
TiempoTotal = CargaImagen("imagenes/TiempoTotal.png",80,30,830,210,False)
btnTop = CargaImagen("imagenes/btnTop.png",280,80,460,620,True)

ImgGroupEstadisiticas = pygame.sprite.Group()
ImgGroupEstadisiticas.add(TituloEstadisticas)
ImgGroupEstadisiticas.add(PuntajeTotal)
ImgGroupEstadisiticas.add(PuntajeVida)
ImgGroupEstadisiticas.add(VidaPerdida)
ImgGroupEstadisiticas.add(Nivel1)
ImgGroupEstadisiticas.add(Nivel2)
ImgGroupEstadisiticas.add(Nivel3)
ImgGroupEstadisiticas.add(Nivel4)
ImgGroupEstadisiticas.add(Nivel5)
ImgGroupEstadisiticas.add(Nivel6)
ImgGroupEstadisiticas.add(Nivel7)
ImgGroupEstadisiticas.add(Nivel8)
ImgGroupEstadisiticas.add(Nivel9)
ImgGroupEstadisiticas.add(Nivel10)
ImgGroupEstadisiticas.add(Pts1)
ImgGroupEstadisiticas.add(Veces1)
ImgGroupEstadisiticas.add(Pts2)
ImgGroupEstadisiticas.add(Veces2)
ImgGroupEstadisiticas.add(btnTop)
ImgGroupEstadisiticas.add(TiempoTotal)
ImgGroupEstadisiticas.add(btnAtras)
#TOP 10 MEJORES PUNTAJES
TituloTop = CargaImagen("imagenes/TituloTop.png",0,0,380,50,False)
ImgGroupTop = pygame.sprite.Group()
ImgGroupTop.add(TituloTop)
ImgGroupTop.add(btnAtras)
#AJUSTES
TituloAjustes = CargaImagen("imagenes/TituloAjustes.png",0,0,500,70,False)
IconoTitu = CargaImagen("imagenes/iconoTitulo.png",500,500,350,-90,True)
btnDesbloquea = CargaImagen("imagenes/btnDesbloquear.png",0,0,430,240,False)
ElijaDificultad = CargaImagen("imagenes/CambioDifi.png",0,0,410,380,False)
btnMedio = CargaImagen("imagenes/btnMedio.png",280,80,490,440,True)
btnDificil = CargaImagen("imagenes/btnDificil.png",280,80,490,550,True)
ImgGroupAjustes = pygame.sprite.Group()
ImgGroupAjustes.add(TituloAjustes)
ImgGroupAjustes.add(IconoTitu)
ImgGroupAjustes.add(btnDesbloquea)
ImgGroupAjustes.add(ElijaDificultad)
ImgGroupAjustes.add(btnMedio)
ImgGroupAjustes.add(btnDificil)
ImgGroupAjustes.add(btnAtras)


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

ImgFondoNivel1 = pygame.image.load("imagenes/FondoNivel1.jpg")  
ImgFondoNivel1 = pygame.transform.scale(ImgFondoNivel1, (1200, 720))
ImgFondoNivel2 = pygame.image.load("imagenes/FondoNivel2.jpg")  
ImgFondoNivel2 = pygame.transform.scale(ImgFondoNivel2, (1200, 720))
ImgFondoNivel3 = pygame.image.load("imagenes/FondoNivel3.jpg")  
ImgFondoNivel3 = pygame.transform.scale(ImgFondoNivel3, (1200, 720))
ImgFondoNivel4 = pygame.image.load("imagenes/FondoNivel4.jpg")  
ImgFondoNivel4 = pygame.transform.scale(ImgFondoNivel4, (1200, 720))
ImgFondoNivel5 = pygame.image.load("imagenes/FondoNivel5.jpg")  
ImgFondoNivel5 = pygame.transform.scale(ImgFondoNivel5, (1200, 720))
ImgFondoNivel6 = pygame.image.load("imagenes/FondoNivel6.jpg")  
ImgFondoNivel6 = pygame.transform.scale(ImgFondoNivel6, (1200, 720))
ImgFondoNivel7 = pygame.image.load("imagenes/FondoNivel7.jpg")  
ImgFondoNivel7 = pygame.transform.scale(ImgFondoNivel7, (1200, 720))
ImgFondoNivel8 = pygame.image.load("imagenes/FondoNivel8.jpg")  
ImgFondoNivel8 = pygame.transform.scale(ImgFondoNivel8, (1200, 720))
ImgFondoNivel9 = pygame.image.load("imagenes/FondoNivel9.jpg")  
ImgFondoNivel9 = pygame.transform.scale(ImgFondoNivel9, (1200, 720))
ImgFondoNivel10 = pygame.image.load("imagenes/FondoNivel10.jpg")  
ImgFondoNivel10 = pygame.transform.scale(ImgFondoNivel10, (1200, 720))

ImgPts = pygame.image.load("imagenes/ImgNiveles/PuntoNivel2.png")
ImgPower = pygame.image.load("imagenes/ImgNiveles/PowerPelletNiv2.png")

#Fantasmas
ImgGroupFantasmas=pygame.sprite.Group()
ImgBlinky = Fantasma(277,311,'imagenes/BlinkyAbajo.png','imagenes/BlinkyArriba.png','imagenes/BlinkyIzquierda.png', 'imagenes/BlinkyDerecha.png', "imagenes/Fantasmapeligro.png", "imagenes/ojosArriba.png")
ImgPinky = Fantasma(413,311,'imagenes/PinkyAbajo.png','imagenes/PinkyArriba.png','imagenes/PinkyIzquierda.png', 'imagenes/PinkyDerecha.png', "imagenes/Fantasmapeligro.png", "imagenes/ojosArriba.png" )
ImgInky = Fantasma(277,379,'imagenes/InkyAbajo.png','imagenes/InkyArriba.png','imagenes/InkyIzquierda.png', 'imagenes/InkyDerecha.png', "imagenes/Fantasmapeligro.png", "imagenes/ojosArriba.png" )
ImgClyde = Fantasma(413,379,'imagenes/ClydeAbajo.png','imagenes/ClydeArriba.png','imagenes/ClydeIzquierda.png', 'imagenes/ClydeDerecha.png', "imagenes/Fantasmapeligro.png", "imagenes/ojosArriba.png" )

ImgGroupFantasmas.add(ImgBlinky)
ImgGroupFantasmas.add(ImgPinky)
ImgGroupFantasmas.add(ImgInky)
ImgGroupFantasmas.add(ImgClyde)
ImgGroupNivel = pygame.sprite.Group()
ImgGroupPuntos = pygame.sprite.Group()
#CARGA PERSONAJES
mover= pygame.sprite.Group()

def CargaNivel(NumNivel,nivel):
    ImgMuro = pygame.image.load("imagenes/ImgNiveles/Muro"+str(NumNivel)+".png")
    ImgGroupNivel.empty()
    ImgGroupNivel.add(btnAtras)
    x = 3
    y = 3
    matriz = nivel[NumNivel-1]
    for i in range(21):
        x = 3
        for j in range(21):
            if matriz[i][j] == '#':
                MuroNiv = CargaSprite(ImgMuro,34,34,x,y,True)
                ImgGroupNivel.add(MuroNiv)
            x += 34
        y += 34

def CargaPuntos(NumNivel,nivel):
    ImgGroupPuntos.empty()
    x = 15
    y = 15
    matriz = nivel[NumNivel-1]
    for i in range(21):
        x = 15
        for j in range(21):
            if matriz[i][j] == '.':
                PuntoNiv = CargaSprite(ImgPts,34,34,x,y,False)
                ImgGroupPuntos.add(PuntoNiv)
            if matriz[i][j] == 'O':
                PuntoNiv = CargaSprite(ImgPower,34,34,x-5,y-5,False)
                ImgGroupPuntos.add(PuntoNiv)
            x += 34
        y += 34

#Coloca el pacman en posicion inicial
def ColocaPacMan(NumNivel,nivel):  
    mover.empty()
    jugador = None
    x = 3
    y = 3
    matriz = nivel[NumNivel-1]
    for i in range(21):
        x = 3
        for j in range(21):
            if matriz[i][j] == '$':
                jugador = pacman(x,y)
                mover.add(jugador)
            x += 34
        y += 34
    return jugador

def EncontrarPacMan(NumNivel,nivel):  
    matriz = nivel[NumNivel-1]
    for i in range(21):
        for j in range(21):
            if matriz[i][j] == '$':
                return i,j



#actualiza posicion pacman
def ActualizaPacMan(jugador,x,y):
    mover.empty()
    jugador.rect.x = x
    jugador.rect.y = y
    mover.add(jugador)
    jugador.animate()

def ActualizaFantasma(Fantasma,x,y,direccion):
    ImgGroupFantasmas.empty()
    
    if Fantasma == "Blinky":
        ImgBlinky.rect.x = x
        ImgBlinky.rect.y = y
        ImgBlinky.update(direccion)
    if Fantasma == "Pinky":
        ImgPinky.rect.x = x
        ImgPinky.rect.y = y
        ImgPinky.update(direccion)
    if Fantasma == "Inky":
        ImgInky.rect.x = x
        ImgInky.rect.y = y
        ImgInky.update(direccion)
    if Fantasma == "Clyde":
        ImgClyde.rect.x = x
        ImgClyde.rect.y = y
        ImgClyde.update(direccion)

    ImgGroupFantasmas.add(ImgBlinky)
    ImgGroupFantasmas.add(ImgPinky)
    ImgGroupFantasmas.add(ImgInky)
    ImgGroupFantasmas.add(ImgClyde)
    

def ActualizaPts(NumNivel,nivel):
    ImgGroupPuntos.empty()
    x = 15
    y = 15
    matriz = nivel[NumNivel-1]
    for i in range(21):
        x = 15
        for j in range(21):
            if matriz[i][j] == '.':
                PuntoNiv0 = CargaSprite(ImgPts,34,34,x,y,False)
                ImgGroupPuntos.add(PuntoNiv0)
            if matriz[i][j] == 'O':
                PuntoNiv0 = CargaSprite(ImgPower,34,34,x-5,y-5,False)
                ImgGroupPuntos.add(PuntoNiv0)
            x += 34
        y += 34