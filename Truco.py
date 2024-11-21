import pygame
import pygame.mixer as mixer
from Funciones import *

mixer.init()
pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))

pygame.display.set_caption("Truco")

modalidad = 1
bandera = True
cartas = cargar_cartas()
cartas_repartidas = []

while bandera:

    if modalidad == 1: 
        btn_1, btn_2 = dar_inicio(ventana)
    elif modalidad == 2:
        cambiar_ranking(ventana)
    elif modalidad == 3:
        jugar_juego(ventana, cartas_repartidas)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        elif modalidad == 1 and presionar_boton(btn_1, evento):
            modalidad = 3
            cartas_repartidas = repartir_cartas(cartas, 3) 
            print("Cartas repartidas:", [carta for carta in cartas_repartidas])
        elif modalidad == 1 and presionar_boton(btn_2, evento):
            modalidad = 2

    pygame.display.update()

pygame.quit()
