import pygame
import random
import time


class Ball(pygame.sprite.Sprite):
    '''
    This class does a lot, it creates the ball and its image and sets the scale. It also creates x and y varibales
    which are later defined in a sprite group in the controller. This class also controlls the movement of the ball
    which I know is supposed to go into the controller but there were to many moving parts. This class also creates
    font renders that display on screen when and out or homerun occurs. 
    '''
    def __init__(self,x, y,catcher,outfielderGroup,ballGroup):
        '''
        This function creats the ball and all other variables associted with the ball and its movements
        '''
        super().__init__()
        pygame.init()
        self.image = pygame.image.load('assets/baseball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
        self.direction = -1
        self.inmotion = None 
        self.dx = random.uniform(-3.5,3.5)
        self.catcher = catcher
        self.outfielderGroup = outfielderGroup
        self.ballGroup = ballGroup
        self.display = pygame.display.set_mode((800, 800))
        self.font = pygame.font.Font('freesansbold.ttf',50)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.out = self.font.render("OUT", True, self.black)
        self.homerun = self.font.render("Homerun!!!", True, self.black)

    def reset(self):
        '''
        This function resets the ball to a starting position whenever it is called
        '''
        self.rect.x = 400
        self.rect.y = 400
        self.direction = -1
        self.inmotion = None 
        self.dx = random.uniform(-3.5,3.5)
        
    

    def update(self, bat):
        '''
      This function updates the movement of the ball and checks for all types of collison between the walls and the
      outfielders as well as the catcher. 
      '''
        if self.inmotion:
            self.rect.y += random.randint(1,10)
        if self.inmotion == False:
            self.direction *= 1
            self.rect.y -= random.randint(5,10)
            self.rect.x += self.dx * self.direction
        if pygame.sprite.spritecollide(self,self.outfielderGroup,False, None):
            self.reset()
            self.display.blit(self.out, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (1,0)
        if pygame.sprite.collide_rect(self,self.catcher):
            self.reset()
            self.display.blit(self.out, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (1,0)            
        if self.rect.left < 0:
            self.reset()
            self.display.blit(self.homerun, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)
        if self.rect.right > 800:
            self.reset()
            self.display.blit(self.homerun,center=(400, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)
        if self.rect.top <= 0:
            self.reset()
            self.display.blit(self.homerun, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)
           
       
    def render(self, display):
        '''
        This function displays the ball on the screen when called in controller.
        '''
        display.blit(self.image, self.rect)
    
