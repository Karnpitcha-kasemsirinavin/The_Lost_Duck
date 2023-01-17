import pygame


def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font('dogicapixelbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class Scenes:
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
                1: ["???", "Who are you?"],
                2: ["Duck", "Quack!"],
                3: ["???", "Oh...you lost your memories?"],
                4: ["Duck", "Quack!"],
                5: ["???", "We are Polo tribe! So, what make you come here?"],
                6: ["Duck", "Quack! Quack!"],
                7: ["Polo", "What? You follow a light ball?"],
                8: ["Polo", "Which light ball? I haven't seen any of it."],
                9: ["Duck", "Quack! Quack! Quack!"],
                10: ["Polo", "....."],
                11: ["Polo", "Don't lie! We don't believe you!"],
                12: ["Polo", "Go away!"],
                13: ["Duck", "....."],

            }
        elif self.level == 2:
            self.text = {
                1: ["Duck", "Quack!"],
                2: ["???", "Who are we? We are Deaire tribe."],
                3: ["Duck", "Quack! Quack!"],
                4: ["Deaire", "So, you lost your memories"],
                5: ["Deaire", "and follow some light ball here?"],
                6: ["Duck", "Quack! Quack! Quack!"],
                7: ["Deaire", "Mmm... Maybe your family is in the forest."],
                8: ["Duck", "Quack?"],
                9: ["Deaire", "I once saw the tribe that similar to you."],
                10: ["Deaire", "They have white fur like you."],
                11: ["Deaire", "Why don't you go there."],
                12: ["Deaire", " You might be able to remember something."],
                13: ["Duck", "Quack! Quack!"],
                14: ["Deaire", "Good Luck!"]
            }
        elif self.level == 3:
            self.text = {
                1: ["???", "Grrr"],
                2: ["Duck", "Quack..."],
                3: ["???", "Grrrrrr!"],
                4: ["Duck", "Quack! Quack! Quack!"]
            }
        elif self.level == 4:
            self.text = {
                1: ["Duck", "Quack!"],
                2: ["???", "Are you okay?"],
                3: ["Duck", "Quack! Quack!"],
                4: ["???", "Ah! You are running from the Fover."],
                5: ["???", "We are Blue."],
                6: ["Duck", "Quack! Quack?"],
                7: ["Blue", "You want to drink OUR water?"],
                8: ["Duck", "Quack!"],
                9: ["Blue", "I don't think we can share it with you."],
                10: ["Duck", "Quack?"],
                11: ["Blue", "You are a stranger. We don't really know you."],
                12: ["Duck", "Quack..."],
                13: ["Blue", "I'm sorry."],
                14: ["Duck", "Quack?"],
                15: ["Blue", "Oh! I think they are the next tribe."],
                16: ["Blue", "Go into deeper and you will find them."],
                17: ["Duck", "Quack!"]
            }
        elif self.level == 5:
            self.text = {
                1: ["Duck", "Quack!"],
                2: ["???", "We are Pao."],
                3: ["Duck", "Quack! Quack!"],
                4: ["Pao", "You mean you are one of us?"],
                5: ["Pao", "But we don't think so."],
                6: ["Pao", "Despite the color"],
                7: ["Pao", "you don't have anything like us"],
                8: ["Duck", "Quack?"],
                9: ["Pao", "I definitely sure we are NOT your family."],
                10: ["Duck", "....."],
                11: ["Pao", "Maybe you can ask the Firb tribe."],
                12: ["Duck", "Quack!"]

            }
        elif self.level == 6:
            self.text = {
                1: ["Duck", "Quack! Quack!"],
                2: ["Firb", "You are from Pao tribe?"],
                3: ["Duck", "Quack!"],
                4: ["Firb", "Ah...Sorry ,but we also not your family."],
                5: ["Duck", "Quack..."],
                6: ["Firb", "But I know who can help you."],
                7: ["Duck", "Quack?"],
                8: ["Firb", "There are fairies who would be able to help you"],
                9: ["Firb", "They live inside the Moon forest."],
                10: ["Duck", "Quack?"],
                11: ["Firb", "Just go along the path and you will find them."],
                12: ["Duck", "Quack!"]
            }
        elif self.level == 7:
            self.text = {
                1: ["???", "Who are you?"],
                2: ["Duck", "Quack!"],
                3: ["???", "You want to go into the Moon forest?"],
                4: ["Duck", "Quack! Quack! Quack?"],
                5: ["???", "hahaha...No, we are not the fairies."],
                6: ["Duck", "Quack?"],
                7: ["???", "We are Fink tribe."],
                8: ["Fink", "If you want to find the fairies."],
                9: ["Fink", "You have to find the place"],
                10: ["Fink", "where you can see the moon clearly."],
                11: ["Duck", "Quack!"],
                12: ["Fink", "But be careful."],
                13: ["Fink", "The night in the forest is very dangerous."],
                14: ["Duck", "Quack!"]
            }
        elif self.level == 8:
            self.text = {
                1: ["Duck", "Quack! Quack!"],
                2: ["???", "Come here, come closer."],
                3: ["Duck", "Quack???"],
                4: ["???", "Just come closer."],
                5: ["Duck", "Quack..."],
                6: ["???", "Come closer,and we Ladyfrog will eat you!"],
                7: ["Duck", "Quack! Quack! Quack!"]
            }
        elif self.level == 9:
            self.text = {
                1: ["Duck", "Quack! Quack!"],
                2: ["???", "Calm down. Clam down. "],
                3: ["Duck", "Quack!!!"],
                4: ["???", "Yes, we are the fairies"],
                5: ["Fairy", "You want to find you family ,right?"],
                6: ["Duck", "Quack! Quack!"],
                7: ["Fairy", "Walk along the river"],
                8: ["Fairy", "and you will find them."],
                9: ["Fairy", "Don't get your hopes too high."],
                10: ["Fairy", "Everything might not turn out"],
                11: ["Fairy", "to be like what you expected."],
                12: ["Duck", "....."]
            }
        elif self.level == 10:
            self.text = {
                1: ["Duck", "Quack! Quack! Quack!"],
                2: ["Family", "Quack! Quack?"],
                3: ["Duck", "Quack!?"],
                4: ["Family", "Quack! Quack! Quack! Quack!"],
                5: ["Duck", "Quack..."],
                6: ["Family", "Quack! Quack! Quack! Quack!"],
                7: ["Duck", "....."]
            }

        self.text_counter = 0

        '''light ball'''
        self.image_list_light = []
        for index in range(10):
            image_name_light = 'Pic\\light_ball\\level' + str(self.level) + '\\level' + str(self.level) + '-' + \
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

            if self.light_x < 1210:
                self.light_x += 10

            if self.enemy_x > 800:
                self.enemy_x -= 5

            elif self.light_x >= 1210 and self.enemy_x <= 800:
                self.re_space = True

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
                speaker_rect = speaker_name.get_rect(topright=(1100, 460))
                self.speak_box_rect = self.speak_box.get_rect(topleft=(950, 440))
                self.screen.blit(self.speak_box, self.speak_box_rect)
                speaker_rect_shadow = speaker_name_shadow.get_rect(topright=(1105, 463))

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

    def running_scene(self):

        display_surf = pygame.display.set_mode((0, 600))

        self.screen.fill((0, 0, 0))
        background_image = 'Pic\\bg\\bg' + str(self.level) + '.png'
        background = pygame.image.load(background_image)
        self.screen.blit(background, (0, 0))

        self.display_escape()
        self.display_speaker()

        display_surf.blit(self.text_box, (0, 500))
        self.text_update()

        self.draw(self.screen)
        self.pic_movement()
        self.player_pic()
        self.light_pic()
        self.enemy_pic()
        self.display_speaker()


class Walk_Scene:
    def __init__(self, level, screen, music):
        self.level = level - 1
        self.screen = screen
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

        self.screen.blit(self.image_player, (self.player_x, self.player_y))

    def check_con(self):
        if self.player_x == 1200:
            return False
        if self.player_x == 1050:
            self.music.fadeout(600)

    def running_scene(self):

        self.screen.fill((0, 0, 0))
        background_image = 'Pic\\bg\\bg' + str(self.level) + '.png'
        background = pygame.image.load(background_image)
        self.screen.blit(background, (0, 0))

        self.player_pic()


class Game_over_scene:

    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.Font('dogicapixel.ttf', 50)
        self.score = score

    def display_text(self):
        font1 = pygame.font.Font('dogicapixelbold.ttf', 50)
        game_over_text = font1.render(f'Game Over', False, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(topright=(850, 300))
        self.screen.blit(game_over_text, game_over_rect)

        font2 = pygame.font.Font('dogicapixelbold.ttf', 20)
        press_text = font2.render(f'Press enter', False, (255, 255, 255))
        press_rect = press_text.get_rect(topright=(1000, 400))
        self.screen.blit(press_text, press_rect)

        font3 = pygame.font.Font('dogicapixelbold.ttf', 20)
        final_score = font3.render(f'score: {self.score}', False, (255, 255, 255))
        final_score_rect = final_score.get_rect(topright=(400, 400))
        self.screen.blit(final_score, final_score_rect)

    def update(self):
        self.screen.fill((0, 0, 0))
        self.display_text()


class Intro:
    def __init__(self, screen, game_bg_channel):
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
        self.game_bg_channel = game_bg_channel

        self.game_bg_channel.play(self.music, loops=-1)

        self.startle = 0

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
            if self.startle <= 1:
                self.startle += 1
            if self.startle == 1:
                startle = pygame.mixer.Sound('Sound_effect\\startle.wav')
                startle.set_volume(0.3)
                startle.play()
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
                if self.player_x >= 1250:
                    self.game_bg_channel.stop()
                    self.re_space = True
                    self.run_player_pic = False
                    self.step += 1

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.re_space is True:
            self.step += 1
            self.re_space = False

        elif keys[pygame.K_ESCAPE]:
            self.game_bg_channel.stop()
            self.step = 7

    def display_escape(self):
        font_esc = pygame.font.Font('dogicapixelbold.ttf', 20)

        esc_text_shadow = font_esc.render(f'Press ESC to skip', False, (0, 0, 0))
        esc_rect_shadow = esc_text_shadow.get_rect(topright=(1145, 13))
        self.screen.blit(esc_text_shadow, esc_rect_shadow)

        esc_text = font_esc.render(f'Press ESC to skip', False, (255, 255, 255))
        esc_rect = esc_text.get_rect(topright=(1150, 10))
        self.screen.blit(esc_text, esc_rect)

    def display_space(self):
        if self.re_space is True:
            font_space = pygame.font.Font('dogicapixelbold.ttf', 20)

            space_text_shadow = font_space.render(f'Press Space', False, (39, 20, 4))
            space_rect_shadow = space_text_shadow.get_rect(topright=(1095, 746))
            self.screen.blit(space_text_shadow, space_rect_shadow)

            space_text = font_space.render(f'Press Space', False, (255, 255, 255))
            space_rect = space_text.get_rect(topright=(1100, 745))
            self.screen.blit(space_text, space_rect)

    def running(self):
        background = pygame.image.load('Pic\\bg\\bg1.png')
        self.screen.blit(background, (0, 0))
        self.display_escape()
        self.display_space()

        self.player_pic()
        self.light_pic()
        self.get_input()
        self.step_display()

        if self.step == 7:
            return False
        else:
            return True


class End_scene:
    def __init__(self, screen, display_score):
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
        self.music.set_volume(0.1)
        self.music.play(loops=-1)

        '''Sound Effect'''
        self.sound = pygame.mixer.Sound('Sound_effect\\glass_break.mp3')
        self.sound.set_volume(0.5)
        self.trigger_sound = 0

        '''Font'''
        self.font = pygame.font.Font('dogicapixelbold.ttf', 20)

        '''Final score'''
        self.final_score = display_score

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

    def display_space(self):
        if self.re_space is True and self.step <= 6:
            font_space = pygame.font.Font('dogicapixelbold.ttf', 20)

            space_text = font_space.render(f'Press Space', False, (255, 255, 255))
            space_rect = space_text.get_rect(topright=(1100, 745))
            self.screen.blit(space_text, space_rect)

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
        self.display_space()

        if self.step >= 5:
            self.screen.fill((0, 0, 0))
        if self.step > 6:
            end_text = self.font.render(f'The end', False, (255, 255, 255))
            end_rect = end_text.get_rect(topright=(1100, 745))
            self.screen.blit(end_text, end_rect)

            score_text = self.font.render(f'score: {self.final_score}', False, (255, 255, 255))
            score_rect = score_text.get_rect(topright=(300, 745))
            self.screen.blit(score_text, score_rect)

            pygame.time.delay(100)
            self.re_space = True

        if self.step >= 8:
            return False
        else:
            return True
