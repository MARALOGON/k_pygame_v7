import pygame as pg
import sys
from random import randint, choice




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

    def rebota(self):
        if self.y <= 0 or self.y >= ALTO: 
            self vy = -self.vy 
 
        if self.x <= 0 or self.x >= ANCHO: 
             self vx = -self.vx
    
   

bolas = []
for _ in range(10):
    bola = Bola(randint(0, ANCHO), #Sustuyo el diciionario bola por la instancia bola, que llama a la clase Bola
                randint(0, ALTO), 
                randint(5, 10) * choice([-1, 1]), #choice es un metodo de la clase random para elegir valores al azar
                randint(5, 10) * choice([-1, 1]),
                (randint(0, 255), randint(0, 255), randint(0, 255)))

    bolas.append(bola)


game_over = False
while not game_over:
    reloj.tick(30)
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True
    
    #Modificacion de estado
    for bola in bolas:
        
        bola.x += bola.vx
        bola.y += bola.vy

        bola.rebota()

    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
   

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos


pg.quit()
sys.exit()