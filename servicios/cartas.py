import random

mazo_usuario = []
mazo_bot = []
#diccionario
cartas_truco = [
    {"carta": "1 de espada", "valor": 14, "src": "imagenes/Cartas/1 de espada.jpg"},
    {"carta": "1 de basto", "valor": 13, "src": "imagenes/Cartas/1 de basto.jpg"},
    
    {"carta": "7 de espada", "valor": 12, "src": "imagenes/Cartas/7 de espada.jpg"},
    {"carta": "7 de oro", "valor": 11, "src": "imagenes/Cartas/7 de oro.jpg"},
    
    {"carta": "3 de espada", "valor": 10, "src": "imagenes/Cartas/3 de espada.jpg"},
    {"carta": "3 de basto", "valor": 10, "src": "imagenes/Cartas/3 de basto.jpg"},
    {"carta": "3 de oro", "valor": 10, "src": "imagenes/Cartas/3 de oro.jpg"},
    {"carta": "3 de copa", "valor": 10, "src": "imagenes/Cartas/3 de copa.jpg"},
    
    {"carta": "2 de espada", "valor": 9, "src": "imagenes/Cartas/2 de espada.jpg"},
    {"carta": "2 de basto", "valor": 9, "src": "imagenes/Cartas/2 de basto.jpg"},
    {"carta": "2 de copa", "valor": 9, "src": "imagenes/Cartas/2 de copa.jpg"},
    {"carta": "2 de oro", "valor": 9, "src": "imagenes/Cartas/2 de oro.jpg"},
    
    {"carta": "1 de copa", "valor": 8, "src": "imagenes/Cartas/1 de copa.jpg"},
    {"carta": "1 de oro", "valor": 8, "src": "imagenes/Cartas/1 de oro.jpg"},
    
    {"carta": "12 de copa", "valor": 7, "src": "imagenes/Cartas/12 de copa.jpg"},
    {"carta": "12 de espada", "valor": 7, "src": "imagenes/Cartas/12 de espada.jpg"},
    {"carta": "12 de basto", "valor": 7, "src": "imagenes/Cartas/12 de basto.jpg"},
    {"carta": "12 de oro", "valor": 7, "src": "imagenes/Cartas/12 de oro.jpg"},
    
    {"carta": "11 de copa", "valor": 6, "src": "imagenes/Cartas/11 de copa.jpg"},
    {"carta": "11 de espada", "valor": 6, "src": "imagenes/Cartas/11 de espada.jpg"},
    {"carta": "11 de basto", "valor": 6, "src": "imagenes/Cartas/11 de basto.jpg"},
    {"carta": "11 de oro", "valor": 6, "src": "imagenes/Cartas/11 de oro.jpg"},
    
    {"carta": "10 de copa", "valor": 5, "src": "imagenes/Cartas/10 de copa.jpg"},
    {"carta": "10 de espada", "valor": 5, "src": "imagenes/Cartas/10 de espada.jpg"},
    {"carta": "10 de basto", "valor": 5, "src": "imagenes/Cartas/10 de basto.jpg"},
    {"carta": "10 de oro", "valor": 5, "src": "imagenes/Cartas/10 de oro.jpg"},
    
    {"carta": "7 de copa", "valor": 4, "src": "imagenes/Cartas/7 de copa.jpg"},
    {"carta": "7 de basto", "valor": 4, "src": "imagenes/Cartas/7 de basto.jpg"},
    
    {"carta": "6 de espada", "valor": 3, "src": "imagenes/Cartas/6 de espada.jpg"},
    {"carta": "6 de basto", "valor": 3, "src": "imagenes/Cartas/6 de basto.jpg"},
    {"carta": "6 de copa", "valor": 3, "src": "imagenes/Cartas/6 de copa.jpg"},
    {"carta": "6 de oro", "valor": 3, "src": "imagenes/Cartas/6 de oro.jpg"},
    
    {"carta": "5 de espada", "valor": 2, "src": "imagenes/Cartas/5 de espada.jpg"},
    {"carta": "5 de basto", "valor": 2, "src": "imagenes/Cartas/5 de basto.jpg"},
    {"carta": "5 de copa", "valor": 2, "src": "imagenes/Cartas/5 de copa.jpg"},
    {"carta": "5 de oro", "valor": 2, "src": "imagenes/Cartas/5 de oro.jpg"},
    
    {"carta": "4 de espada", "valor": 1, "src": "imagenes/Cartas/4 de espada.jpg"},
    {"carta": "4 de basto", "valor": 1, "src": "imagenes/Cartas/4 de basto.jpg"},
    {"carta": "4 de copa", "valor": 1, "src": "imagenes/Cartas/4 de copa.jpg"},
    {"carta": "4 de oro", "valor": 1, "src": "imagenes/Cartas/4 de oro.jpg"},
]

def cartas_aleatorias():
    
    cartas_en_juego = []
    cartas_cargadas = cartas_truco
    
    for carta in range(3):  
        try:
            indice_random = random.randrange(0, len(cartas_cargadas))
            carta_seleccionada = cartas_cargadas[indice_random]
            cartas_en_juego.append(carta_seleccionada)
        
            cartas_cargadas.pop(indice_random)

        except:
            print(len(cartas_cargadas))
        
    return cartas_en_juego

