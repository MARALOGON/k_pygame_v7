import pygame as pg
import sys
from random import randint

def rebotaX(x): #Estas funciones sustituye a los if de las lineas 57 y 61, establece un cambio de direccion de la bola si toca con el borde. Se le cambia el signo (return -1), lo que es igual a que adquiere la misma velocidad en sentido contrario
    if x <= 0 or x >= ANCHO: 
        return -1
    
    return 1


def rebotaY(y):
    if y <= 0 or y >= ANCHO: 
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

bolas = []
for _ in range(10):
    bola = {'x': randint(0, ANCHO), 
            'y': randint(0, ALTO), 
            'vx': randint(5, 10), 
            'vy': randint(5, 10),
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
    
    }
    bolas.append(bola)

'''
#Bola 1
x = ANCHO // 2 # Se pone doble barra para que el resultado de la division sean solo numeros enteros, que nod e decimales
y = ALTO // 2
vx = -5 #Esta variable marca la velocidad de la bola
vy = -5

#Bola 2
x2 = randint(0, ANCHO)
y2 = randint(0, ALTO)
vx2 = randint(5, 15)
vy2 = randint(5, 15)

'''

game_over = False
while not game_over:
    reloj.tick(60)
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True
    
    #Modificacion de estado
    '''
    x += vx #Estas coordenadas cambian cada vez que se recorre el bucle for, para que la bola esté cada vez en una posición nueva
    y += vy
    x2 += vx2
    y2 += vy2
    '''
    for bola in bolas:
        bola['x'] += bola['vx']
        bola['y'] += bola['vy']

    #vy *= rebotaY(y) #Esta modificacion de estado de la variable vy va en relación de la funcion RebotaY  
        bola['vy'] *= rebotaY(bola['y'])
    #vx *= rebotaX(x)
        bola['vx'] *= rebotaX(bola['x'])

    #vy2 *= rebotaY(y2)
    #vx2 *= rebotaX(x2)

    '''
    if y <= 0 or y >= ALTO: #Si la y es <= 0 rebota, es menor que la coordenada vertical superior, o es >= ALTO, es decir, es  mayor que la coordenada vertical inferior
        vy = -vy #Se iguala al negativo de la variable para que cuando rebote lo haga a la misma velocidad a la que iba, que se ha determinado fuera del while
    

    if x <= 0 or x >= ANCHO: #Si la x es <= 0 rebota, es menor que la coordenada horizontal izquierda, o x>= ANCHO, es decir, es mator que la coordenada horizontal derecha
        vx = -vx
    
    '''

    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    for bola in bolas:
        pg.draw.circle(pantalla, bola['color'], (bola['x'], bola['y']), 10)
   
    # pg.draw.circle(pantalla, ROJO, (x, y), 10) #Dibuja el circulo en el centro de la pantalla como inicio, con su color y tamaño de su radio (10)
    
    # pg.draw.circle(pantalla, VERDE, (x2, y2), 10)

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos


pg.quit()
sys.exit()