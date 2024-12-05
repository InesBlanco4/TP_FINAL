import pygame

def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    imagen = pygame.image.load("recursos/fondos/fondo_dentro_juego.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    pantalla.blit(imagen, (0, 0)) 