import random
import time
import pygame as pg
import sys

# initialise pygame
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

# image du dechet spawn par le mob
img_dechet = pg.image.load("assets/dechets.png")
img_dechet = pg.transform.scale(img_dechet, (30,30))

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
        self.vitesse = 10
        self.etat = None

    # fonction qui crée le mob
    def spawn(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        print("I spawned !")

    # fonction qui affiche sur le terminal les informations du mob
    def print_infos(self):
        print(f"nom = {self.nom}, couleur = {self.couleur}, vitesse = {self.vitesse}, etat = {self.etat}")

    # fonction qui enlève le mob de l'écran et du sprite groupe
    def despawn(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        self.all_mobs.remove()
        # mob.kill()
        print("I died !")

    # mob qui ajoute un déchet sur le terrain à une position donnée
    def jette_un_dechet(self,x, y):
        # create a "dechet" object to throw at position of the mob
        etat = "jette un déchet"
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        window.blit(img_dechet, (x, y))
        print(f"Je jette un déchet à {x} : {y}")

    # mob qui ajoute du CO2
    def rajoute_du_co2(self,etat, co2):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        # add CO2 to the CO2 progression
        co2 += random.randint(0.001, 0.025)
        print("Je rajoutes du CO2")

    # mob passif
    def passif(self, etat):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        print("Je suis passif")

    # fonction qui détermine les mouvements aléatoires du mobs sur le terrain, collisions non comprises
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

    # fonction qui applique le filtre de couleur sur les mobs pour les différencier visuellement
    def filtre_mob(self):
        filtre = pg.Surface((80, 80))
        filtre.set_alpha(128)
        filtre.fill((255, 0, 0))
        self.image.blit(filtre, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    def get_x(self):
        pos_x = self.rect.x
        t = 0
        while True :
            t+=1
            if t == 10:
                x = pos_x
                break
        return x
    def get_y(self):
        pos_y = self.rect.y
        t = 0
        while True :
            t+=1
            if t == 10:
                y = pos_y
                break
        return y



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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                mob.jette_un_dechet(mob.get_x(), mob.get_y())
                print("success")
    mob.mouvement_mob()
    pg.display.flip()
    clock.tick(60)