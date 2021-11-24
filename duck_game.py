import pygame
from Player import Duck_Player
from Enemy import Enemy
from Laser import Enemy_laser
from random import choice,randint
from item import Item

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font('dogicapixelbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class Duck_Game:
    def __init__(self, level, score, heart, status, game_bg_channel, music):
        '''health and score'''
        self.heart = heart
        self.heart_surf = pygame.image.load('Pic\heart.png').convert_alpha()
        self.heart_x_start_heart = 0 + (self.heart_surf.get_size()[0])

        self.multiply = 1
        self.score = score
        '''font and size'''
        self.font = pygame.font.Font('dogicapixelbold.ttf', 20)

        '''level'''
        self.level = level
        self.status = status

        '''Setup for enemies'''
        '''Enemies position'''
        self.enemies_laser = pygame.sprite.Group()
        enemy_posx = set()
        enemy_posy = set()
        if self.level % 2 == 1:
            for index in range(4):
                enemy_posy.add(250+index*140)

            for index in range(self.level*2):
                enemy_posx.add(1000+index*150)
        if self.level % 2 == 0:
            for index in range(8):
                if index <= 4:
                    enemy_posy.add(250+index*110)
                enemy_posy.add(250+index*55)
            for index in range(self.level*2):
                enemy_posx.add(1000+index*150)

        enemy_posx = list(sorted(enemy_posx))
        enemy_posy = list(sorted(enemy_posy))

        self.enemy_list = pygame.sprite.Group()
        for number_x in range(len(enemy_posx)):
            for number_y in range(len(enemy_posy)):
                if self.level % 2 == 1:
                    enemies_sprites = Enemy(enemy_posx[number_x], enemy_posy[number_y], self.level)

                elif self.level % 2 == 0:
                    if number_x % 2 == 0 and number_y%2 == 0:
                        enemies_sprites = Enemy(enemy_posx[number_x], enemy_posy[number_y], self.level)
                    elif number_x % 2 == 1 and number_y%2 == 1:
                        enemies_sprites = Enemy(enemy_posx[number_x], enemy_posy[number_y], self.level)

                self.enemy_list.add(enemies_sprites)


        '''-----check position at x = 0 for Game Over-----'''
        self.enemy_pos_check = True

        '''-----Item-----'''
        self.spawn = True
        '''Heart'''
        self.item_ready_heart = False
        self.item_time_heart = 0
        self.item_list_heart = pygame.sprite.Group()
        self.item_time_heart = pygame.time.get_ticks()
        '''Double score'''
        self.timer_multiple_score = 0
        self.multiple_score = False
        self.multiple_period = 10000
        self.item_ready_double = False
        self.item_time_double = 0
        self.item_list_double = pygame.sprite.Group()
        self.item_time_double = pygame.time.get_ticks()


        '''-----Text for enter-----'''
        self.text_enter = {1: 'Press enter'}
        self.text_counter = 0

        '''-----spawn laser-----'''
        self.spawn_laser = False
        self.count_laser_spawn = 0

        self.continue_game = True

        '''-----Ultimate bar-----'''
        self.ultimate_size = 0
        self.color_code1, self.color_code2, self.color_code3 = 255, 255, 255
        self.count_color_change = 0

        '''-----Music-----''' '''channel 1'''
        self.music = music

        '''-----Sound effect-----''' '''channel 3'''
        '''collect heart'''
        self.sound_heart = pygame.mixer.Sound('Sound_effect\\sound_heart.mp3')
        self.sound_heart.set_volume(0.5)

        '''multiple score period sound''' '''channel 1'''

        self.sound_multiple = pygame.mixer.Sound('Sound_effect\\sound_multiple.mp3')
        self.sound_multiple.set_volume(0.1)
        self.trigger_sound_multiple = 0

        '''Ultimate hit sound'''

        '''Bg channel'''
        self.game_bg_channel = game_bg_channel
        self.sound_effect_channel = pygame.mixer.Channel(3)



        '''enemy Laser sound'''
        self.laser_sound = pygame.mixer.Sound('Sound_effect\ES_Laser Gun Fire 4 - SFX Producer.mp3')
        self.laser_sound.set_volume(0.5)

        '''Player Setup'''
        player_sprite = Duck_Player((50, 350), screen_height, level, self.game_bg_channel)

        self.player = pygame.sprite.GroupSingle(player_sprite)


    def laser_spawnning(self):
        if self.count_laser_spawn >= 100:
            self.spawn_laser = True
        else:
            self.count_laser_spawn += 1

    def draw(self, screen):
        draw_text(
            screen,
            self.text_enter[1][0:int(self.text_counter)],
            30,
            (0, 0, 0),
            475,
            403

        )
        draw_text(
            screen,
            self.text_enter[1][0:int(self.text_counter)],
            30,
            (255, 255, 255),
            470,
            400

        )

    def spawn_item(self):
        if self.spawn is True:
            if self.item_ready_heart:
                item_x_pos = randint(900, 1100)
                items_sprites = Item(item_x_pos, 0, screen_height, 'heart', self.level)
                self.item_list_heart.add(items_sprites)
                self.item_ready_heart = False
                self.item_time_heart = pygame.time.get_ticks()

            if self.item_ready_double:
                item_x_pos = randint(900, 1100)
                items_sprites = Item(item_x_pos, 0, screen_height, '2xscore', self.level)
                self.item_list_double.add(items_sprites)
                self.item_ready_double = False
                self.item_time_double = pygame.time.get_ticks()

    def checking_item_cooldown(self):
        '''Heart cooldown'''
        if not self.item_ready_heart:
            self.item_cooldown_heart = randint(10000, 60000)
            counting_time_heart = pygame.time.get_ticks()
            if counting_time_heart - self.item_time_heart >= self.item_cooldown_heart:
                self.item_ready_heart = True

            '''Double Score cooldown'''
        if not self.item_ready_double:
            self.item_cooldown_double = randint(20000, 60000)
            counting_time_double = pygame.time.get_ticks()
            if counting_time_double - self.item_time_double >= self.item_cooldown_double:
                self.item_ready_double = True

    '''Enemies's laser'''
    def enemies_shoot(self):
        if self.spawn_laser is True:
            if self.enemy_list.sprites():
                random_enemy1 = choice(self.enemy_list.sprites())
                '''Only spawn laser if the enemy is in the frame'''
                if random_enemy1.rect.x <= 1200:
                    laser_sprite1 = Enemy_laser(random_enemy1.rect.center, screen_width, self.level)
                    self.enemies_laser.add(laser_sprite1)
                if self.level > 5:
                    random_enemy2 = choice(self.enemy_list.sprites())
                    if random_enemy2.rect.x <= 1200:
                        laser_sprite2 = Enemy_laser(random_enemy2.rect.center, screen_width, self.level)
                        self.enemies_laser.add(laser_sprite2)
                        self.laser_sound.play()


    def checking_collision(self):

        '''player's laser'''
        '''Time for double score'''

        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                '''Hit Enemies'''
                if pygame.sprite.spritecollide(laser, self.enemy_list, True, pygame.sprite.collide_mask):
                    laser.kill()
                    self.score += 100*self.multiply
                    self.player.sprite.countdown_ultimate += 1
                    if self.player.sprite.ultimate_run is False:
                        if self.ultimate_size != 250 and self.level <= 5:
                            self.ultimate_size += 50
                        elif self.ultimate_size != 250 and self.level > 5:
                            self.ultimate_size += 25

                elif pygame.sprite.spritecollide(laser, self.item_list_heart, True, pygame.sprite.collide_mask):
                        self.sound_effect_channel.play(self.sound_heart)
                        self.heart += 1
                        laser.kill()
                elif pygame.sprite.spritecollide(laser, self.item_list_double, True, pygame.sprite.collide_mask)\
                            and self.multiple_score is False:
                        laser.kill()
                        self.multiply = 2
                        self.timer_multiple_score = pygame.time.get_ticks()
                        self.multiple_score = True

        if self.player.sprite.ultimatepower:
            for ultimate in self.player.sprite.ultimatepower:
                if pygame.sprite.spritecollide(ultimate, self.enemy_list, True, pygame.sprite.collide_mask):
                    ultimate.kill()
                    self.score += 100 * self.multiply
                elif pygame.sprite.spritecollide(ultimate, self.item_list_heart, True, pygame.sprite.collide_mask):
                    self.sound_effect_channel.play(self.sound_heart)
                    self.heart += 1
                    ultimate.kill()
                elif pygame.sprite.spritecollide(ultimate, self.item_list_double, True, pygame.sprite.collide_mask)\
                            and self.multiple_score is False:
                        ultimate.kill()
                        self.multiply = 2
                        self.timer_multiple_score = pygame.time.get_ticks()
                        self.multiple_score = True


        '''Skipping for check'''
        keys = pygame.key.get_pressed()

        '''Next level'''
        if len(self.enemy_list) == 0:
            self.spawn = False
            if int(self.text_counter) < len(self.text_enter[1]):
                self.text_counter += 0.4
            self.draw(screen)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                self.status = False
                self.level += 1
        '''Skipping for check'''
        if keys[pygame.K_ESCAPE]:
            self.status = False
            self.level += 1
            # self.music.stop()


        #     '''additional heart'''
            # if self.heart >= self.heart-2:
            #     self.heart += 1


        '''enemies Laser'''
        global check
        if self.enemies_laser:
            for laser in self.enemies_laser:
                '''Hit the player'''
                if pygame.sprite.spritecollide(laser, self.player, False, pygame.sprite.collide_mask):
                    laser.kill()
                    self.heart -= 1
                    '''Exit'''
                    if self.heart <= 0:
                        self.continue_game = False
                        self.status = False
                        # self.music.stop()
                        # check = False
                        # pygame.quit()
                        # sys.exit()


        '''enemy hit with the player'''
        if self.enemy_list:
            for enemy in self.enemy_list:
                if pygame.sprite.spritecollide(enemy, self.player, False, pygame.sprite.collide_mask):
                    self.continue_game = False
                    self.status = False
                    # self.music.stop()
                    # pygame.quit()
                    # sys.exit()

        '''player hit with heart'''
        if self.item_list_heart:
             for heart in self.item_list_heart:
                 if pygame.sprite.spritecollide(heart, self.player, False, pygame.sprite.collide_mask):
                     self.sound_effect_channel.play(self.sound_heart)
                     heart.kill()
                     self.heart += 1

        if self.item_list_double:
             for double in self.item_list_double:
                 if pygame.sprite.spritecollide(double, self.player,False, pygame.sprite.collide_mask):
                    double.kill()
                    self.multiply = 2
                    self.multiple_score = True
                    self.timer_multiple_score = pygame.time.get_ticks()


    def display_heart(self):
        if self.heart:
            display_heart = self.heart
            x = 15
            for heart in range(1,display_heart+1):
                if heart == 11:
                    x = 15
                if heart > 10:
                    screen.blit(self.heart_surf, (x, 48))
                    x += 40
                else:
                    screen.blit(self.heart_surf, (x, 8))
                    x += 40

        # for heart in range(self.heart):
        #     x = self.heart_x_start_heart + (heart * (self.heart_surf.get_size()[0] + 10))
        #     screen.blit(self.heart_surf,(x,8))

    def display_score(self):
        score_surf_shadow = self.font.render(f'score: {self.score}', False, (0, 0, 0))
        score_rect_shadow = score_surf_shadow.get_rect(topright=(screen_width - 105, 11))
        screen.blit(score_surf_shadow, score_rect_shadow)

        score_surf = self.font.render(f'score: {self.score}', False, (255, 255, 255))
        score_rect = score_surf.get_rect(topright = (screen_width-100,8))
        screen.blit(score_surf, score_rect)

    def display_multiply(self):

        if not self.multiple_score:
            multiple_surf = self.font.render(f'', True, (255, 255, 255))
            multiple_surf_shadow = self.font.render(f'', False, (0, 0, 0))

        elif self.multiple_score:
            self.trigger_sound_multiple += 1
            current_time = pygame.time.get_ticks()
            if current_time - self.timer_multiple_score >= self.multiple_period:
                self.multiply = 1
                self.multiple_score = False
                self.game_bg_channel.play(self.music)

            multiple_surf_shadow = self.font.render(f'multiple', False, (0, 0, 0))
            multiple_surf = self.font.render(f'multiple', False, (255,  255, 255))

        multiple_rect_shadow = multiple_surf_shadow.get_rect(topright=(screen_width - 505, 11))
        screen.blit(multiple_surf_shadow, multiple_rect_shadow)

        multiple_rect = multiple_surf.get_rect(topright=(screen_width - 500, 8))
        screen.blit(multiple_surf, multiple_rect)

        if self.trigger_sound_multiple == 1:
            self.game_bg_channel.play(self.sound_multiple)

    def display_ultimate_bar(self):
        keys = pygame.key.get_pressed()

        bar_bg = pygame.image.load('Pic\\Ultimate_bar\\Ultimate_bar.png')
        icon_bar = pygame.image.load('Pic\\Ultimate_bar\\Icon_bar.png')


        font_q = pygame.font.Font('dogicapixel.ttf', 30)
        text_q = font_q.render(f'Q', False, (self.color_code1, self.color_code2, self.color_code3))

        if self.heart <= 10:

            screen.blit(bar_bg, (15, 58))
            screen.blit(icon_bar, (15, 50))
            text_q_rect = text_q.get_rect(topright=(50, 60))
            screen.blit(text_q, text_q_rect)
            pygame.draw.rect(screen, (self.color_code1, self.color_code2, self.color_code3),
                             pygame.Rect(59, 63, self.ultimate_size, 20))

        elif self.heart > 10:

            screen.blit(bar_bg, (15, 98))
            screen.blit(icon_bar, (15, 90))
            text_q_rect = text_q.get_rect(topright=(50, 100))
            screen.blit(text_q, text_q_rect)
            pygame.draw.rect(screen, (self.color_code1, self.color_code2, self.color_code3),
                             pygame.Rect(59, 103, self.ultimate_size, 20))

        if self.ultimate_size == 250:
            if keys[pygame.K_q]:
                self.ultimate_size = 0
                self.color_code1, self.color_code2, self.color_code3 = 255,255,255
            else:
                self.count_color_change += 1
                if self.count_color_change == 5:
                    self.color_code1 = randint(150, 255)
                    self.color_code2 = randint(150, 255)
                    self.color_code3 = randint(150, 255)
                    self.count_color_change = 0


        '''left top width height'''

    def check_status(self):
        if self.status is False:
            return False

    def check_con_pos_enemy(self):
        for enemy in self.enemy_list.sprites():
            if enemy.rect.x == 0:
                self.status = False
                self.enemy_pos_check = False
                # self.music.stop()


    def running_game(self):
        self.player.update()
        self.enemy_list.update()
        self.checking_collision()
        self.enemies_laser.update()
        self.item_list_heart.update()
        self.item_list_double.update()
        self.spawn_item()
        self.checking_item_cooldown()
        self.laser_spawnning()
        self.check_con_pos_enemy()


        self.player.sprite.lasers.draw(screen)
        self.player.sprite.ultimatepower.draw(screen)
        self.player.draw(screen)
        self.enemy_list.draw(screen)
        self.enemies_laser.draw(screen)
        self.item_list_heart.draw(screen)
        self.item_list_double.draw(screen)
        self.display_heart()
        self.display_score()
        self.display_multiply()
        self.display_ultimate_bar()


        if self.continue_game is False or self.enemy_pos_check is False:
            return False

##########################################################################################################
