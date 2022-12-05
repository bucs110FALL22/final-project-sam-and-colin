import pygame
import random
from src.outfielder import outfielderGroup
from src.catcher import catcher

class Ball(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        pygame.init()
        self.image = pygame.image.load('assets/baseball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
        self.direction = -1
        self.inmotion = None 
        self.dx = random.uniform(-3,3)
      
    def update(self, bat):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_p]:
            self.inmotion = True
        if self.inmotion:
                self.rect.y += random.randint(1,10)
        if self.rect.colliderect(bat.rect) and pressed_keys[pygame.K_SPACE]:
            self.inmotion = False
        if self.inmotion == False:
            self.direction *= 1
            self.rect.y -= 3
            self.rect.x += self.dx * self.direction
        if pygame.sprite.spritecollide(self,outfielderGroup,False, None):
            self.kill()
            pygame.sprite.Group.empty(ballGroup)
            ballGroup.add(Ball(400,400))
        if pygame.sprite.collide_rect(self,catcher):
            self.kill()
            pygame.sprite.Group.empty(ballGroup)
            ballGroup.add(Ball(400,400))

    def render(self, display):
        display.blit(self.image, self.rect)
    
ballGroup = pygame.sprite.Group()
ballGroup.add(Ball(400,400))