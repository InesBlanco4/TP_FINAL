import pygame
import sys
import pygame.mixer as mixer
import juego.jugar as jugar
import juego.funciones as funciones
import rutas as rutas
import juego.valores_cartas as cargar_cartas
import juego.opciones as opciones
import juego.salir as salir
from juego.menu import *
from juego.funciones import *
from juego.valores_cartas import *
from juego.jugar import *

mixer.init()
pygame.init()

import juego.menu as menu
import juego.partida as partida

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gatruco")
icono = pygame.image.load("imagenes/importante/gato_icono.jpg")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()


modalidad = 1
bandera = True

pygame.mixer.music.load("musica/musica_fondo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.02)

musica = True
#Inicio
while bandera == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bandera = False

    if rutas.ruta_actual == "menu": 
        menu.comienzo(ventana)
    elif rutas.ruta_actual == "jugar":
        partida.comienzo(ventana)
    elif rutas.ruta_actual == "opciones":
        opciones.comienzo(ventana)
    elif rutas.ruta_actual == "salir":
        sys.exit()

    pygame.display.update()

pygame.quit()