import pygame as pg
import sys


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600


pg.init
pantalla = pg.display.set_mode((ANCHO,ALTO))
pg.display.set_caption("Hola")

game_over = False
x = ANCHO // 2 # Se pone doble barra para que el resultado de la division sean solo numeros enteros, que nod e decimales
y = ALTO // 2
vx = -5 #Esta variable marca la velocidad de la bola
vy = -5
reloj = pg.time.Clock()

while not game_over:
    reloj.tick(60)
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True
    
    #Modificacion de estado
    x += vx #Estas coordenadas cambian cada vez que se recorre el bucle for, para que la bola esté cada vez en una posición nueva
    y += vy

    if y <= 0 or y >= ALTO: #Si la y es <= 0 rebota, es menor que la coordenada vertical superior, o es >= ALTO, es decir, es  mayor que la coordenada vertical inferior
        vy = -vy #Se iguala al negativo de la variable para que cuando rebote lo haga a la misma velocidad a la que iba, que se ha determinado fuera del while
    

    if x <= 0 or x >= ANCHO: #Si la x es <= 0 rebota, es menor que la coordenada horizontal izquierda, o x>= ANCHO, es decir, es mator que la coordenada horizontal derecha
        vx = -vx
    


    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    pg.draw.circle(pantalla, ROJO, (x, y), 10) #Dibuja el circulo en el centro de la pantalla como inicio, con su color y tamaño de su radio (10)
    

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos


pg.quit()
sys.exit()