import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_height, item, level):
        super().__init__()
        if item == 'heart':
            self.image = pygame.image.load('Pic\\heart.png').convert_alpha()
        elif item == '2xscore':
            self.image = pygame.image.load('Pic\\Double_score.png').convert_alpha()

        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        self.height_y_constraint = screen_height
        self.level = level
        self.speed = 1

    def move(self):
        '''Movement of item'''
        if self.rect.y <= 800:
            self.rect.y += self.speed
        elif self.rect.y > 800:
            self.kill()

        self.rect.x -= 2

    def update(self):
        self.move()

