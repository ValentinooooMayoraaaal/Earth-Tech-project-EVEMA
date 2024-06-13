import random
import time
import pygame as pg
import sys

# initialise pygame
pg.init()

# Temps du jeu
clock = pg.time.Clock()
FPS = 60

# variable locale à récupérer avec la data du joueur
co2 = 0.00

# taille de la fenêtre de jeu
length = 1080
height = 720

# Couleurs en tant que variables
white = (255, 255, 255)
sand = (235, 170, 80)
background_image = pg.image.load("assets/fondearthtech.jpg")
background_image = pg.transform.scale(background_image,(length,height))
couleurs_mobs = [(255,255,50), (255,120,0), (255,0,0)]

# noms des mobs à print uniquement dans le terminal
noms = ["Mob qui rajoute du CO2", "Mob qui jette les déchets", "Mob passif"]

# image du mob ainsi que l'application du filtre de couleur pour différencier les mobs
image = pg.image.load("assets/alien.png")
image = pg.transform.scale(image, (60,60))

# image du dechet spawn par le mob
img_dechet = pg.image.load("assets/trash_bag_earth_tech.png")
img_dechet = pg.transform.scale(img_dechet, (30,30))
dechet_rect = img_dechet.get_rect()

# font settings
font = pg.font.Font(None, 36)  # Police par défaut, taille 36

# Paramètres de la fenêtre de jeu
screen = pg.display.set_mode((length, height))
pg.display.set_caption('Test Mob')

# code classe déchet par chatgpt
# Classe pour gérer les déchets
class Dechet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = dechet_rect.copy()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(img_dechet, (self.x, self.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Liste pour stocker les objets déchet
dechets = []

# Fonction pour créer un déchet
def jette_un_dechet(x, y):
    dechets.append(Dechet(x, y))
# fin du code chatgpt

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
        self.etat = ["Passif", "Co2", "Dechet"]
        self.co2 = 0

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
    def jette_un_dechet1(self,x, y):
        # create a "dechet" object to throw at position of the mob
        etat = "jette un déchet"
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        screen.blit(img_dechet, (x, y))
        dechets.append(Dechets(x,y))
        print(f"Je jette un déchet à {x} : {y}")

    # mob qui ajoute du CO2
    def rajoute_du_co2(self, etat):
        # Choix aléatoire d'une action toutes les 20 millisecondes
        if pg.time.get_ticks() % 20 == 0:
        # add CO2 to the CO2 progression
            self.co2 += random.randint(1, 5)*10**-2
        #text_surface = font.render(f"co2 : {self.co2}", True, (255, 255, 255))
        #screen.blit(text_surface, text_rect)
        print("Je rajoutes du CO2")

    # mob passif
    def passif(self, etat):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        print("Je suis passif")

    # fonction qui détermine les mouvements aléatoires du mobs sur le terrain, collisions non comprises
    def mouvement_mob(self):
        mob = pg.Rect(self.rect.x, self.rect.y, 20, 20)
        # Choix aléatoire d'une action toutes les 20 millisecondes
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
    def filtre_mob(self,etat):
        if etat is None:
            # défini un état de mob random entre les 3 disponibles
            random_etat = self.etat[random.randint(0,2)]
        else:
            random_etat = None
            if (random_etat or etat) == "Passif":
                filtre = pg.Surface((80, 80))
                filtre.set_alpha(128)
                filtre.fill((0, 0, 0))
                self.image.blit(filtre, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

            elif (random_etat or etat) == "Co2":
                filtre = pg.Surface((80, 80))
                filtre.set_alpha(128)
                filtre.fill((125, 0, 0))
                self.image.blit(filtre, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

            elif (random_etat or etat) == "Dechet":
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
mob_dechet = Mobs()
mob_passif = Mobs()
mob_co2 = Mobs()

# Les couleurs sont à paufiner donc je vais l'ignorer pour l'instant, les mobs sont tous avec un filtre noir peut importe leur attribut 'etat"
#mob_dechet.filtre_mob("Dechet")
#mob_passif.filtre_mob("Passif")
#mob_co2.filtre_mob("Co2")

counter_text = font.render(f"Counter CO2: {round(co2,2)}", True, (0, 0, 0))
# Boucle du jeu
running = True

while running:
    # à executer hors conditions
    # Toutes les 1000 millisecondes (1 seconde) du co2 s'ajoute SI un mob passif est présent, il manque un "while mob passif is alive"
    if pg.time.get_ticks() % 1000 == 0:
        co2 += 10 ** -2 * random.randint(1, 5)

    # blit de l'écran avec l'image de backgroud, le mob et le co2
    screen.blit(background_image,(0,0))
    screen.blit(mob_dechet.image, mob_dechet.rect)
    screen.blit(mob_passif.image,mob_passif.rect)
    screen.blit(mob_co2.image,mob_co2.rect)
    counter_text = font.render(f"Counter CO2: {round(co2, 2)}", True, (0, 0, 0))
    screen.blit(counter_text, (10, 10))
    for dechet in dechets :
        dechet.draw(screen)

    # mouvement du mob
    mob_dechet.mouvement_mob()
    mob_passif.mouvement_mob()
    mob_co2.mouvement_mob()
    pg.display.flip()

    for event in pg.event.get():

        # Condition de sortie de jeu
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

        # Events en fontions des inputs clavier
        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_SPACE:
                # Si input clavier est espace alors spawn un déchet
                jette_un_dechet(mob.get_x(), mob.get_y())
                print("success")

        # code chatgpt
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                pos = event.pos
                # Vérifiez si un déchet a été cliqué
                for dechet in dechets[:]:  # Itérer sur une copie de la liste
                    if dechet.is_clicked(pos):
                        dechets.remove(dechet)
                        print("dechet removed")
                        # fin du code chatgpt

    pg.display.flip()
    clock.tick(FPS)