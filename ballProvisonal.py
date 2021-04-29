import pygame as pg
import sys


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)


pg.init
pantalla = pg.display.set_mode((800,600))
pg.display.set_caption("Hola")

game_over = False
x = 400
y = 300
vx = -5 #Esta variable marca la velocidad de la bola
vy = -5

while not game_over:
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True
    
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    pg.draw.circle(pantalla, ROJO, (x, y), 10) #Dibuja el circulo en el centro de la pantalla como inicio, con su color y tamaño de su radio (10)
    x += vx #Estas coordenadas cambian cada vez que se recorre el bucle for, para que la bola esté cada vez en una posición nueva
    y += vy

    if y == 0: 
        vy = 5
    elif y == 600:
        vy = -5

    if x == 0: 
        vx = 5
    elif x == 800:
        vx = -5

    pg.display.flip() #Renderiza la pantalla


pg.quit()
sys.exit()