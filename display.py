import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)

# Taille initiale de la fenêtre
largeur = 800
hauteur = 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
pygame.display.set_caption('Display')

# Boucle de jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            largeur = event.w
            hauteur = event.h
            fenetre = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Basculement entre le mode fenêtré et le mode plein écran avec la touche "f"
                if fenetre.get_flags() & pygame.FULLSCREEN:
                    fenetre = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
                else:
                    fenetre = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)

    # Créer un tampon de trame hors écran
    tampon = pygame.Surface((largeur, hauteur))
    tampon.fill(BLANC)

    # Copier le tampon sur la fenêtre principale
    fenetre.blit(tampon, (0, 0))
    # Rafraîchir l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()
