import random
import time
import pygame as pg

pg.init()
length = 700
height = 600
white = (255, 255, 255)
noms = ["Mob qui rajoute du CO2", "Mob qui jette les déchets", "Mob passif"]
couleurs_mobs = [(255,255,50), (255,120,0), (255,0,0)]
co2 = 0
window = pg.display.set_mode((length, height))
window.fill(white)
pg.display.set_caption('Test Mob')
running = True
class Mobs:
    def __init__(self):
        self.x = x = 0
        self.y = y = 0
        self.nom = noms
        self.couleur = couleurs_mobs
        self.image = image
        self.vitesse = vitesse
        self.etat = etat

    def spawn(self):
        mob = pg.Rect(self.x, self.y, 20, 20)
        print("I spawned !")
    def print_infos(self):
        print(f"nom = {self.nom}, couleur = {self.couleur}, vitesse = {self.vitesse}, etat = {self.etat}")
    @staticmethod
    def despawn():
        mob = pg.Rect(self.x, self.y, 20, 20)
        # mob.kill()
        print("I died !")

    def jette_un_dechet(self):
        # create a "dechet" object to throw at position of the mob
        mob = pg.Rect(self.x, self.y, 20, 20)
        dechet = pg.draw.rect(window, self.x, self.y, 15, 15)
        print("Je jette un déchet")
    @staticmethod
    def rajoute_du_co2():
        # add CO2 to the CO2 progression
        co2 += random.randint(0.01, 0.05)
        print("Je rajoutes du CO2")
    @staticmethod
    def passif():
        print("Je suis passif")

    def mouvement_mob(self):
        mob = pg.Rect(self.x, self.y, 20, 20)
        # while mob is alive :
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

while running:

    mob_CO2 = Mobs()
    mob_Dechet = Mobs()
    mob_Passif = Mobs()

    mob_CO2.spawn()
    mob_CO2.rajoute_du_co2()
    mob_CO2.mouvement_mob()
    mob_CO2.print_infos()
    mob_CO2.despawn()

    mob_Dechet.spawn()
    mob_Dechet.jette_un_dechet()
    mob_Dechet.mouvement_mob()
    mob_Dechet.print_infos()
    mob_Dechet.despawn()

    mob_Passif.spawn()
    mob_Passif.passif()
    mob_Passif.mouvement_mob()
    mob_Passif.print_infos()
    mob_Passif.despawn()

    window.blit()
    running = False