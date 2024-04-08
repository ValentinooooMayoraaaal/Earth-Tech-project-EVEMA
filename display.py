import pygame as pg
import sys
#from button import Button

pg.init()

running = True
hauteur = 600
largeur = 800
couleur_texte = (0,0,0)
police = pg.font.Font(None, 36)

fenetre = pg.display.set_mode((largeur, hauteur))
pg.display.set_caption("Maeve World")

image_background = pg.image.load("assets/img.png")
image_background = pg.transform.scale(image_background, (largeur, hauteur))
def ecran_accueil():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                return
        fenetre.blit(image_background, (0,0))
        texte1 = police.render("Appuyez sur une touche pour démarrer", True, couleur_texte)
        texte_rect1 = texte1.get_rect(center=(largeur//2, hauteur//2))
        fenetre.blit(texte1, texte_rect1)
        texte2 = police.render("Appuyez sur une touche pour quitter", True, couleur_texte)
        texte_rect2 = texte2.get_rect(center=(largeur // 2, hauteur // 2.2))
        fenetre.blit(texte2, texte_rect2)
        pg.display.flip()

ecran_accueil()