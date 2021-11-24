import pygame

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font('dogicapixelbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class Scenes():
    def __init__(self, level, screen):
        self.level = level - 1
        self.screen = screen
        self.step = 1

        self.text_box = pygame.image.load('Pic\\text_box\\text_box.png').convert_alpha()
        self.speak_box = pygame.image.load('Pic\\text_box\\speaker_box.png').convert_alpha()
        self.speak_box_rect = self.speak_box.get_rect(topleft=(1150, 460))

        '''Continue'''
        self.con = False
        self.re_space = True


        if self.level == 1:
            self.text = {
                1: ["Duck", "Hello, nice to meet you! "],
                2: ["Duck", "My name is Duck"],
                3: ["Mon1", "Bye"]
            }
        elif self.level == 2:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 3:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 4:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 5:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 6:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 7:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 8:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 9:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }
        elif self.level == 10:
            self.text = {
                1: ["Duck", "WHat"],
                2: ["Duck", "Why u look at me like that?"],
                3: ["Mon", "Yumma na"],
                4: ["Mon", "Hahahaha"]
            }

        self.text_counter = 0

        '''light ball'''
        self.image_list_light = []
        for index in range(10):
            image_name_light = 'Pic\\light_ball\\level' + str(self.level) + '\\level' +  str(self.level) + '-' + \
                               str(index + 1) + '.png'
            self.image_list_light.append(pygame.image.load(image_name_light).convert_alpha())

        self.image_order_light = 0
        self.frame_light = 0
        self.light_ball = self.image_list_light[self.image_order_light]
        self.light_x = 0
        self.light_y = 275

        '''Player'''
        self.image_list_player = []
        for index in range(14):
            image_name_player = 'Pic\\Player\\Walk\\Walk' + str(index + 1) + '.png'
            self.image_list_player.append(pygame.image.load(image_name_player).convert_alpha())

        self.image_order = 0
        self.image_player = self.image_list_player[self.image_order]
        self.player_x = 0
        self.player_y = 350
        self.run_player_pic = False
        self.run_player_action = False
        self.frame = 0

        '''Enemy'''
        self.enemy_list = []

        for index in range(10):
            image_name = 'Pic\\Enemy' + str(self.level) + '\\Enemy' + str(self.level) + '_' + str(index + 1) + '.png'
            self.enemy_list.append(pygame.image.load(image_name).convert_alpha())

        self.enemy_image_order = 0
        self.enemy_image = self.enemy_list[self.enemy_image_order]
        self.enemy_x = 1000
        self.enemy_y = 350
        self.enemy_frame = 0

    def enemy_pic(self):

        self.enemy_frame += 1
        if self.enemy_frame == 7:
            self.enemy_frame = 0
            self.enemy_image_order += 1

            if self.enemy_image_order >= len(self.enemy_list):
                self.enemy_image_order = 0

        self.enemy_image = self.enemy_list[self.enemy_image_order]

        self.screen.blit(self.enemy_image, (self.enemy_x, self.enemy_y))

    def light_pic(self):

        self.frame_light += 1
        if self.frame_light == 7:
            self.frame_light = 0
            self.image_order_light += 1

            if self.image_order_light >= len(self.image_list_light):
                self.image_order_light = 0

        self.light_ball = self.image_list_light[self.image_order_light]

        self.screen.blit(self.light_ball, (self.light_x, self.light_y))

    def player_pic(self):

        if self.run_player_pic is True:
            self.frame += 1
            if self.frame >= 1:
                self.frame = 0
                self.image_order += 1

                if self.image_order >= len(self.image_list_player):
                    self.image_order = 0

            self.image_player = self.image_list_player[self.image_order]

        else:
            self.image_player = self.image_list_player[0]

        self.screen.blit(self.image_player, (self.player_x, self.player_y))

    def pic_movement(self):
        if self.step == 1:

            self.run_player_pic = True
            if self.player_x >= 300:
                self.run_player_pic = False
                self.re_space = True
            elif self.player_x < 300:
                self.player_x += 5
                self.light_x += 10

        elif self.step == 2:
            if self.enemy_x > 800:
                self.enemy_x -= 5
            elif self.enemy_x <= 800:
                self.re_space = True
            if self.light_x < 1200:
                self.light_x += 10

        elif self.step == len(self.text):
            if self.enemy_x < 1210:
                self.enemy_x += 5
            elif self.enemy_x >= 1210:
                self.re_space = True
        else:
            self.re_space = True

    def text_update(self):
        keys = pygame.key.get_pressed()

        '''First dialogue'''
        if self.step == len(self.text) + 1:
                self.con = True

        elif int(self.text_counter) < len(self.text[self.step][1]):
            self.text_counter += 0.4

        elif int(self.text_counter) >= len(self.text[self.step][1]):
            font_space = pygame.font.Font('dogicapixelbold.ttf', 20)

            space_text_shadow = font_space.render(f'Press Space', False, (39, 20, 4))
            space_rect_shadow = space_text_shadow.get_rect(topright=(1105, 746))
            self.screen.blit(space_text_shadow, space_rect_shadow)

            space_text = font_space.render(f'Press Space', False, (255, 255, 255))
            space_rect = space_text.get_rect(topright=(1100, 745))
            self.screen.blit(space_text, space_rect)

            if keys[pygame.K_SPACE] and self.re_space is True:
                self.text_counter = 0
                self.step += 1
                self.re_space = False

        '''skip scene'''
        if keys[pygame.K_ESCAPE]:
            self.con = True

    def display_speaker(self):

        if self.step != len(self.text) + 1:
            font = pygame.font.Font('dogicapixelbold.ttf', 20)

            speaker_name_shadow = font.render(self.text[self.step][0], False, (39, 20, 4))
            speaker_rect_shadow = speaker_name_shadow.get_rect(topright=(10, 303))

            speaker_name = font.render(self.text[self.step][0], False, (255, 255, 255))
            speaker_rect = speaker_name.get_rect(topright=(5, 300))
            if self.text[self.step][0] != 'Duck':
                speaker_rect = speaker_name.get_rect(topright=(1050, 460))
                self.speak_box_rect = self.speak_box.get_rect(topleft=(950, 440))
                self.screen.blit(self.speak_box, self.speak_box_rect)
                speaker_rect_shadow = speaker_name_shadow.get_rect(topright=(1055, 463))

            elif self.text[self.step][0] == 'Duck':
                speaker_rect = speaker_name.get_rect(topright=(100, 460))
                self.speak_box_rect = self.speak_box.get_rect(topleft=(0, 440))
                self.screen.blit(self.speak_box, self.speak_box_rect)
                speaker_rect_shadow = speaker_name_shadow.get_rect(topright=(105, 461))

            self.screen.blit(speaker_name_shadow, speaker_rect_shadow)
            self.screen.blit(speaker_name, speaker_rect)


    def display_escape(self):
        font_esc = pygame.font.Font('dogicapixelbold.ttf', 20)
        esc_text_shadow = font_esc.render(f'Press ESC to skip', False, (0, 0, 0))
        esc_rect_shadow = esc_text_shadow.get_rect(topright=(1145, 13))
        self.screen.blit(esc_text_shadow, esc_rect_shadow)

        esc_text = font_esc.render(f'Press ESC to skip', False, (255, 255, 255))
        esc_rect = esc_text.get_rect(topright=(1150, 10))
        self.screen.blit(esc_text, esc_rect)

    def draw(self, screen):

        if self.step != len(self.text) + 1:
            draw_text(
                screen,
                self.text[self.step][1][0:int(self.text_counter)],
                25,
                (39, 20, 4),
                105,
                553
            )
            draw_text(
                screen,
                self.text[self.step][1][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                100,
                550
            )


    def check_con(self):
        if self.con is True:
            return False

    def runnning_scene(self):

        background_image = 'Pic\\bg\\bg' + str(self.level) + '.png'
        background = pygame.image.load(background_image)
        self.screen.blit(background, (0, 0))

        self.display_escape()
        self.display_speaker()

        display_surf = pygame.display.set_mode((0,600))
        display_surf.blit(self.text_box, (0, 500))
        self.text_update()

        self.draw(self.screen)
        self.pic_movement()
        self.player_pic()
        self.light_pic()
        self.enemy_pic()
        self.display_speaker()



class Walk_Scene():
    def __init__(self, level, screen, music):
        self.level = level - 1
        self.screen = screen
        # self.player_sprite = Player_scene_walk(self.level, (300,380))
        # self.player = pygame.sprite.GroupSingle(self.player_sprite)
        self.con = None

        self.image_list_player = []
        self.frame = 0

        for index in range(14):
            image_name_player = 'Pic\\Player\\Walk\\Walk' + str(index + 1) + '.png'
            self.image_list_player.append(pygame.image.load(image_name_player).convert_alpha())

        self.image_order = 0
        self.image_player = self.image_list_player[self.image_order]
        self.player_x = 300
        self.player_y = 350
        self.bg_x = 0
        self.music = music

    def player_pic(self):

        self.player_x += 5

        self.frame += 10
        if self.frame >= 20:
            self.frame = 0
            self.image_order += 1

            if self.image_order >= len(self.image_list_player):
                self.image_order = 0

        self.image_player = self.image_list_player[self.image_order]

        self.screen.blit(self.image_player,(self.player_x,self.player_y))

    def check_con(self):
        if self.player_x == 1200:
            return False
        if self.player_x == 1050:
            self.music.fadeout(600)

    # def check_walk_scene(self):
    #     return self.player_sprite.check_player()

    def running_scene(self):

        self.screen.fill(((0, 0, 0)))
        background_image = 'Pic\\bg\\bg' + str(self.level) + '.png'
        background = pygame.image.load(background_image)
        self.screen.blit(background, (0, 0))

        self.player_pic()

class Game_over_scene():

    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.Font('dogicapixel.ttf', 50)
        # self.image.player = pygame.image.load('Pic\\Player\\Player.png')
        self.score = score

    def display_text(self):
        font1 = pygame.font.Font('dogicapixelbold.ttf', 50)
        game_over_text = font1.render(f'Game Over', False, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(topright=(850, 300))
        self.screen.blit(game_over_text, game_over_rect)

        font2 = pygame.font.Font('dogicapixelbold.ttf', 20)
        press_text = font2.render(f'Press enter', False, (255,255,255))
        press_rect = press_text.get_rect(topright=(1000, 400))
        self.screen.blit(press_text, press_rect)

        font3 = pygame.font.Font('dogicapixelbold.ttf', 20)
        final_score = font3.render(f'score: {self.score}', False, (255, 255, 255))
        final_score_rect = final_score.get_rect(topright=(400, 400))
        self.screen.blit(final_score, final_score_rect)

    def update(self):

        self.screen.fill((0, 0, 0))
        self.display_text()

        # display_surf = pygame.display.set_mode((0, 600))
        #
        # display_surf.blit(self.image_player,(0,500))

class Intro():
    def __init__(self,screen):
        self.screen = screen
        self.image_list_player = []
        self.image_list_light = []
        self.frame = 0
        self.step = 0
        self.re_space = True

        for index in range(14):
            image_name_player = 'Pic\\Player\\Walk\\Walk' + str(index + 1) + '.png'
            self.image_list_player.append(pygame.image.load(image_name_player).convert_alpha())

        self.image_order = 0
        self.image_player = self.image_list_player[self.image_order]
        self.player_x = 0
        self.player_y = 350
        self.run_player_pic = False
        self.run_player_action = False

        for index in range(10):
            image_name_light = 'Pic\\light_ball\\intro\\' + str(index + 1) + '.png'
            self.image_list_light.append(pygame.image.load(image_name_light).convert_alpha())

        self.image_order_light = 0
        self.frame_light = 0
        self.light_ball = self.image_list_light[self.image_order_light]
        self.light_x = 0
        self.light_y = 275

        '''Intro music'''
        self.music = pygame.mixer.Sound('Music\\level\\intro.mp3')
        self.music.set_volume(0.2)
        self.music.play(loops=-1)

    def player_pic(self):

        if self.run_player_pic is True:
            self.frame += 1
            if self.frame >= 1:
                self.frame = 0
                self.image_order += 1

                if self.image_order >= len(self.image_list_player):
                    self.image_order = 0

            self.image_player = self.image_list_player[self.image_order]

        elif self.run_player_action is True:
            self.image_player = pygame.image.load('Pic\\Player\\intro\\!.png')

        else:
            self.image_player = self.image_list_player[0]

        self.screen.blit(self.image_player, (self.player_x, self.player_y))

    def light_pic(self):

        self.frame_light += 1
        if self.frame_light == 7:
            self.frame_light = 0
            self.image_order_light += 1

            if self.image_order_light >= len(self.image_list_light):
                self.image_order_light = 0

        self.light_ball = self.image_list_light[self.image_order_light]

        if self.step >= 2:
            self.screen.blit(self.light_ball, (self.light_x, self.light_y))

    def step_display(self):
        if self.re_space is False:
            if self.step == 1:
                self.run_player_pic = True
                self.player_x += 5
                if self.player_x >= 200:
                    self.re_space = True
                    self.run_player_pic = False

            elif self.step == 2:
                self.light_x += 3
                if self.light_x >= 500:
                    self.re_space = True

            elif self.step == 3:
                self.run_player_pic = True
                self.player_x += 5
                if self.player_x >= 300:
                    self.re_space = True
                    self.run_player_pic = False

            elif self.step == 4:
                self.run_player_action = True
                self.image_player = pygame.image.load('Pic\\Player\\intro\\!.png')
                self.light_y -= 2
                if self.light_y < 225:
                    self.re_space = True

            elif self.step == 5:
                self.run_player_action = False
                self.light_x += 10
                if self.light_y <= 275:
                    self.light_y += 2
                if self.light_x > 1200:
                    self.re_space = True

            elif self.step == 6:
                self.run_player_pic = True
                self.player_x += 5
                if self.player_x == 1050:
                    self.music.fadeout(30)
                if self.player_x >= 1200:
                    self.re_space = True
                    self.run_player_pic = False
                    self.step += 1

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.re_space is True:
            self.step += 1
            self.re_space = False

        elif keys[pygame.K_ESCAPE]:
            self.music.fadeout(30)
            self.step = 7

    def display_escape(self):
        font_esc = pygame.font.Font('dogicapixelbold.ttf', 20)

        esc_text_shadow = font_esc.render(f'Press ESC to skip', False, (0, 0, 0))
        esc_rect_shadow = esc_text_shadow.get_rect(topright=(1145, 13))
        self.screen.blit(esc_text_shadow, esc_rect_shadow)

        esc_text = font_esc.render(f'Press ESC to skip', False, (255, 255, 255))
        esc_rect = esc_text.get_rect(topright=(1150, 10))
        self.screen.blit(esc_text, esc_rect)

    def running(self):
        background = pygame.image.load('Pic\\bg\\bg1.png')
        self.screen.blit(background, (0, 0))
        self.display_escape()

        self.player_pic()
        self.light_pic()
        self.get_input()
        self.step_display()

        if self.step == 7:
            return False
        else:
            return True

class End_scene():
    def __init__(self, screen):
        self.screen = screen
        self.image_list_player = []
        self.image_list_light = []
        self.frame = 0
        self.step = 0
        self.re_space = True

        for index in range(14):
            image_name_player = 'Pic\\Player\\Walk\\Walk' + str(index + 1) + '.png'
            self.image_list_player.append(pygame.image.load(image_name_player).convert_alpha())

        self.image_order = 0
        self.image_player = self.image_list_player[self.image_order]
        self.player_x = 0
        self.player_y = 350
        self.run_player_pic = False
        self.run_player_action = False

        for index in range(10):
            image_name_light = 'Pic\\light_ball\\end\\' + str(index + 1) + '.png'
            self.image_list_light.append(pygame.image.load(image_name_light).convert_alpha())

        self.image_order_light = 0
        self.frame_light = 0
        self.light_ball = self.image_list_light[self.image_order_light]
        self.light_x = 0
        self.light_y = 275

        '''Music'''
        self.music = pygame.mixer.Sound('Music\\level\\end.mp3')
        self.music.set_volume(0.2)
        self.music.play()

        '''Sound Effect'''
        self.sound = pygame.mixer.Sound('Sound_effect\\glass_break.mp3')
        self.sound.set_volume(0.7)
        self.trigger_sound = 0

        self.font = pygame.font.Font('dogicapixelbold.ttf', 20)



    def player_pic(self):

        if self.run_player_pic is True:
            self.frame += 8
            if self.frame >= 20:
                self.frame = 0
                self.image_order += 1

                if self.image_order >= len(self.image_list_player):
                    self.image_order = 0

            self.image_player = self.image_list_player[self.image_order]

        elif self.run_player_action is True:
            self.image_player = pygame.image.load('Pic\\Player\\intro\\!.png')

        else:
            self.image_player = self.image_list_player[0]

        if 2 <= self.step:
            self.screen.blit(self.image_player, (self.player_x, self.player_y))

    def light_pic(self):

        self.frame_light += 1
        if self.frame_light == 7:
            self.frame_light = 0
            self.image_order_light += 1

            if self.image_order_light >= len(self.image_list_light):
                self.image_order_light = 0

        self.light_ball = self.image_list_light[self.image_order_light]

        if 1 <= self.step:
            self.screen.blit(self.light_ball, (self.light_x, self.light_y))

    def step_display(self):
        if self.re_space is False:

            if self.step == 1:
                self.light_x += 10
                if self.light_x >= 600:
                    self.re_space = True

            elif self.step == 2:
                self.player_x += 5
                if self.player_x >= 450:
                    self.re_space = True

            elif self.step == 3:
                if self.light_y <= 350:
                    self.light_y += 2

                self.player_x += 2
                if self.player_x >= 565:
                    self.re_space = True

            elif self.step == 4:
                self.music.fadeout(300)
                self.re_space = True

            elif self.step == 5:
                self.trigger_sound += 1
                if self.trigger_sound == 1:
                    self.sound.play()
                self.re_space = True

            elif self.step == 6:
                self.re_space = True

            else:
                self.re_space = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.re_space is True:
            self.step += 1
            self.re_space = False

    def running(self):
        background = pygame.image.load('Pic\\bg\\end.png')
        self.screen.blit(background, (0, 0))

        self.player_pic()
        self.light_pic()
        self.get_input()
        self.step_display()

        if self.step >= 5:
            self.screen.fill((0, 0, 0))
        if self.step > 6:
            end_text = self.font.render(f'The end', False, (255, 255, 255))
            end_rect = end_text.get_rect(topright=(1100, 745))
            self.screen.blit(end_text, end_rect)
            pygame.time.delay(100)
            self.re_space = True

        if self.step >= 8:
            return False
        else:
            return True


