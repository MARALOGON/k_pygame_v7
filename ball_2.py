#Ejercicio con sprites. Este modulo de pygame permite tener hasta 9 coordenadas del objeto, con lo que será mas facil manejarlo por la pantalla

import pygame as pg
import sys, os
import random
from enum import Enum #Enum es una clase de pygame que sirve para crear diferentes estados, y luego poder enumerarlos

ANCHO = 800
ALTO = 600
FPS = 60
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

''' #Este lo dejamos comentado porque hemos creado otra clase Marcador alternativa 
class Marcador(pg.sprite.Sprite):

    class Justificado():
        izquierda = 'I'
        derecha = 'D'
        centro  = 'C'

    def __init__(self, x, y, justificado, fontsize=25, color=BLANCO):
        super().__init__()
        self.fuente = pg.font.Font(os.path.join('PTMono.ttc'), 30)
        self.text = "0"
        self.color = color
        self.x = x
        self.y = y
        if not justificado:
            self.justificado = Marcador.Justificado.izquierda
        else:
            self.justificado = justificado

        self.image = self.fuente.render(str(self.text), True, self.color)

        
    
    def update(self, dt): #La funcion update debe ir incluida en todas las clases
        self.image = self.fuente.render(str(self.text), True, self.color)

        ''' #Esta es una version normal con if para seleccionar donde vamos a poner los marcadores
        if self.justificado == Marcador.Justificado.izquierda:
            self.rect = self.image.get_rect(topleft=(self.x,self.y))
        elif self.justificado == Marcador.Justificado.derecha:
            self.rect = self.image.get_rect(topright=(self.x,self.y))
        else:
            self.rect = self.image.get_rect(midtop=(self.x,self.y))
        '''
'''

#Aqui vamos a crear una v ersion de la clase marcador mas reducida para el tema de los justificados de los marcadores
class MarcadorAlt(pg.sprite.Sprite):


    def __init__(self, x, y, justificado = 'topleft', fontsize=25, color=BLANCO):
        super().__init__()
        self.fuente = pg.font.Font(os.path.join('PTMono.ttc'), 30)
        self.text = "0"
        self.color = color
        self.x = x
        self.y = y
        self.justificado = justificado
        self.image = self.fuente.render(str(self.text), True, self.color)

        
    
    def update(self, dt): #La funcion update debe ir incluida en todas las clases
        self.image = self.fuente.render(str(self.text), True, self.color)
        dict = {self.justificado: (self.x, self.y)}
        self.rect = self.image.get_rect(**dict)


class Raqueta(pg.sprite.Sprite):
    disfraces = ['electric00.png', 'electric01.png', 'electric02.png']

    def __init__(self, x, y):
        super().__init__()
        self.imagenes = self.cargaImagenes()
        self.imagen_actual = 0
        self.milisegundos_para_cambiar = 1000 // FPS * 30
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
    disfraces = ['ball1.png','ball2.png', 'ball3.png', 'ball4.png', 'ball5.png']

    class EstadoBola(Enum): #Una clase puede estar dentro de otra clase, lo que se llama comoposicion de clases
        viva = 0
        agonizando = 1 
        muerta = 2
    
    def __init__(self, x, y):
       # pg.sprite.Sprite.__init__(self) Esta forma de llamar a la superclase o clase Padre Sprite es lo mismo que la forma de llamarla de la siguiente linea. Lo que hace es incializar esa clase por si tiene algun atributo que haya que inicializar y no lo sabemos
       super().__init__() #Inicializa la clase padre Sprite, igual que la linea de arriba
       self.imagenes = self.cargaImagenes()
       self.imagen_actual = 0
       self.image = self.imagenes[self.imagen_actual]
       self.milisegundos_acumulados = 0
       self.milisegundos_para_cambiar = 1000 // FPS * 10
       self.rect = self.image.get_rect(center=(x,y)) #Este get_rect devuelve un rectangulo del mismo tamaño (en este caso 30x30px) en el que está pintada la imagen que hemos cargado
       self.xOriginal = x
       self.yOriginal = y
       #self.estado = 0 # 0 = Bola viva, 1 - Bola agonizando (5 imagenes), 2 - Bola muerta
       self.estado = Bola.EstadoBola.viva


       self.vx = random.randint(5, 10) * random.choice([1, 1])
       self.vy = random.randint(5, 10) * random.choice([1, 1])
    
    def cargaImagenes(self):
        imagenes = []
        for fichero in self.disfraces:
            imagenes.append(pg.image.load("./images/{}".format(fichero)))
        return imagenes


    def prueba_colision(self, grupo):
        candidatos = pg.sprite.spritecollide(self, grupo, False)
        if len(candidatos) > 0:
            self.vy *= -1


    def update(self,dt):
        if self.estado == Bola.EstadoBola.viva:
            self.rect.x += self.vx
            self.rect.y += self.vy

            if self.rect.left <= 0 or self.rect.right >= ANCHO:
                self.vx *= -1
            if self.rect.top <= 0:
                self.vy *= -1

            if self.rect.bottom >= ALTO:
                self.estado = Bola.EstadoBola.agonizando
                self.rect.bottom = ALTO
        elif self.estado == Bola.EstadoBola.agonizando:
            self.milisegundos_acumulados += dt
            if self.milisegundos_acumulados >= self.milisegundos_para_cambiar:
                self.imagen_actual += 1
                self.milisegundos_acumulados = 0
                if self.imagen_actual >= len(self.disfraces):
                    self.estado = Bola.EstadoBola.muerta
                    self.imagen_actual = 0
                self.image = self.imagenes[self.imagen_actual]

        else: 
            self.rect.center = (self.xOriginal, self.yOriginal)
            self.vx = random.randint(5, 10) * random.choice([1, 1])
            self.vy = random.randint(5, 10) * random.choice([1, 1])
            self.estado = Bola.EstadoBola.viva

class Game():
    def __init__(self): #se crean los atributos de Game dentro de la funcion constructoria
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.vidas = 3
        self.todoGrupo = pg.sprite.Group()
        self.grupoJugador = pg.sprite.Group()
        self.grupoLadrillos = pg.sprite.Group()

        self.cuentaSegundos = Marcador(10,10)
        self.cuentaVidas = Marcador(790,10, "topright")
        self.todoGrupo.add(self.cuentaSegundos, self.cuentaVidas)

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
            self.cuentaVidas.text = self.vidas
            self.bola.prueba_colision(self.grupoJugador)
            self.todoGrupo.update(dt)
            if self.bola.estado == Bola.EstadoBola.muerta:
                self.vidas -=1
        
            self.pantalla.fill((0, 0, 0))
            self.todoGrupo.draw(self.pantalla)
            

            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game() #instancia Game
    game.bucle_principal() #llamar al juego, la clase game llama al resto de clases

