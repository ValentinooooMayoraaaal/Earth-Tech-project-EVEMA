import random
import time
class Mobs:
    def __init__(self, nom, couleur, taille, vitesse):
        self.nom = nom
        self.couleur = couleur
        self.taille = taille
        self.vitesse = vitesse
        #self.niveau = (self.vitesse + self.taille) / 2

    #def level(self):
    #    self.niveau = (self.vitesse + self.taille) / 2

    def mouvement(self):
        self.vitesse += vitesse
    def spawn(self):
        print("I spawned !")
    def print_infos(self):
        print(f"nom = {self.nom}, couleur = {self.couleur}, taille = {self.taille}, vitesse = {self.vitesse}")

    def despawn(self):
        print("I died !")

running = True

noms = ["mob1", "mob2", "mob3"]

while running:
    for _ in range(1,10):
        mob=Mobs(noms[random.randint(0,2)],(random.randint(1,255), random.randint(1,255), random.randint(1,255)), random.randint(1,20), random.randint(1,5))
        mob.spawn()
        mob.print_infos()
        mob.despawn()
        time.sleep(1)
    running = False