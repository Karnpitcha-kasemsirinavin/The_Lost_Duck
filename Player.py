import pygame
from Laser import Laser
from Ultimate import Ultimatepower

class Duck_Player(pygame.sprite.Sprite):
    def __init__(self, position, screen_constraint, level, game_bg_channel):
        super().__init__()
        '''-----Player-----'''
        self.image = pygame.image.load('Pic\Player\Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.level = level


        '''-----increase speed-----'''
        self.speed = 4 +level
        # print(f'level: {level}')
        # print(self.speed)

        '''----shooting image----'''
        self.shooting_image_list = []
        self.image_order = 0

        for index in range(16):
            image_name = 'Pic\Player\Player_shoot\Player_shoot' + str(index+1) + '.png'
            self.shooting_image_list.append(pygame.image.load(image_name).convert_alpha())

        self.max_constraint = screen_constraint
        self.shooting_ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        '''----Make it collides perfectly----'''
        self.mask = pygame.mask.from_surface(self.image)

        self.lasers = pygame.sprite.Group()


        '''-----Animating----'''
        self.shoot_animating = False

        '''Ultimate'''
        self.ultimatepower = pygame.sprite.Group()
        '''30 sec'''
        self.ultimate_run = False
        self.countdown_ultimate = 0
        self.start_ultimate_time = 0
        self.ultimate_period = 2000

        self.ultimate_pic_time = 10
        self.ultimate_pic_ready = False
        self.recharge_ultimate = 0

        self.press_q = False

        '''-----ultimate player image-----'''
        self.ultimate_player_pic_ready = False
        self.frame_ultimate = 0
        self.ultimate_player_list = []

        for index in range(7):
            image_name = 'Pic\Player\Player_ultimate\Player_ultimate' + str(index + 1) + '.png'
            self.ultimate_player_list.append(pygame.image.load(image_name).convert_alpha())

        '''Bg sound channel'''
        self.game_bg_channel = game_bg_channel
        self.ultimate_channel = pygame.mixer.Channel(2)

        '''-----Sound effect-----'''
        '''Ultimate period sound'''
        self.sound_ultimate = pygame.mixer.Sound('Sound_effect\\ultimate_bg_sound.mp3')
        self.sound_ultimate.set_volume(0.2)





    '''Method to link input keys and player's movement'''
    def get_input(self):
        keys = pygame.key.get_pressed()
        self.current_ultimate_time = pygame.time.get_ticks()

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.walking_animation = True
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.walking_animation = True

        '''When ready to shoot and player press space'''
        if keys[pygame.K_SPACE]:
            if self.ultimate_run:
                if self.ultimate_pic_ready == True:
                    self.ultimate()
                    self.ultimate_pic_ready = False
                    self.recharge_ultimate = pygame.time.get_ticks()
                self.ultimate_call()
                self.ultimate_time_check()

            if not self.ultimate_run and self.shooting_ready:
                self.player_laser()
                self.shooting_ready = False
                self.laser_time = pygame.time.get_ticks()
                self.shoot_animating = True


            '''how many enemies should be killed before use ultimate power'''
        if self.level <= 5:
            if self.press_q is False:
                if keys[pygame.K_q] and self.countdown_ultimate >= 5:
                    self.ultimate_run = True
                    self.start_ultimate_time = pygame.time.get_ticks()
                    self.ultimate_player_pic_ready = True
                    self.image_order = 0
                    self.press_q = True

                    self.game_bg_channel.pause()
                    self.ultimate_channel.play(self.sound_ultimate)

        elif self.level > 5:
            if self.press_q is False:
                if keys[pygame.K_q] and self.countdown_ultimate >= 10:
                    self.ultimate_run = True
                    self.start_ultimate_time = pygame.time.get_ticks()
                    self.ultimate_player_pic_ready = True
                    self.image_order = 0
                    self.press_q = True

                    self.game_bg_channel.pause()
                    self.ultimate_channel.play(self.sound_ultimate)



    def ultimate_call(self):                     ## The distance of ultimate power pic
        if not self.ultimate_pic_ready:
            current_recharge = pygame.time.get_ticks()
            if current_recharge - self.recharge_ultimate >= 200:
                self.ultimate_pic_ready = True


    def ultimate_time_check(self):
        if self.ultimate_run is True:
            curren_time_ultimate = pygame.time.get_ticks()
            if curren_time_ultimate - self.start_ultimate_time >= self.ultimate_period:
                self.ultimate_run = False
                self.countdown_ultimate = 0
                self.press_q = False
                self.ultimate_player_pic_ready = False
                self.ultimate_channel.stop()
                self.game_bg_channel.unpause()



    def player_ultimate_pic(self):
        if self.ultimate_player_pic_ready is True and self.ultimate_run is True:
            self.frame_ultimate += 1
            if self.frame_ultimate % 3 == 0:
                self.image_order += 1

            if self.image_order >= len(self.ultimate_player_list):
                self.image_order = 0
                self.frame_ultimate = 0

            self.image = self.ultimate_player_list[self.image_order]




    def recharge_laser(self):
        if not self.shooting_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.shooting_ready = True

    def shooting_pic(self):
        if self.shoot_animating is True:
            self.image_order += 1

            if self.image_order >= len(self.shooting_image_list):
                self.image_order = 0
                self.shoot_animating = False

            self.image = self.shooting_image_list[self.image_order]

        else:
            self.image = pygame.image.load('Pic\Player\Player.png').convert_alpha()



    '''Limit movement of the player'''
    def screen_constraint(self):
        if self.rect.top <= 250:
            self.rect.top = 250
        elif self.rect.bottom >= self.max_constraint:
            self.rect.bottom = self.max_constraint

    '''Creating player's laser'''
    def player_laser(self):
        self.lasers.add(Laser(self.rect.midleft,self.rect.bottom,self.level))
        self.player_laser_sound = pygame.mixer.Sound('Sound_effect\mixkit-retro-arcade-casino-notification-211.wav')
        self.player_laser_sound.set_volume(0.5)
        self.player_laser_sound.play()

    def ultimate(self):
        self.ultimatepower.add(Ultimatepower(self.rect.midleft,self.rect.bottom,self.level))

    def update(self):
        self.get_input()
        self.screen_constraint()
        self.recharge_laser()
        self.lasers.update()
        self.shooting_pic()
        self.ultimatepower.update()
        self.player_ultimate_pic()


