from arkanoid import ANCHO, ALTO, FPS, BLANCO, ROJO
import pygame as pg
import random
from enum import Enum



class MarcadorAlt(pg.sprite.Sprite):
    plantilla = "{}"

    def __init__(self, x, y, justificado = 'topleft', fontsize=25, color=BLANCO):
        super().__init__()
        self.fuente = pg.font.Font(('./PTMono.ttc'), 30)
        self.text = ""
        self.color = color
        self.x = x
        self.y = y
        self.justificado = justificado
        self.image = None
        self.rect = None

        
    
    def update(self, dt): #La funcion update debe ir incluida en todas las clases
        self.image = self.fuente.render(self.plantilla.format(self.text), True, self.color)
        dict = {self.justificado: (self.x, self.y)}
        self.rect = self.image.get_rect(**dict)

class Ladrillo(pg.sprite.Sprite):
    disfraces = ['greenTile.png', 'redTile.png', 'redTileBreak.png']

    def __init__(self, x, y, esDuro=False):
        super().__init__()
        self.imagenes = self.cargaImagenes()
        self.esDuro = esDuro
        self.imagen_actual = 1 if self.esDuro else 0
        self.image = self.imagenes[self.imagen_actual]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.numGolpes = 0


    def cargaImagenes(self):
        imagenes = []
        for fichero in self.disfraces:
            imagenes.append(pg.image.load("./images/{}".format(fichero)))
        return imagenes


    def update(self, dt):
        if self.esDuro and self.numGolpes == 1:
            self.imagen_actual = 2
            self.image = self.imagenes[self.imagen_actual]


    def desaparece(self):
        self.numGolpes += 1
        return self.numGolpes > 0 and not self.esDuro or self.numGolpes > 1 and self.esDuro

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
        self.vx = 10
    
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
        return candidatos

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

