import pygame
import juego.funciones as func
import rutas


def dibujar_fondo(ventana):
    info = pygame.display.Info()
    imagen = pygame.image.load("imagenes/importante/morris_el_gato.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    ventana.blit(imagen, (0, 0)) 

def comienzo(ventana):
    dibujar_fondo(ventana)
    func.btn(ventana, (100, 200), "Jugar", lambda: rutas.navegar("jugar"))
    func.btn(ventana, (100, 250), "Opciones", lambda: rutas.navegar("opciones"))
    func.btn(ventana, (100, 300), "Salir", lambda: rutas.navegar("salir"))

