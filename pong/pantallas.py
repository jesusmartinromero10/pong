import pygame as pg
from pong.entities import Bola, Raqueta
from pong import ALTO, AMARILLO,ANCHO,BLANCO, NARANJA,NEGRO, FPS, COLOR2, PRIMER_AVISO, ROJO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA




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
        self.temporizador = TIEMPO_MAXIMO_PARTIDA
        self.fuente_marcador = pg.font.Font("pong/font/Silkscreen.ttf", 40)
        #self.fuente_cuenta = pg.font.Font("pong/font/Silkscreen.ttf", 20)
        self.fuenteTemporizador = pg.font.Font("pong/font/Silkscreen.ttf", 20)
        #self.cronometro2 = pg.time.Clock()
        self.color_fondo = NEGRO
        self.contador_fotograma = 0
        self.fondoPantalla = NEGRO

    
    def fijar_fondo(self):
        self.contador_fotograma += 1

        if self.temporizador > PRIMER_AVISO:
            self.contador_fotograma = 0
            
            
        elif self.temporizador > SEGUNDO_AVISO:
            if self.contador_fotograma == 10:
                if self.fondoPantalla == NEGRO:
                    self.fondoPantalla = NARANJA
                else:
                    self.fondoPantalla = NEGRO
                self.contador_fotograma = 0
            
            
            
        else:
            if self.contador_fotograma >= 5:
                if self.fondoPantalla == ROJO:
                    self.fondoPantalla = NEGRO
                else:
                    self.fondoPantalla = ROJO
                self.contador_fotograma = 0

        return self.fondoPantalla

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        cronometro = 0
        game_over = False
        velo1 = self.duracion * 1000 // 3
        velo2 = self.bola.vx * 1.5

        while not game_over and \
            self.puntuacion1 < 10 and \
            self.puntuacion2 < 10 and \
            self.temporizador > 0:
           
            salto_tiempo = self.metronomo.tick(FPS)
            self.temporizador -= salto_tiempo
            
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            

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


            

            
            self.pantalla_principal.fill(self.fijar_fondo())
            






            #cambio = self.duracion - cronometro / 1000
            """if self.temporizador < 3000:
                self.pantalla_principal.fill((ROJO))
                if self.temporizador < 2500:
                    self.pantalla_principal.fill((COLOR2))
                if self.temporizador < 2000:
                    self.pantalla_principal.fill((ROJO))
                if self.temporizador < 1500:
                    self.pantalla_principal.fill((COLOR2))
                if self.temporizador < 1000:
                    self.pantalla_principal.fill((ROJO))
                if self.temporizador < 500:
                    self.pantalla_principal.fill((COLOR2))
                    """
            
            
            self.bola.dibujar(self.pantalla_principal)

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            p1 = self.fuente_marcador.render(str(self.puntuacion1), True, BLANCO)
            self.pantalla_principal.blit(p1, (10,10))
            p2 = self.fuente_marcador.render(str(self.puntuacion2), True, BLANCO)
            
            self.pantalla_principal.blit(p2, (ANCHO - 50,10))
            contador = self.fuenteTemporizador.render(str(f"{self.temporizador / 1000}"), True, BLANCO)
            self.pantalla_principal.blit(contador, (ANCHO // 2,10))
            
           


            
            
            
            """if self.duracion - cronometro // 1000 > 10:
                pass
                print(self.bola.vx)
                
            elif self.duracion - cronometro // 1000 > 5:
                self.bola.vx = 3
                print(self.bola.vx)
                
            elif self.duracion - cronometro // 1000 < 5:
                self.bola.mover(vx = 4)
              
                print(self.bola.vx)
            """


            pg.display.flip()
