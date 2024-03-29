import random
import time
import pygame as pg
import sys

pg.init()

# Temps du jeu
clock = pg.time.Clock()

# variable locale à récupérer avec la data du joueur
co2 = 0

# taille de la fenêtre de jeu
length = 1080
height = 720

# Couleurs en tant que variables
white = (255, 255, 255)
sand = (235, 170, 80)
couleurs_mobs = [(255,255,50), (255,120,0), (255,0,0)]

# noms des mobs à print uniquement dans le terminal
noms = ["Mob qui rajoute du CO2", "Mob qui jette les déchets", "Mob passif"]

# image du mob ainsi que l'application du filtre de couleur pour différencier les mobs
image = pg.image.load("assets/alien.png")
image = pg.transform.scale(image, (80,80))

# Paramètres de la fenêtre de jeu
window = pg.display.set_mode((length, height))
pg.display.set_caption('Test Mob')


# Classe Mobs
class Mobs(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nom = noms
        self.couleur = couleurs_mobs
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 600
        self.vitesse = 5
        self.etat = None


    def spawn(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        print("I spawned !")
    def print_infos(self):
        print(f"nom = {self.nom}, couleur = {self.couleur}, vitesse = {self.vitesse}, etat = {self.etat}")

    def despawn(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        self.all_mobs.remove()
        # mob.kill()
        print("I died !")

    def jette_un_dechet(self, etat):
        # create a "dechet" object to throw at position of the mob
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        dechet = pg.draw.rect(window, self.rect.x, self.rect.y, 15, 15)
        print("Je jette un déchet")

    def rajoute_du_co2(self,etat, co2):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        # add CO2 to the CO2 progression
        co2 += random.randint(0.01, 0.05)
        print("Je rajoutes du CO2")

    def passif(self, etat):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        print("Je suis passif")

    def mouvement_mob(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        # Choix aléatoire d'une action toutes les 1000 millisecondes (1 seconde)
        if pg.time.get_ticks() % 20 == 0:
            action = random.choice(['0', '1', '2', '3'])
            if action == '0':
                self.rect.x += self.vitesse
            elif action == '1':
                self.rect.x -= self.vitesse
            elif action == '2':
                self.rect.y += self.vitesse
            elif action == '3':
                self.rect.y -= self.vitesse

    def filtre_mob(self):
        filtre = pg.Surface((80, 80))
        filtre.set_alpha(128)
        filtre.fill((255, 0, 0))
        self.image.blit(filtre, (0, 0), special_flags=pg.BLEND_RGBA_MULT)


# création des objets
mob = Mobs()
mob.filtre_mob()
# Boucle du jeu
running = True

while running:
    # à executer hors conditions

    window.fill(sand)
    window.blit(mob.image,mob.rect)
    #window.blit(mob_Dechet.image, (50, 0))
    #window.blit(mob_Passif.image, (0, 0))

    pg.display.flip()

    for event in pg.event.get():

        # Condition de sortie de jeu
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

    mob.mouvement_mob()
    pg.display.flip()
    clock.tick(60)