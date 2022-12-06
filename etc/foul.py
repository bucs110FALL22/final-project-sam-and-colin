import pygame

class Foul(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('assets/foulline.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, 800))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (400,800)

    def render(self, display):
        display.blit(self.image, self.rect)
