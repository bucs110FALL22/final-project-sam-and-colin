import pygame
import sys
from src.catcher import Catcher
from src.bat import Bat
from src.outfielder import Outfielder
from src.ball import Ball
from src.scoreboard import Scoreboard


class Controller:
    def __init__(self):
        pygame.init()
        # initializes pygame displays screen creates varables for classes 
        self.display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Home Run Derby')
        self.bg = pygame.image.load("assets/field.png")
        self.bat = Bat()
        self.catcher = Catcher()
        self.scoreboard = Scoreboard()
        self.main_menu = True
        self.font = pygame.font.Font('freesansbold.ttf',25)
        self.gameOver = False
    
   
        #outfielder group
        self.outfielderGroup = pygame.sprite.Group()
        self.outfielderGroup.add(Outfielder(400,40))
        self.outfielderGroup.add(Outfielder(100,150))
        self.outfielderGroup.add(Outfielder(700,150))

        #ball group
        self.ballGroup = pygame.sprite.Group()
        self.ballGroup.add(Ball(400,400,self.catcher, self.outfielderGroup,self.ballGroup))

    
        
    def mainloop(self):
        self.gameOn = True
        while self.gameOn == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        # gets the Ball
                      self.ballGroup.sprites()[0].inmotion = True
                    #   sets animation
                    if event.key == pygame.K_SPACE:
                        if (self.ballGroup.sprites()[0].rect.colliderect(self.bat.rect)):
                            self.ballGroup.sprites()[0].inmotion = False
                        self.bat.animate()
                    else:
                      self.is_animating = False

                    #checks for collision in sprites that update scoreboard 

            if (self.ballGroup.sprites()[0].rect.colliderect(self.catcher.rect)):
                self.scoreboard.update()
            if (self.ballGroup.sprites()[0].rect.colliderect(self.outfielderGroup.sprites()[0])):
                self.scoreboard.update()
            if (self.ballGroup.sprites()[0].rect.colliderect(self.outfielderGroup.sprites()[1])):
                self.scoreboard.update()
            if (self.ballGroup.sprites()[0].rect.colliderect(self.outfielderGroup.sprites()[2])):
                self.scoreboard.update()
                
            self.display.blit(self.bg, (0, 0))
            self.bat.render(self.display)
            self.bat.update()
            self.catcher.render(self.display)
            for outfielder in self.outfielderGroup:
                outfielder.render(self.display)
                #if out or homerun is scored we update scoreboard
            board = []
            for ball in self.ballGroup:
                #ball.update(outfielder)
                result = ball.update(self.bat)
                if result:
                  board.append(result)
                ball.render(self.display)
            outs = 0
            homeruns = 0
            for i in board:
              outs+=i[0]
              homeruns+=i[1]
            self.scoreboard.scores(outs,homeruns)
            self.scoreboard.render()
                
            FPS = pygame.time.Clock()
            FPS.tick(120)
            
        

            pygame.display.update()


