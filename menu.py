import pygame

surfaceW = 800  # Dimension de la fenêtre / Largeur
surfaceH = 600  # Dimension de la fenêtre / Longueur


class Menu:
    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        self.couleurs = dict(
            normal=(0, 200, 0),
            survol=(0, 200, 200),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('JOUER', application.jeu),
            ('CREDIT', self.credit),
            ('QUITTER', application.quitter)

        )
        x = 400
        y = 200
        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes:
                groupe.add(mb)

    def credit(self, application, *groupes):
        credit = Credit(application, groupes)
        application.ecran = credit

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur):
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche:
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else:
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else:
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur


class MenuBouton(pygame.sprite.Sprite):
    """ Création d'un simple bouton rectangulaire """

    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande):
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur / 2, hauteur / 2)

        self.dessiner(couleur)

    def dessiner(self, couleur):
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self):
        # Appel de la commande du bouton
        self._commande()


class Jeu:
    """ Simulacre de l'interface du jeu """

    def __init__(self, jeu, *groupes):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self._couleurTexte = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.creerTexte()
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (surfaceW / 2, surfaceH / 2)
        # Création d'un event
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

        # bouton retour
        self.bouton_retour = MenuBouton("Retour au menu",
        (0, 200, 0), # couleur normale
        self._font,
        surfaceW - 140,
        30, # position y
        240, # largeur
        50, # Hauteur
        jeu.menu # fonction retour au menu
        )
        groupes[0].add(self.bouton_retour)

    def creerTexte(self):
        self.texte = self._font.render(
            'LE JEU EST EN COURS D\'EXÉCUTION',
            True,
            next(self._couleurTexte)
        )

    def update(self, events):
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.creerTexte()
                break

    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer


class Credit:
    """ Display the game credits """

    def __init__(self, application, *groupes):
        self.application = application
        self.font = pygame.font.SysFont('Helvetica', 24, bold=True)
        self.color = (0, 200, 0)
        self.text = self.font.render("GAME CREDITS", True, self.color)
        self.rect = self.text.get_rect()
        self.rect.center = (surfaceW // 2, surfaceH // 2)

        # Add the credit object to the group
        for groupe in groupes:
            groupe.add(self)

    def update(self, events):
        # Handle any event
        for event in events:
            if event.type == pygame.QUIT:
                self.application.quitter()

        # Draw the credit text
        self.application.fenetre.blit(self.text, self.rect)

    def executerCommande(self):
        pass

    def detruire(self):
        pass


# generer la fênetre de notre jeu
class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MAEVE WORLD")

        self.fond = (150,) * 3

        self.fenetre = pygame.display.set_mode((surfaceW, surfaceH))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def quitter(self):
        self.statut = False

    def update(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
                return

        self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

        # vérification du clic sur le bouton "retour menu"
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # vérifie si le clic gauche a été enfoncé
                # vérification du clic sur le bouton "Retour au menu"
                for bouton in self.groupeGlobal:
                    if isinstance(bouton, MenuBouton) and bouton.texte == "Retour au menu":
                        if bouton.rect.collidepoint(event.pos):
                                self.menu() # retour au menu principal


app = Application()
app.menu()

clock = pygame.time.Clock()

while app.statut:
    app.update()
    clock.tick(30)

pygame.quit()