import pygame

class Plate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.image = pygame.image.load('assets/homeplate.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = [400,750]
    def render(self, display):
            display.blit(self.image, self.rect)

    
plate = Plate()   