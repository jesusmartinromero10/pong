from curses import KEY_UP
import pygame as pg
from entities import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))

pg.display.set_caption("Pong")
cronometro = pg.time.Clock()

game_over = False
bola = Bola(400, 300, color=(255,255,255))
bola.vx = 5
bola.vy = 5
raqueta1 = Raqueta(20, 300, color=(255,255,255))
raqueta2 = Raqueta(780, 300, color=(255,255,255))
raqueta2.vy = 5
raqueta1.vy = 5


while not game_over:
    dt = cronometro.tick(60)
    print(dt)
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
       
    
    


    pantalla_principal.fill((0, 0, 0))

    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    bola.mover()

    if bola.izquierda <= raqueta1.derecha and bola.abajo >= raqueta1.arriba and bola.arriba <= raqueta1.abajo and bola.izquierda >= raqueta1.izquierda:
        bola.vx *= -1
        
    if bola.derecha >= raqueta2.izquierda and bola.abajo >= raqueta2.arriba and bola.arriba <= raqueta2.abajo and bola.derecha <= raqueta2.derecha:
        bola.vx *= -1


    pg.display.flip()
