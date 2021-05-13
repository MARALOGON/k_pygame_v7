from arkanoid import ANCHO, ALTO, FPS, BLANCO, ROJO, levels
from arkanoid.entities import MarcadorAlt, Bola, Raqueta, Ladrillo
import pygame as pg
import random
import sys



class Scene():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.todoGrupo = pg.sprite.Group()
        self.reloj = pg.time.Clock()
    
    def maneja_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or \
                evento.type == pg.KEYDOWN and evento.key == pg.K_q:
                    pg.quit() 
                    sys.exit()
        
        return False
    
    def reset(self):
        pass

    def bucle_principal(self):
        pass
        ''' #Esto es lo mismo que el pass de arriba
        while True:
            self.maneja_eventos()
            self.todoGrupo.update(dt)
            self.todoGrupo.draw(self.pantalla)
            pg.display.flip()
        '''



class Game(Scene):
    def __init__(self, pantalla): #se crean los atributos de Game dentro de la funcion constructoria
        super().__init__(pantalla)
        self.grupoJugador = pg.sprite.Group()
        self.grupoLadrillos = pg.sprite.Group()
       

        self.disponer_ladrillos(levels[self.level])

        self.cuentaPuntos = MarcadorAlt(10,10)
        self.cuentaVidas = MarcadorAlt(790,10, "topright") #Metiendo aqui la llamada a la Clase Cuentavidas conseguimos que la clase Game no tenga mas responsabilidad con el marcador que informar 
        self.cuentaVidas.plantilla = "Vidas: {}"
        self.fondo = pg.image.load("./images/background.png")

        self.bola = Bola(ANCHO // 2, ALTO // 2)
        self.todoGrupo.add(self.bola)
        
        self.raqueta = Raqueta(x = ANCHO//2, y = ALTO - 40)
        self.grupoJugador.add(self.raqueta)

        self.reset()

        self.todoGrupo.add(self.grupoJugador, self.grupoLadrillos)

    def reset(self):
        self.vidas = 3
        self.puntuacion = 0
        self.level = 0
        self.todoGrupo.remove(self.grupoLadrillos)
        self.grupoLadrillos.empty()
        self.disponer_ladrillos(levels(self.level))
        self.todoGrupo.add(self.grupoLadrillos)
        self.todoGrupo.remove(self.cuentaPuntos, self.cuentaVidas)
        self.todoGrupo.add(self.cuentaPuntos, self.cuentaVidas)


    #En esta funcion se crean las filas y columnas de ladrillos segun el mapa de level1
    def disponer_ladrillos(self, level): 
        for fila, cadena in enumerate(level):
            for columna, caracter in enumerate(cadena):
                if caracter in "XD":
                    x = 5 + (100 * columna)
                    y = 5 + (40 * fila)
                    ladrillo = Ladrillo(x, y, caracter == 'D')
                    self.grupoLadrillos.add(ladrillo)
                    
              
    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        while not game_over and self.vidas >0:
            dt = reloj.tick(FPS)

            for evento in pg.event.get():
                if evento.type == pg.QUIT or\
                    evento.type == pg.KEYDOWN and evento.key == pg.K_q:
                        pg.quit() 
                        sys.exit()

            self.cuentaPuntos.text = self.puntuacion
            self.cuentaVidas.text = self.vidas
            self.bola.prueba_colision(self.grupoJugador)
            tocados = self.bola.prueba_colision(self.grupoLadrillos)
            for ladrillo in tocados:
                self.puntuacion += 5
                if ladrillo.desaparece():
                    self.grupoLadrillos.remove(ladrillo)
                    self.todoGrupo.remove(ladrillo)
                    if len(self.grupoLadrillos) == 0:
                        self.level += 1
                        self.disponer_ladrillos(levels(self.level))
                        self.todoGrupo.add(self.grupoLadrillos)

            self.todoGrupo.update(dt)
            if self.bola.estado == Bola.EstadoBola.muerta:
                self.vidas -=1
        
            self.pantalla.blit(self.fondo, (0,0))
            self.todoGrupo.draw(self.pantalla)
            

            pg.display.flip()

class Portada(Scene):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.instrucciones = MarcadorAlt(ANCHO // 2, ALTO // 2, "center", 50, BLANCO)
        self.instrucciones.text = "Pulsa espacio para jugar"
        self.todoGrupo.add(self.instrucciones)


    def bucle_principal(self):
        game_over = False
        while not game_over:
            dt = self.reloj.tick(FPS)


            self.maneja_eventos

            teclas_pulsadas = pg.key.get_pressed()
            if teclas_pulsadas[pg.K_SPACE]:
                game_over = True

            self.todoGrupo.update(dt)
            self.pantalla.fill((0, 0, 0))
            self.todoGrupo.draw(self.pantalla)

            pg.display.flip()

