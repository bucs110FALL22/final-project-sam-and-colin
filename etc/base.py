import pygame

class Base(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load('assets/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)         
    

    def render(self, display):
            display.blit(self.image, self.rect)

# baseGroup = pygame.sprite.Group()
# baseGroup.add(Base(400,400))
# baseGroup.add(Base(75,400))
# baseGroup.add(Base(250,100))