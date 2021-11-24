import pygame

class Ultimatepower(pygame.sprite.Sprite):
    def __init__(self,position ,screen_width,level):
        super().__init__()

        self.image_list = []
        self.frame = 0
        self.image_order = 0

        for index in range(7):
            ultimate_file = 'Pic\\Player\\Ultimate\\ultimate' + str(index+1) + '.png'
            self.image_list.append(pygame.image.load(ultimate_file).convert_alpha())

        self.image = self.image_list[self.image_order]
        self.rect = self.image.get_rect(midleft = position)
        self.speed = 14 + level
        self.width_x_constraint = screen_width
        self.level = level

    def destroy(self):
        if self.rect.x <= 0 or self.rect.x >= self.width_x_constraint+810:
            self.kill()

    def pic(self):

        self.frame += 1
        if self.frame == 12:
            self.frame = 0
            self.image_order += 1

            if self.image_order >= len(self.image_list):
                self.image_order = 0

        self.image = self.image_list[self.image_order]

    def update(self):
        self.pic()
        self.rect.x += self.speed
        self.destroy()