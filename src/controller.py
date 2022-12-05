import pygame
import sys
from src.catcher import catcher
from src.bat import bat
from src.plate import plate
from src.outfielder import outfielderGroup
from src.base import baseGroup
from src.ball import ballGroup

class Controller:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 800))
        self.image = pygame.image.load('assets/green.png').convert_alpha()
        # self.display.fill((79, 128, 77))
        
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
            
            plate.render(self.display)
            plate.update()
            bat.render(self.display)
            bat.update()
            catcher.render(self.display)
            for outfielder in outfielderGroup:
                outfielder.render(self.display)
            for ball in ballGroup:
                ball.update(outfielder)
                ball.update(bat)
                ball.render(self.display)
            for base in baseGroup:
              base.update()
              base.render(self.display)
            FPS = pygame.time.Clock()
            FPS.tick(60)
            
        

            pygame.display.update()

