
import pygame as pg
from pong import ALTO, ANCHO
from pong.pantallas import Menu, Partida

class Controlador:
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        metronomo = pg.time.Clock()
        self.pantallas = [Menu(pantalla_principal, metronomo), (Partida(pantalla_principal, metronomo))]

        self.menu = Menu(pantalla_principal, metronomo)
        self.partida = Partida(pantalla_principal, metronomo)
        #self.records = Records()
        
        
        
    def jugar(self):
        salida = False
        ix = 0
        while not salida:
            salida = self.pantallas[ix].bucle_ppal()
            
            
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0
                
            
            


