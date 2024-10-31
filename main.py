import pygame as pg
import numpy as np
import os
from config import *

pg.init()

class Settings:                                                         
    def __init__(self):                                                
        self.clock = pg.time.Clock()                               
        self.display_mode = (WIDTH, HEIGHT)                    
        self.screen = pg.display.set_mode(self.display_mode)      

        self.display_color = (0, 0, 0)                                 
        self.directory = os.path.dirname(__file__)                      
        self.game_active = True                                         
        #*self.type_cursor = pg.mouse.set_visible(False)

        self.frame = np.random.uniform(0, 1, (HRES, HALFVRES * 2, 3))

        self.go_up = False
        self.go_down = False
        self.go_left = False
        self.go_right = False

set = Settings()

def move(posx, posy, rot, keys):
    if keys[pg.K_UP] or keys[ord('w')]:
        posx, posy = posx + np.cos(rot) * 0.1, posy + np.sin(rot) * 0.1
    if keys[pg.K_DOWN] or keys[ord('s')]:
       posx, posy = posx - np.cos(rot) * 0.1, posy + np.sin(rot) * 0.1
    if keys[pg.K_LEFT] or keys[ord('a')]:
        rot = rot - 0.1
    if keys[pg.K_RIGHT] or keys[ord('d')]:
        rot = rot + 0.1

    return posx, posy, rot

while set.game_active:

    POSX, POSY, ROT = move(POSX, POSY, ROT, pg.key.get_pressed())

    for event in pg.event.get():
        if event.type == pg.QUIT:
            set.game_active = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_TAB and pg.K_ESCAPE:
                 set.game_active = False

    #! Ray-casting         

    for i in range(HRES):
        rot_i = ROT + np.deg2rad(i / MOD - 30)
        sin, cos = np.sin(rot_i), np.cos(rot_i)

        for j in range(HALFVRES):
            n = HALFVRES / (HALFVRES - j)
            x, y = POSX + cos * n, POSY + sin * n

            if int(x) % 2 == int(y) % 2:
                set.frame[i][HALFVRES * 2 - j - 1] = [0, 0, 0]
            else :
                set.frame[i][HALFVRES * 2 - j - 1] = [1, 1, 1]
    
    surf = pg.surfarray.make_surface(set.frame * 255)
    surf = pg.transform.scale(surf, (WIDTH, HEIGHT))


    set.screen.blit(surf, (0, 0))

    #! Ray-casting 


          

    pg.display.update()