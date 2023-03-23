import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint

vec = pg.math.Vector2

# player class

class Player(Sprite):
    def __init__(self,game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        elif keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        elif keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        elif keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
    # method to keep sprite on screen 
    def jump(self):
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)

    def inbounds (self):
        if self.rect.x > WIDTH-25:
            self.pos.x = 775
            self.vel.x *= 0
        if self.rect.x < 25:
            self.pos.x = 25
            self.vel.x *= 0
        if self.rect.y > HEIGHT-25:
            self.pos.y = 575
            self.vel.y *= 0
        if self.rect.y < 25:
            self.pos.y = 25
            self.vel.y *= 0


    def update(self):
        self.inbounds()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

class Mob(Sprite):
    def __init__(self,width,height,color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # method to keep sprite on screen 
    def inbounds (self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            self.pos.x = 800
        if self.rect.x < 0:
            self.vel.x *= -1
            self.pos.x = 0
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            self.pos.y = 600
        if self.rect.y < 0:
            self.vel.y *= -1
            self.pos.y = 0

    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos