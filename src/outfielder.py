import pygame

class Outfielder(pygame.sprite.Sprite):
    '''
    This class creates the outfielders who are in a sprite group created in controller.py
    '''
    def __init__(self,x,y):
        '''
        This function loads the image of the outfielder and creates x and y variable which is defined in 
        controller.py
        '''
        super().__init__()
        self.image = pygame.image.load('assets/glove.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    

    def render(self, display):
        '''
        This function renders the outfielders on the screen
        '''
        display.blit(self.image, self.rect)

