import pygame as pg
import sys
from random import randint

def rebotaX(x): #Estas funciones sustituye a los if de las lineas 57 y 61, establece un cambio de direccion de la bola si toca con el borde. Se le cambia el signo (return -1), lo que es igual a que adquiere la misma velocidad en sentido contrario
    if x <= 0 or x >= ANCHO: 
        return -1
    
    return 1


def rebotaY(y):
    if y <= 0 or y >= ALTO: 
        return -1
    
    return 1


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600


pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        

bolas = []
for _ in range(10):
    bola = Bola(randint(0, ANCHO), #Sustuyo el diciionario bola por la instancia bola, que llama a la clase Bola
                randint(0, ALTO), 
                randint(5, 10), 
                randint(5, 10),
                (randint(0, 255), randint(0, 255), randint(0, 255)))

    '''
    bola = {'x': randint(0, ANCHO), 
            'y': randint(0, ALTO), 
            'vx': randint(5, 10), 
            'vy': randint(5, 10),
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
    }
    '''

    bolas.append(bola)


game_over = False
while not game_over:
    reloj.tick(60)
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True
    
    #Modificacion de estado
    for bola in bolas:
        
        bola.x += bola.vx
        bola.y += bola.vy

        bola.vy *= rebotaY(bola.y)
        bola.vx *= rebotaX(bola.x)
        
        '''
        bola['x'] += bola.vx
        bola.y += bola.vy

        bola.vy *= rebotaY(bola.y)
        bola.vx *= rebotaX(bola['x'])
       
        '''


    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
   

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos


pg.quit()
sys.exit()