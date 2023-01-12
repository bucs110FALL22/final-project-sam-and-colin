import pygame

class Scoreboard:
    '''
    This class creates the scoreboard and allows for updating values to be assinged and updated on screen
    '''
    def __init__(self):
        '''
        This function creates a display for the scoreboard to be shown on and sets default values for each of 
        the possible values that can be updated
        '''
        self.display = pygame.display.set_mode((800, 800))
        self.out = 0
        self.bluescore = 0
        self.font = pygame.font.Font('freesansbold.ttf',25)
    

    def update(self):
        '''
        This function updates the number of outs displayed on the screen when the function is called
        '''
        self.out = self.out + 1  

    def blue_score(self):
        '''
        This function updates the blue score when the function is called
        '''
        self.bluescore = self.bluescore + 1

    def scores(self,outs,homeruns):
        '''
        This is what adds to the count in order for the program to keep track
        '''
        self.out += outs
        self.bluescore += homeruns

    def render(self):
        '''
        This function renders each element of the scoreboard that needs to be displayed on the screen
        '''
        blueteam = self.font.render("Blue Team:"+str(self.bluescore), True, "blue")
        self.display.blit(blueteam, (0, 15))
        outs = self.font.render("Outs:"+str(self.out), True, "white")
        self.display.blit(outs, (600, 15))
            
    
        





            

        
        
