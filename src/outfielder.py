import pygame

class Outfielder(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('assets/glove.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    

    def render(self, display):
            display.blit(self.image, self.rect)

