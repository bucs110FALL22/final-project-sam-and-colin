import pygame

pygame.init()

class Bat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('assets/flatbat.png').convert_alpha())
        self.sprites.append(pygame.image.load('assets/bat.png').convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.midbottom = [400,750]

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