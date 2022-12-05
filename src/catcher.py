import pygame

class Catcher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        self.image = pygame.image.load('assets/catcher.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 800)

    
    def render(self, display):
            display.blit(self.image, self.rect)

catcher = Catcher()