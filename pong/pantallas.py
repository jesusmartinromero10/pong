import pygame as pg
from pong.entities import Bola, Raqueta
from pong import ALTO, AMARILLO,ANCHO,BLANCO,NEGRO, FPS, COLOR2, ROJO




pg.init()

class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Pong")
        self.metronomo = pg.time.Clock()

        self.bola = Bola(ANCHO//2, ALTO//2, color=BLANCO)
        self.raqueta1 = Raqueta(20, ALTO//2, color=(BLANCO))
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(ANCHO - 20, ALTO//2, color=(BLANCO))
        self.raqueta2.vy = 5
        self.duracion = 15
        self.puntuacion1 = 0
        self.puntuacion2 = 0 
        #self.cronometro = 0
        self.fuente_marcador = pg.font.Font("pong/font/Silkscreen.ttf", 40)
        self.fuente_cuenta = pg.font.Font("pong/font/Silkscreen.ttf", 20)
        self.cronometro2 = pg.time.Clock()
    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        cronometro = 0
        game_over = False
        velo1 = self.bola.vx * 1.2
        velo2 = self.bola.vx * 1.5

        while not game_over and \
            self.puntuacion1 < 10 and \
            self.puntuacion2 < 10:
           
            self.metronomo.tick(FPS)
            
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            if cronometro < 15000:
                
                cronometro += self.cronometro2.tick()
            elif cronometro > 1500:
                game_over = True
            
           
            
            print(cronometro)

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)

            quien = self.bola.mover()

            if quien == "RIGHT":
                self.puntuacion2 += 1
                
            elif quien == "LEFT":
                self.puntuacion1 += 1
            
            
            
            #if self.puntuacion1 > 9 or self.puntuacion2 > 9:
            #    game_over = True    
            self.bola.comprobar_choque(self.raqueta1, self.raqueta2)
            self.pantalla_principal.fill((NEGRO))
            cambio = self.duracion - cronometro / 1000
            if cambio < 3:
                self.pantalla_principal.fill((ROJO))
                if cambio < 2.5:
                    self.pantalla_principal.fill((COLOR2))
                if cambio < 2:
                    self.pantalla_principal.fill((ROJO))
                if cambio < 1.5:
                    self.pantalla_principal.fill((COLOR2))
                if cambio < 1:
                    self.pantalla_principal.fill((ROJO))
                if cambio < 0.5:
                    self.pantalla_principal.fill((COLOR2))
            
            
            self.bola.dibujar(self.pantalla_principal)

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            p1 = self.fuente_marcador.render(str(self.puntuacion1), True, BLANCO)
            self.pantalla_principal.blit(p1, (10,10))
            p2 = self.fuente_marcador.render(str(self.puntuacion2), True, BLANCO)
            
            self.pantalla_principal.blit(p2, (ANCHO - 50,10))
            contador = self.fuente_cuenta.render(str(f"{self.duracion - cronometro // 1000}"), True, BLANCO)
            self.pantalla_principal.blit(contador, (ANCHO - 400,10))
            
           


            
            
            if cronometro < 5000:
                pass
                print(self.bola.vx)
                
            elif cronometro < 10000:
                self.bola.mover(vx = 3)
                print(self.bola.vx)
                
            elif cronometro < 15000:
                self.bola.mover(vx = 4)
                print(self.bola.vx)
            


            pg.display.flip()
