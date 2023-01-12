import pygame

class Catcher(pygame.sprite.Sprite):
    '''
    This class creates the catcher behind home plate
    '''
    def __init__(self):
        '''
        This function loads the image of the catcher and sets the location of the screen
        '''
        pygame.init()
        self.image = pygame.image.load('assets/catcher.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 800)

    
    def render(self, display):
        '''
        This function renders the catcher on the screen 
        '''
        display.blit(self.image, self.rect)

