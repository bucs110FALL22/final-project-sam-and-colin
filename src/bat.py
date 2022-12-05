import pygame

pygame.init()

class Bat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('assets/b1.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/b2.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/b3.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/b4.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/b5.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/b6.png').convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.midbottom = [360,730]

         


    def animate(self):
      if pygame.KEYDOWN:
        if pygame.K_p:
            self.is_animating = True

    def update(self): 
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
    


    def render(self, display):
            display.blit(self.image, self.rect)

#bat = Bat()