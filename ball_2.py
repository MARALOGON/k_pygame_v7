#Ejercicio con sprites. Este modulo de pygame permite tener hasta 9 coordenadas del objeto, con lo que será mas facil manejarlo por la pantalla

import pygame as pg
import sys, os
import random


ANCHO = 800
ALTO = 600
FPS = 60
BLANCO = (255, 255, 255)

class Marcador():
    def __init__(self, x, y, fontsize=25, color=BLANCO):
        self.fuente = pg.font.SysFont('PTMono.ttc', 30)
        self.x = x
        self.y = y
        self.color = color
    
    def dibuja(self, text, lienzo):
        image = self.fuente.render(str(text), True, self.color)
        lienzo.blit(image, (self.x, self.y))


class Bola(pg.sprite.Sprite):
    def __init__(self, x, y):
       # pg.sprite.Sprite.__init__(self) Esta forma de llamar a la superclase Bola es lo mismo que la forma de llamarla de la siguiente linea
       super().__init__()
       self.image = pg.image.load('./images/ball1.png').convert_alpha()
       self.rect = self.image.get_rect(center=(x,y)) #Este get_rect devuelve un rectangulo del mismo tamaño (en este caso 30x30px) en el que está pintada la imagen que hemos cargado

       self.vx = random.randint(5, 10) * random.choice([1, 1])
       self.vy = random.randint(5, 10) * random.choice([1, 1])



    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.vy *= -1

class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.botes = 0
        self.cuentaGolpes = Marcador(10,10)

        self.ballGroup = pg.sprite.Group()
        for i in range(random.randint(1, 25)):
            bola = Bola(random.randint(0, ANCHO), random.randint(0, ALTO))
            self.ballGroup.add(bola)


        self.bola = Bola(ANCHO//2, ALTO//2)

    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        while not game_over:
            reloj.tick(FPS)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.ballGroup.update()
        
            self.pantalla.fill((0, 0, 0))
            self.cuentaGolpes.dibuja('Hola', self.pantalla)
            self.ballGroup.draw(self.pantalla)
            

            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()

