import os
class Profil:
    def __init__(self, pseudo, progression, ressources):
        self.pseudo = pseudo
        self.progression = progression
        self.ressources = ressources
    def ask_pseudo(self):
        self.pseudo = input("Enter a pseudo : ")
    def save_profil(self):
        with open('save_profile.txt', "w", encoding='utf-8') as profil_joueur :
            profil_joueur.write(f"ID : {self.pseudo}\nProgression : {self.progression}\nRessources : {self.ressources}\n")
            profil_joueur.close()
    def get_profil(self):
        with open('save_profile.txt',"r", encoding='utf-8') as read_profil_joueur:
            contenu = read_profil_joueur.read().split()
            for _ in contenu :
                pseudo = contenu[2:3]
                progression = contenu[5:6]
                ressources = contenu[8:9]
            var_pseudo = str(pseudo[0])
            var_progression = float(progression[0])
            var_ressources = str(ressources[0])
            read_profil_joueur.close()
        print(f"Pseudo : {var_pseudo}\nProgression : {var_progression}\nRessouces : {var_ressources}\n")
        return var_pseudo, var_progression, var_ressources

profil1 = Profil("", 0.25, 204)
profil1.ask_pseudo()
profil1.save_profil()
profil1.get_profil()