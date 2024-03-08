import os
class Profil:
    def __init__(self, pseudo="", progression=0.0, ressources=0):
        self.pseudo = pseudo
        self.progression = progression
        self.ressources = ressources
    def ask_pseudo(self):
        while self.pseudo == "":
            self.pseudo = input("Enter a pseudo : ")
    def save_profil(self):
        with open('save_profile.txt', "a", encoding='utf-8') as profil_joueur :
            profil_joueur.write(f"{self.pseudo} {self.progression} {self.ressources}\n")

    def get_profil(self):
        x=0
        test = False
        profil1.ask_pseudo()
        with open('save_profile.txt',"r", encoding='utf-8') as read_profil_joueur:
            contenu = read_profil_joueur.read().split()
            if self.pseudo in contenu :
                print('Pseudo exits. Gathering Profile info...')
                while test is False:
                    if self.pseudo in contenu[x]:
                        test = True
                        self.pseudo = contenu[x]
                        self.progression = contenu[x+1]
                        self.ressources = contenu[x+2]
                    else:
                        x += 3
            else:
                print("Pseudo doesnt exist. Creating New Profile")
                profil1.save_profil()
                profil1.get_profil()
        return self.pseudo, self.progression, self.ressources


profil1 = Profil()
pseudo, progression, ressources = profil1.get_profil()
print(f"Pseudo : {pseudo}\nProgression : {progression}\nRessouces : {ressources}\n")