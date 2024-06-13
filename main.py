import pygame
import sys
from settings import *
from level import Level
from player import Player


class Button:
    def __init__(self, x, y, width, height, text):
        self.image = pygame.Surface((width, height))
        self.image.fill((198, 178, 128))  # Button color
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(text, True, (255, 255, 255))  # Text color
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)
        screen.blit(self.text_surf, self.text_rect)

        return action


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), pygame.RESIZABLE)
        pygame.display.set_caption('MAEVE WORLD')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.main_menu = True
        self.credit_menu = False
        self.play = False
        self.is_running = True

        self.credit_button = Button(WIDTH // 2 - 70, HEIGTH // 2 + 110, 200, 50, 'Credits')
        self.start_button = Button(WIDTH // 2 - 300, HEIGTH // 2 + 110, 200, 50, 'Start')
        self.exit_button = Button(WIDTH // 2 + 150, HEIGTH // 2 + 110, 200, 50, 'Exit')

        # Adding exit button for the credit menu
        self.credit_exit_button = Button(WIDTH // 2 - 70, HEIGTH // 2 + 180, 200, 50, 'Exit')

    def run(self):
        while self.is_running:
            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))  # Fill with black background

            if self.main_menu:
                self.level.run()  # Run the game level in the background

                key = pygame.key.get_pressed()
                if self.exit_button.draw(self.screen) or key[pygame.K_q]:
                    self.is_running = False
                if self.start_button.draw(self.screen) or key[pygame.K_s]:
                    self.main_menu = False
                    self.play = True
                if self.credit_button.draw(self.screen) or key[pygame.K_c]:
                    self.main_menu = False
                    self.credit_menu = True

            elif self.credit_menu:
                self.screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 36)

                # Multi-line credits
                credits_lines = [
                    "Credits:",
                    "Développeur :",
                    "Esteban, Emma, Abdel, Valentino, Maïwen"
                ]

                y_offset = HEIGTH // 2 - 50
                for line in credits_lines:
                    credit_text = font.render(line, True, (198, 178, 128))
                    text_rect = credit_text.get_rect(center=(WIDTH // 2, y_offset))
                    self.screen.blit(credit_text, text_rect)
                    y_offset += 40  # Adjust space between lines

                key = pygame.key.get_pressed()
                if self.credit_exit_button.draw(self.screen) or key[pygame.K_e]:
                    self.main_menu = True
                    self.credit_menu = False

            elif self.play:
                self.level.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
