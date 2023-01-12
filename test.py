import pygame
import sys
import random
import pygame.math as math


pygame.init()
display = pygame.display.set_mode((800, 800))

FPS = pygame.time.Clock()

title = "PRESS SPACE TO HIT PRESS P TO PITCH!"
pygame.display.set_caption(title)

def Scoreboard():
  
  redscore = 0
  bluescore = 0 
  innings = 0 
  out = 0
  
  white = (255,255,255)
  blue = (0,0,255)
  red = (255,0,0)
  black = (0,0,0)
  font = pygame.font.Font('freesansbold.ttf',25)


  pygame.draw.rect(display, black, pygame.Rect((0,0),(800,50)))
  
  blueteam = font.render("Blue Team:"+str(bluescore), True, blue)
  display.blit(blueteam, (0, 15))
  redteam = font.render("Red Team:"+str(redscore), True, red)
  display.blit(redteam, (200, 15))
  outs = font.render("Outs:"+str(out), True, white)
  display.blit(outs, (600, 15))
  inning = font.render("Inning:"+str(innings), True, "white")
  display.blit(inning, (700, 15))
  pygame.display.update()

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


class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('assets/flatbat.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/bat.png').convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.midbottom = [400,650]

    def animate(self):
        self.is_animating = True

    def update(self): 
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

    def render(self, display):
            display.blit(self.image, self.rect)

bat = Bat()

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
class Outfielder(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('assets/stick.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)

    

    def render(self, display):
            display.blit(self.image, self.rect)

outfielderGroup = pygame.sprite.Group()
outfielderGroup.add(Outfielder(400,50))
outfielderGroup.add(Outfielder(100,100))
outfielderGroup.add(Outfielder(700,100))

class Base(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load('assets/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)         
    

    def render(self, display):
            display.blit(self.image, self.rect)

baseGroup = pygame.sprite.Group()
baseGroup.add(Base(600,400))
baseGroup.add(Base(175,400))
baseGroup.add(Base(400,250))

class Plate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/homeplate.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 650)
    def render(self, display):
            display.blit(self.image, self.rect)

    
plate = Plate()   


class Controller:
    pygame.init()

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_SPACE:
                    bat.animate()
                else:
                    self.is_animating = False
            
            display.fill((79, 128, 77))
            
            
            plate.render(display)
            plate.update()
            bat.render(display)
            bat.update()
            catcher.render(display)
            catcher.update()
            for outfielder in outfielderGroup:
                outfielder.render(display)
            for ball in ballGroup:
                ball.update(outfielder)
                ball.update(bat)
                ball.render(display)
            for base in baseGroup:
              base.update()
              base.render(display)
            Scoreboard()
            FPS.tick(60)
            
        

            pygame.display.update()

def main():
    controller = Controller()
    controller.mainloop()

main()