import pygame as pg
import sys
from random import randint, choice


ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ANCHO = 800
ALTO = 600



pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))
fuente = pg.font.Font(None, 50)
fuente2 = pg.font.Font(None, 50)
reloj = pg.time.Clock()




class Bola():
    def __init__(self, x, y, vx=5, vy=5, color=(255, 255, 255), radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.anchura = radio * 2
        self.altura = radio * 2

    def actualizar(self):
        self.x +=self.vx
        self.y +=self.vy
        
        if self.y <= 0: 
            self.vy = -self.vy 
 
        if self.x <= 0 or self.x >= ANCHO: 
             self.vx = -self.vx

        if self.y >= ALTO:
            self.x = ANCHO // 2
            self.y = ALTO // 2
            self.vx = randint(5,10) * choice((-1, 1))
            self.vy = randint(5,10) * choice((-1, 1))
        
            return True
        return False

    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.anchura//2) 
   
    def comprueba_colision(self, objeto):
        
        choqueX = self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
           self.x + self.anchura >= objeto.x and self.x + self.anchura <= objeto.x + objeto.anchura
        choqueY = self.y >= objeto.y and self.y <= objeto.y + objeto.altura or \
           self.y + self.altura >= objeto.y and self.y + self.altura <= objeto.y + objeto.altura
        
        if choqueX and choqueY:
            self.vy *= -1
            
            
            


class Raqueta():
    def __init__(self, x=0, y=0):   
        self.altura = 10
        self.anchura = 100
        self.color = (255, 255, 255)
        self.x = (ANCHO - self.anchura) // 2
        self.y = ALTO - self.altura - 15
        self.vy = 0
        self.vx = 10

    def dibujar(self, lienzo):
        rect = pg.Rect(self.x, self.y, self.anchura, self.altura)   #Clase rectangulo de Pygame
        pg.draw.rect(lienzo, self.color, rect)


    def actualizar(self):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT] and self.x > 0:
            self.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT] and self.x < ANCHO - self.anchura:
            self.x += self.vx
        
class Game():
    def __init__(self, x, y, color, font):
        self.x = x
        self.y = y
        self.texto = texto
        self.color = color
        
    
    #def contador_vidas(self, x = 10, y = 10, color = BLANCO):
        
    

puntos = 0
vidas = 3
bola = Bola(randint(0, ANCHO), #Sustuyo el diciionario bola por la instancia bola, que llama a la clase Bola
    randint(0, ALTO), 
    randint(5, 10) * choice([-1, 1]), #choice es un metodo de la clase random para elegir valores al azar
    randint(5, 10) * choice([-1, 1]),
    (randint(0, 255), randint(0, 255), randint(0, 255)))


raqueta = Raqueta()


game_over = False
while not game_over:
    reloj.tick(30)
    # Gestion de eventos
    for evento in pg.event.get(): #Bucle con instruccion tipo de pygame para la gestión de eventos 
        if evento.type == pg.QUIT:
            game_over = True



    #Modificacion de estado
    pierdebola = bola.actualizar()
    raqueta.actualizar()
    bola.comprueba_colision(raqueta)
    #bola.comprueba_colision(objeto)
    texto_puntos = fuente2.render("Puntos: " + str(puntos), True, ROJO)
    texto_vidas = fuente2.render("Vidas: " + str(vidas), True, VERDE)
    texto_gameover = fuente2.render("Game Over", True, ROJO)  
    if vidas == 0:
        pantalla.blit(texto_gameover, True, (ANCHO // 2, ALTO //2)) 

   

    # Gestion de la pantalla
    pantalla.fill(NEGRO) #Pinta la pantalla de negro antes de cada movimiento
    bola.dibujar(pantalla)
    raqueta.dibujar(pantalla)
    pantalla.blit(texto_puntos, (600, 10))
    pantalla.blit(texto_vidas, (30,10))
   

    
   

    pg.display.flip() #Renderiza la pantalla y muestra los cambios producidos por los eventos
    if pierdebola:
        pg.time.delay(1000)
        vidas -= 1
    
        #pg.time.delay(2000)
        #quit()
        

pg.quit()
sys.exit()