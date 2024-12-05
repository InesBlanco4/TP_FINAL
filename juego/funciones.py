import pygame
import random


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

def cambiar_ranking(superficie:any):
    superficie.fill(BLANCO)    

def jugar_juego(superficie:any, cartas:list):
    superficie.fill(VERDE)
    x_inicio = 200
    y_inicio = 300
    espacio_x = 150
    for i, carta in enumerate(cartas):
        if carta["imagen"]:
            superficie.blit(carta["imagen"], (x_inicio + i * espacio_x, y_inicio))

def dar_inicio(ventana:any)->tuple:

    btn_1 = dibujar_boton(ventana, "Jugar", AZUL, (215,215,215), 100, 100)
    btn_2 = dibujar_boton(ventana, "Opciones", AZUL, (215,215,215), 100, 300)

    return btn_1, btn_2

def dibujar_boton(superficie: any, texto: str, color: tuple, texto_color: tuple,
                  x: int, y: int, ancho=200, alto=60):
    
    boton = pygame.Rect(x, y, ancho, alto)
    
    pygame.draw.rect(superficie, color, boton)
    fuente = pygame.font.SysFont("Arial", 20)
    superficie_texto = fuente.render(texto, True, texto_color)
    texto_color = superficie_texto.get_rect(center=boton.center)
    superficie.blit(superficie_texto, texto_color)

    return boton

def presionar_boton(boton: any, evento: any)->bool:
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if boton.collidepoint(evento.pos):
            return True
    return False


def textBlock(screen, text:str, pos:tuple, font_size:int=16, color:str="white"):
    font = pygame.font.Font("fonts/Gamilia.otf", font_size)
    text_surface = font.render(text, True, color)  # True para suavizar bordes (anti-aliasing)
    screen.blit(text_surface, pos)


isCardClicked = False

def btn(ventana, cord:tuple, text:str, callback:any)-> None:

    figura = pygame.draw.rect(ventana, "red", pygame.Rect(cord[0], cord[1], 150, 40))

    font = pygame.font.Font("fonts/Gamilia.otf", 16)
    text_surface = font.render(text, True, "white")  # True para suavizar bordes (anti-aliasing)
    
    file = pygame.image.load("imagenes/importante/boton.png") # BTN Texture
    texture = pygame.transform.scale(file, (figura.width, figura.height))
    ventana.blit(texture, figura.topleft)

    ventana.blit(text_surface, (figura.center[0] - text_surface.get_width() / 2, figura.center[1] - text_surface.get_height() / 2))
    
    
    global isCardClicked
    pos = pygame.mouse.get_pos()
    if figura.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if isCardClicked == False:
            if mouse_buttons[0]:
                callback()
                isCardClicked = True
        else:
            if mouse_buttons[0] == False:
                isCardClicked = False