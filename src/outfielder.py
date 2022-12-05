import pygame

class Outfielder(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.init()
        self.image = pygame.image.load('assets/stick.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    def render(self, display):
            display.blit(self.image, self.rect)

outfielderGroup = pygame.sprite.Group()
outfielderGroup.add(Outfielder(400,50))
outfielderGroup.add(Outfielder(100,100))
outfielderGroup.add(Outfielder(700,100))
