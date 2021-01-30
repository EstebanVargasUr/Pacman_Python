import pygame.mixer
import time

def crearSonido(name):
    fullname = "sonidos/" + name     # path + name of the sound file
    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(0.10)
    return sound

def SonidoMover():
    sonido = crearSonido("pacman_chomp.wav")
    sonido.play()
    time.sleep(0.4)
    sonido.stop()

def SonidoMuerte():
    sonido = crearSonido("pacman_death.wav")
    sonido.play()
    time.sleep(2)
    sonido.stop()

def SonidoComerFantasma():
    sonido = crearSonido("pacman_eatghost.wav")
    sonido.play()
    

def SonidoIniciar():
    sonido = crearSonido("pacman_beginning.wav")
    sonido.play()
    time.sleep(4.2)
    sonido.stop()

def SonidoVictoria():
    sonido = crearSonido("pacman_intermission.wav")
    sonido.play()