import pygame
import random
import time
#from src.controller import Controller
#from src.outfielder import outfielderGroup
#from src.catcher import catcher

class Ball(pygame.sprite.Sprite):
    def __init__(self,x, y,catcher,outfielderGroup,ballGroup):
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
        self.highscore = self.font.render("High Score: ", True, self.black)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 400
        self.direction = -1
        self.inmotion = None 
        self.dx = random.uniform(-3.5,3.5)
        
    

    def update(self, bat):
      
        if self.inmotion:
                self.rect.y += random.randint(1,10)
        if self.inmotion == False:
            self.direction *= 1
            self.rect.y -= random.randint(5,10)
            self.rect.x += self.dx * self.direction
          #checks collision between outfielders and ball resets the ball and signals homerun
        if pygame.sprite.spritecollide(self,self.outfielderGroup,False, None):
            self.reset()
            self.display.blit(self.out, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (1,0)
            
           #checks collision between outfielders and ball resets the ball and signals homerun
        if pygame.sprite.collide_rect(self,self.catcher):
            self.reset()
           
            self.display.blit(self.out, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (1,0)
            
 #checks collision between catcher and ball resets the ball and signals out
        if self.rect.left < 0:
            self.reset()
            self.display.blit(self.homerun, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)

            #checks if and ball resets the ball and signals homerun
        if self.rect.right > 800:
            self.reset()
            self.display.blit(self.homerun,center=(400, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)
          #checks if and ball is outside border and signals homerun
        if self.rect.top <= 0:
            self.reset()
            self.display.blit(self.homerun, (400/2, 400/2))
            pygame.display.flip()
            pygame.time.delay(1000)
            return (0,1)
           
       
            
          
    def render(self, display):
        display.blit(self.image, self.rect)
    
