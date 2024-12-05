import pygame
import servicios.cartas as ServicioCartas
import juego.funciones as func

en_juego = False

carta1_pos = True
carta2_pos = True
carta3_pos = True

movimientos_usuario = [
]

movimientos_bot = [
]

turno = 1

def set_card_1():
    global carta1_pos
    global turno
    turno += 1
    carta1_pos = False
def set_card_2():
    global carta2_pos
    global turno
    turno += 1
    carta2_pos = False
def set_card_3():
    global carta3_pos
    global turno
    turno += 1
    carta3_pos = False

carta_presionada = False
def dibujar_carta(pantalla, coordenadas:tuple, cartas:dict, accion:any):
    w, h = 80, 100

    # Dibujar el rectángulo de la carta
    carta_obj = pygame.draw.rect(
        pantalla,
        "#FFFFFF00",
        pygame.Rect(coordenadas[0], coordenadas[1], w, h)
    )
    
    archivo = pygame.image.load(cartas["src"]) 
    textura = pygame.transform.scale(archivo, (carta_obj.width, carta_obj.height))
    pantalla.blit(textura, carta_obj.topleft)
    
    #Clicks

    global carta_presionada
    pos = pygame.mouse.get_pos()
    if carta_obj.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if carta_presionada == False:
            if mouse_buttons[0]:
                accion()
                movimientos_usuario.append(cartas)
                carta_presionada = True
        else:
            if mouse_buttons[0] == False:
                carta_presionada = False

def dibujar_mazo(pantalla, nuevas_cartas):
    info = pygame.display.Info()
    if len(nuevas_cartas) == 3:
        
        global carta1_pos
        global carta2_pos
        global carta3_pos

        global movimientos_usuario
        global movimientos_bot
        global turno 
 
        if len(movimientos_usuario) == 1 and turno == 2:
            movimientos_bot.append(ServicioCartas.mazo_bot[0])
            turno += 1
        if len(movimientos_usuario) == 2 and turno == 4:
            movimientos_bot.append(ServicioCartas.mazo_bot[2])
            turno += 1
        if len(movimientos_usuario) == 3 and turno == 6:
            movimientos_bot.append(ServicioCartas.mazo_bot[1])
            turno += 1

        
        if carta1_pos: dibujar_carta(pantalla, (75, info.current_h - 120 - 10), nuevas_cartas[0], lambda: set_card_1())
        if carta2_pos: dibujar_carta(pantalla, (75 + 130, info.current_h - 120 - 10), nuevas_cartas[1], lambda: set_card_2())
        if carta3_pos: dibujar_carta(pantalla, (225 + 110, info.current_h - 120 - 10), nuevas_cartas[2], lambda: set_card_3())
        
        bot_start_pos = (277, 76)
        usuario_start_pos = (277, 196)
        i = 0
        
        
        for carta_ganadora in movimientos_usuario:
            dibujar_carta(pantalla, (usuario_start_pos[0] + 90 * i, usuario_start_pos[1]), carta_ganadora, lambda: print("xd"))
            dibujar_carta(pantalla, (bot_start_pos[0] + 90 * i, bot_start_pos[1]), ServicioCartas.mazo_bot[i], lambda: print("xd"))
            
            if carta_ganadora["valor"] > ServicioCartas.mazo_bot[i]["valor"]:
                func.textBlock(pantalla, "Ganaste", (usuario_start_pos[0] + 90 * i, 300), 16, "#3FFE3F")
            elif carta_ganadora["valor"] == ServicioCartas.mazo_bot[i]["valor"]:
                func.textBlock(pantalla, "Empardaste", (usuario_start_pos[0] + 90 * i, 300), 16, "#3F3F3F")
            else:
                func.textBlock(pantalla, "Perdiste", (usuario_start_pos[0] + 90 * i, 300), 16, "#3FFEFE")
            i += 1 


def draw_basic_ui(screen)-> None:
    info = pygame.display.Info()
    pygame.draw.rect(screen, "#1A1A1A", pygame.Rect(0, 0, info.current_w, info.current_h))
    

def comienzo(screen):
    global in_game
    
    global en_juego
    
    if en_juego == False:
        ServicioCartas.mazo_usuario = ServicioCartas.cartas_aleatorias()
        ServicioCartas.mazo_bot = ServicioCartas.cartas_aleatorias()

        en_juego = True
        in_game = False

    draw_basic_ui(screen)
    dibujar_mazo(screen, ServicioCartas.mazo_usuario)