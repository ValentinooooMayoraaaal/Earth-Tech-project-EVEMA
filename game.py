import pygame as pg
from mob import Mobs

# Classe Jeu
class Game:
    def __init__(self):
        self.mob = Mobs()
        self.all_mobs = pg.sprite.Group()

    def check_collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)

# création des objets
game = Game()