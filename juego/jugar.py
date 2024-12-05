import pygame

def dibujar_fondo(ventana):
    info = pygame.display.Info()
    imagen = pygame.image.load("imagenes/importante/fondo_dentro_juego.png")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    ventana.blit(imagen, (0, 0)) 

carta_presionada = False
def dibujar_carta(ventana, coordenadas:tuple, cartas:dict):
    w, h = 80, 60

    #Dibujar el rectángulo de la carta
    carta_obj = pygame.draw.rect(
        ventana,
        "#FFFFFF00",
        pygame.Rect(coordenadas[0], coordenadas[1], w, h)
    )
    
    archivo = pygame.image.load(cartas["src"]) 
    textura = pygame.transform.scale(archivo, (carta_obj.width, 200))
    ventana.blit(textura, carta_obj.topleft)
    
    #Clicks

    global carta_presionada
    pos = pygame.mouse.get_pos()
    if carta_obj.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if carta_presionada == False:
            if mouse_buttons[0]:
                cartas.enviar_carta({"event":"cartas_send", "card":cartas})
                carta_presionada = True
        else:
            if mouse_buttons[0] == False:
                carta_presionada = False

def dibujar_mazo(ventana, cartas):
    info = pygame.display.Info()
    if len(cartas) == 3:
        dibujar_carta(ventana, (75, info.current_h - 80 - 60), cartas[0])
        dibujar_carta(ventana (75 + 130, info.current_h - 80 - 60), cartas[1])
        dibujar_carta(ventana, (225 + 110, info.current_h - 80 - 60), cartas[2])

def dibujar_mazo_rival(ventana, cartas):
    info = pygame.display.Info()
    if len(cartas) == 3:
        dibujar_carta(ventana, (500, info.current_h - 80 - 60), cartas[0])
        dibujar_carta(ventana, (500 + 60, info.current_h - 80 - 60), cartas[1])
        dibujar_carta(ventana, (560 + 120, info.current_h - 80 - 60), cartas[2])
        
def mostrar_cartas(ventana, cartas):
    # Mostrar las cartas en la pantalla
    x, y = 100, 100
    for carta_nombre, carta in cartas.items():
        imagen = carta["imagen"]
        if imagen:
            ventana.blit(imagen, (x, y))
            y += 100

# def inicio(ventana):

#     global en_juego
    
#     if en_juego == False:
#         cartas.mazo_usuario = cartas.cartas_aleatorias()
#         cartas.mazo_bot = cartas.cartas_aleatorias()
#         en_juego = True

        
#     dibujar_fondo(ventana)
#     dibujar_mazo(ventana, cartas.mazo_usuario)
#     dibujar_mazo(ventana, cartas.mazo_bot)

    #pygame.mixer.init()
    #pygame.mixer.music.load("recursos/sonidos/musica_partida.mp3")
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.1)