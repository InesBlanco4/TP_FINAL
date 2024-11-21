import pygame
import random
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

def cambiar_ranking(superficie:any):
    superficie.fill(BLANCO)    

def jugar_juego(superficie:any):
    superficie.fill(VERDE)
    x_inicio = 200
    y_inicio = 300
    espacio_x = 150
    for i, carta in enumerate(cartas_repartidas):
        if carta["imagen"]:
            superficie.blit(carta["imagen"], (x_inicio + i * espacio_x, y_inicio))

def dar_inicio(pantalla:any)->tuple:

    btn_1 = dibujar_boton(pantalla, "Jugar", AZUL, (215,215,215), 100, 100)
    btn_2 = dibujar_boton(pantalla, "Opciones", AZUL, (215,215,215), 100, 300)

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

def repartir_cartas(cartas: dict, cantidad: int) -> list:
    """
    Selecciona aleatoriamente `cantidad` de cartas del diccionario `cartas`.
    """
    return random.sample(list(cartas.values()), cantidad)