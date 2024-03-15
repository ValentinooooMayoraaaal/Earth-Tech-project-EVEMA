import os
class Profil:
    def __init__(self):
        self.pseudo = pseudo = ""
        self.progression = progression = 0.00
        self.ressource_monnaie = ressource_monnaie = 0
        self.ressource_dechet = ressource_dechet = 0
        self.ressource_carbone = ressource_carbone = 10
    def ask_pseudo(self):
        while self.pseudo == "":
            self.pseudo = input("Enter a pseudo : ")
    def save_profil(self):
        with open('save_profile.txt', "a", encoding='utf-8') as profil_joueur :
            profil_joueur.write(f"{self.pseudo} {self.progression} {self.ressource_monnaie} {self.ressource_dechet} {self.ressource_carbone}\n")

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
                        self.ressource_monnaie = contenu[x+2]
                        self.ressource_dechet = contenu[x+3]
                        self.ressource_carbone = contenu[x+4]
                    else:
                        x += 5
            else:
                print("Pseudo doesnt exist. Creating New Profile")
                profil1.save_profil()
                profil1.get_profil()
        return self.pseudo, self.progression, self.ressource_monnaie, self.ressource_dechet, self.ressource_carbone

profil1 = Profil()
pseudo, progression, ressource_monnaie, ressource_dechet, ressource_carbone = profil1.get_profil()
print(f"Pseudo : {pseudo}\nProgression : {progression}\nRessource Monnaie : {ressource_monnaie}\nRessource Déchet : {ressource_dechet}\nRessource Carbone : {ressource_carbone}\n")