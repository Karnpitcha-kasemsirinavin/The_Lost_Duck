import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, level):
        super().__init__()
        self.image_list = []
        self.level = level
        self.frame = 0

        for index in range(10):
            image_name = 'Pic\\Enemy' + str(level) + '\\Enemy' + str(level) + '_' + str(index+1) + '.png'
            self.image_list.append(pygame.image.load(image_name).convert_alpha())

        self.image_order = 0
        self.image = self.image_list[self.image_order]
        # self.image = pygame.image.load('Pic\Enemy1\Enemy1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 1
        '''speed for each level'''
        # if self.level%4 >= 0.5:
        #     self.speed = 1*ceil(self.level/4)
        # elif self.level%4 < 0.5:
        #     self.speed = 1*floor(self.level/4)


        # print(f'level: {level}')
        # print(self.speed)

        self.lasers = pygame.sprite.Group()
        '''Make it collide perfectly'''
        self.mask = pygame.mask.from_surface(self.image)

        '''special enemy'''
        special_number = randint(0, 10)
        if special_number == 4:
            self.special = 'heart'
        elif special_number == 1:
            self.special = 'item'
        else:
            self.special = 'none'

        self.check_game_over = True

    def move(self):
        '''Movement speed of Enemy1'''
        if self.rect.x > 0:
            self.rect.x -= self.speed
        elif self.rect.x == 0:
            '''Constraint for enemies pos'''
            self.check_game_over = False
            # pygame.quit()
            # sys.exit()

    def pic(self):

        self.frame += 1
        if self.frame == 12:
            self.frame = 0
            self.image_order += 1

            if self.image_order >= len(self.image_list):
                self.image_order = 0

        self.image = self.image_list[self.image_order]

    def update(self):
        self.move()
        self.pic()
        if self.check_game_over is False:
            return False




