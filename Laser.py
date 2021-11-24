'''Laser is one of the sprites'''
import pygame
from math import floor,ceil

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, screen_width,level):
        super().__init__()
        self.frame = 0

        '''image'''
        self.image_list = []

        for index in range(5):
            image_name = 'Pic\Player\PlayerLaser\Playerlaser'+ str(index + 1) + '.png'
            self.image_list.append(pygame.image.load(image_name).convert_alpha())


        self.image_order = 0
        self.image = self.image_list[self.image_order]
        self.rect = self.image.get_rect(midleft=position)

        '''speed for each level'''
        if level%2 == 0:
            self.speed = 11+round(level/2)
        elif level%2 == 1:
            self.speed = 11+ceil(level/2)
        # print(f'level: {level}')
        # print(self.speed)

        self.width_x_constraint = screen_width

    def pic(self):

        self.frame += 1
        if self.frame == 10:
            self.frame = 0
            self.image_order += 1

            if self.image_order >= len(self.image_list):
                self.image_order = len(self.image_list) - 1

        self.image = self.image_list[self.image_order]

    def destroy(self):
        if self.rect.x <= 0 or self.rect.x >= self.width_x_constraint+810:
            self.kill()

    def update(self):
        '''Go to right'''
        self.rect.x += self.speed
        '''Destroy the laser that spawn at the left'''
        self.destroy()
        self.pic()

class Enemy_laser(Laser):
    def __init__(self, position, screen_width,level):
        super().__init__(position,screen_width,level)
        self.level = level
        self.image_list = []

        for index in range(10):
            image_name = 'Pic\EnemyLaser' + str(level) + '\EnemyLaser' + str(level) + '_' + str(index+1) + '.png'
            self.image_list.append(pygame.image.load(image_name).convert_alpha())

        self.image_order = 0
        self.image = self.image_list[self.image_order]

        # self.image = pygame.image.load('Pic\EnemyLaser1\EnemyLaser1_1.png')

        '''speed for each level'''
        if level%2 == 0:
            self.speed = 9+round(level/2)
        elif level%2 == 1:
            self.speed = 9+ceil(level/2)
        # print(f'level: {level}')
        # print(self.speed)

        '''Change pic of enemy laser'''
        laser_name = 'Pic\EnemyLaser' + str(level) +'.png'
        self.rect = self.image.get_rect(midleft = position)

    def pic(self):

        self.frame += 1
        if self.frame == 10:
            self.frame = 0
            self.image_order += 1

            if self.image_order >= len(self.image_list):
                self.image_order = 0

        self.image = self.image_list[self.image_order]

    def update(self):
        '''Go to left'''
        self.rect.x -= self.speed
        '''Destroy the laser that spawn at the left'''
        self.destroy()
        self.pic()
