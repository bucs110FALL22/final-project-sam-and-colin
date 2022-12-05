import pygame
import json

class Scoreboard:
        def __init__(self):
            self.display = pygame.display.set_mode((800, 800))
            self.out = 0
            self.bluescore = 0
            self.highscore = 0
            self.font = pygame.font.Font('freesansbold.ttf',25)
        

        def update(self):
                self.out = self.out + 1  
                print(self.out)

        def blue_score(self):
            self.bluescore = self.bluescore + 1

        def scores(self,outs,homeruns):
          self.out += outs
          self.bluescore += homeruns

        def render(self):
            blueteam = self.font.render("Blue Team:"+str(self.bluescore), True, "blue")
            self.display.blit(blueteam, (0, 15))
            outs = self.font.render("Outs:"+str(self.out), True, "white")
            self.display.blit(outs, (600, 15))
             
     
         





            

        
        
