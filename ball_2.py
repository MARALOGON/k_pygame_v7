#Ejercicio con sprites. Este modulo de pygame permite tener hasta 9 coordenadas del objeto, con lo que será mas facil manejarlo por la pantalla

import pygame as pg
import sys, os
import random


ANCHO = 800
ALTO = 600
FPS = 60
BLANCO = (255, 255, 255)

class Marcador(pg.sprite.Sprite):
    def __init__(self, x, y, fontsize=25, color=BLANCO):
        super().__init__()
        self.fuente = pg.font.SysFont('PTMono.ttc', 30)
        self.text = "0"
        self.color = color
        self.image = self.fuente.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect(topleft=(x,y))
        
    
    def update(self):
        self.image = self.fuente.render(str(self.text), True, self.color)


class Bola(pg.sprite.Sprite):
    def __init__(self, x, y):
       # pg.sprite.Sprite.__init__(self) Esta forma de llamar a la superclase o clase Padre Sprite es lo mismo que la forma de llamarla de la siguiente linea. Lo que hace es incializar esa clase por si tiene algun atributo que haya que inicializar y no lo sabemos
       super().__init__() #Inicializa la clase padre Sprite, igual que la linea de arriba
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
        self.cuentaSegundos = Marcador(10,10)

        self.todoGrupo = pg.sprite.Group()
        for i in range(random.randint(1, 25)):
            bola = Bola(random.randint(0, ANCHO), random.randint(0, ALTO))
            self.todoGrupo.add(bola)
        self.todoGrupo.add(self.cuentaSegundos)

    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        contador_milisegundos = 0
        segundero = 0
        while not game_over:
            dt = reloj.tick(FPS)
            contador_milisegundos += dt

            if contador_milisegundos >= 1000:
                segundero += 1
                contador_milisegundos = 0

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.cuentaSegundos.text = segundero
            self.todoGrupo.update()
        
            self.pantalla.fill((0, 0, 0))
            self.todoGrupo.draw(self.pantalla)
            

            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()

