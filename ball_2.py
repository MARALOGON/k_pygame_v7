#Ejercicio con sprites. Este modulo de pygame permite tener hasta 9 coordenadas del objeto, con lo que será mas facil manejarlo por la pantalla

import pygame as pg
import sys, os
import random


ANCHO = 800
ALTO = 600
FPS = 60
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

class Marcador(pg.sprite.Sprite):
    def __init__(self, x, y, fontsize=25, color=BLANCO):
        super().__init__()
        self.fuente = pg.font.SysFont('PTMono.ttc', 30)
        self.text = "0"
        self.color = color
        self.image = self.fuente.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect(topleft=(x,y))
        
    
    def update(self, dt):
        self.image = self.fuente.render(str(self.text), True, self.color)

class Raqueta(pg.sprite.Sprite):
    disfraces = ['electric00.png', 'electric01.png', 'electric02.png']

    def __init__(self, x, y):
        super().__init__()
        self.imagenes = self.cargaImagenes()
        self.imagen_actual = 0
        self.milisegundos_para_cambiar = 1000 // FPS * 60
        self.milisegundos_acumulados = 0
        self.image = self.imagenes[self.imagen_actual]

        self.rect = self.image.get_rect(centerx = x, bottom = y)
        self.vx = 7
    
    def cargaImagenes(self):
        imagenes = []
        for fichero in self.disfraces:
            imagenes.append(pg.image.load("./images/{}".format(fichero)))
        return imagenes


    def update(self, dt):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.vx

        if teclas_pulsadas[pg.K_RIGHT]:
            self.rect.x += self.vx
        
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO

        self.milisegundos_acumulados += dt
        if self.milisegundos_acumulados >= self.milisegundos_para_cambiar:
            self.imagen_actual += 1
            if self.imagen_actual >= len(self.disfraces):
                self.imagen_actual = 0
            self.milisegundos_acumulados = 0
        self.image = self.imagenes[self.imagen_actual]


class Bola(pg.sprite.Sprite):
    def __init__(self, x, y):
       # pg.sprite.Sprite.__init__(self) Esta forma de llamar a la superclase o clase Padre Sprite es lo mismo que la forma de llamarla de la siguiente linea. Lo que hace es incializar esa clase por si tiene algun atributo que haya que inicializar y no lo sabemos
       super().__init__() #Inicializa la clase padre Sprite, igual que la linea de arriba
       self.image = pg.image.load('./images/ball1.png').convert_alpha()
       self.rect = self.image.get_rect(center=(x,y)) #Este get_rect devuelve un rectangulo del mismo tamaño (en este caso 30x30px) en el que está pintada la imagen que hemos cargado
       self.xOriginal = x
       self.yOriginal = y
       self.estoyViva = True

       self.vx = random.randint(5, 10) * random.choice([1, 1])
       self.vy = random.randint(5, 10) * random.choice([1, 1])
    
    def prueba_colision(self, grupo):
        candidatos = pg.sprite.spritecollide(self, grupo, False)
        if len(candidatos) > 0:
            self.vy *= -1



    def update(self,dt):
        if self.estoyViva:
            self.rect.x += self.vx
            self.rect.y += self.vy

            if self.rect.left <= 0 or self.rect.right >= ANCHO:
                self.vx *= -1
            if self.rect.top <= 0:
                self.vy *= -1

            if self.rect.bottom >= ALTO:
                self.estoyViva = False

        else: 
            self.rect.center = (self.xOriginal, self.yOriginal)
            self.vx = random.randint(5, 10) * random.choice([1, 1])
            self.vy = random.randint(5, 10) * random.choice([1, 1])
            self.estoyViva = True

class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.vidas = 3
        self.todoGrupo = pg.sprite.Group()
        self.grupoJugador = pg.sprite.Group()
        self.grupoLadrillos = pg.sprite.Group()

        self.cuentaSegundos = Marcador(10,10)
        self.todoGrupo.add(self.cuentaSegundos)

        self.bola = Bola(ANCHO // 2, ALTO // 2)
        self.todoGrupo.add(self.bola)
        
        self.raqueta = Raqueta(x = ANCHO//2, y = ALTO - 40)
        self.grupoJugador.add(self.raqueta)

        self.todoGrupo.add(self.grupoJugador, self.grupoLadrillos)


    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        contador_milisegundos = 0
        segundero = 0
        while not game_over and self.vidas >0:
            dt = reloj.tick(FPS)
            contador_milisegundos += dt


            if contador_milisegundos >= 1000:
                segundero += 1
                contador_milisegundos = 0

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.cuentaSegundos.text = segundero
            self.bola.prueba_colision(self.grupoJugador)
            self.todoGrupo.update(dt)
            if not self.bola.estoyViva:
                self.vidas -=1
        
            self.pantalla.fill((0, 0, 0))
            self.todoGrupo.draw(self.pantalla)
            

            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()

