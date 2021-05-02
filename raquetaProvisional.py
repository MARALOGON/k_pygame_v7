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

class Raqueta():
    def __init__(self):

class Bola():
    def __init__(self, x, y, vx=5, vy=5, color=(255, 255, 255), radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

    def actualizar(self):
       self.x +=self.vx
       self.y +=self.vy
        
       if self.y <= 0 or self.y >= ALTO: 
            self.vy = -self.vy 
 
       if self.x <= 0 or self.x >= ANCHO: 
             self.vx = -self.vx
    

    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio) 
   


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
    bola.actualizar()
        
        

    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    bola.dibujar(pantalla)
        
   

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos


pg.quit()
sys.exit()