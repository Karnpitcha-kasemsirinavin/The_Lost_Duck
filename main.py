import pygame
import sys
from duck_game import Duck_Game
from scenes import Scenes, Walk_Scene, Game_over_scene, Intro, End_scene

pygame.init()

'''=============================== Setup ================================================'''

'''Setup for window screen'''
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

'''Window icon'''
game_icon = pygame.image.load('Pic\\Player\\Player.png')
pygame.display.set_icon(game_icon)

'''set window name as game name'''
pygame.display.set_caption('The Lost Duck')

'''For checking each level of game'''
status = True

'''level in game'''
level = 1

'''start score'''
score = 0

'''start heart '''
heart = 10

'''For checking if Game Over or not'''
continue_game = True

'''start display score, will be update with the current score and pass to Game Over or end scene'''
display_score = 0

'''Number of round to play'''
round_num = 10

'''Trigger for cut scenes in each level'''
run_scene = False

'''Trigger for walking scene btw each level'''
walking_scene_ready = False

'''Trigger for intro scene'''
intro_ready = True

'''Trigger for end scene'''
end_scene_ready = True

'''Trigger for end scene loop'''
con_end_scene = False

'''Trigger for clicking the button'''
click = False

'''Trigger for game'''
start_game = False

'''---------------------------------- Main menu ------------------------------------------'''


def call_main_menu():
    global click, start_game, screen, run_scene, walking_scene_ready, round_num, continue_game, score, \
        display_score, con_end_scene, level, heart

    '''Window icon'''
    game_icon = pygame.image.load('Pic\\Player\\Player.png')
    pygame.display.set_icon(game_icon)

    '''Cloud picture in menu to calculate and check the position'''
    bg_x_cloud1 = 0

    '''Setup menu bg music'''
    menu_music = pygame.mixer.Sound('Music\\Guitar-Gentle.mp3')
    menu_music.set_volume(0.1)

    '''Create sound channel 1'''
    game_bg_channel = pygame.mixer.Channel(1)

    '''Create sound channel 0 for menu bg music'''
    menu_sound_channel = pygame.mixer.Channel(0)

    '''Play menu bg music in channel 0'''
    game_bg_channel.play(menu_music, loops=-1)

    '''Setup click sound effect'''
    click_sound = pygame.mixer.Sound('Sound_effect\\clicking_sound.wav')
    click_sound.set_volume(0.2)

    while True:

        continue_game = True
        round_num = 10
        clock = pygame.time.Clock()

        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(450, 500, 300, 100)  # left top width height
        button_2 = pygame.Rect(450, 650, 300, 100)

        if button_1.collidepoint((mx, my)):
            if click:
                menu_sound_channel.play(click_sound)
                menu_music.fadeout(30)
                menu_music.fadeout(30)
                pygame.time.delay(300)

                clock = pygame.time.Clock()

                '''Play game loop for ten rounds'''
                while round_num != 0 and continue_game is not False:
                    '''Call intro scene for first round'''
                    if round_num == 10:
                        call_intro(game_bg_channel)

                    '''Generate music for each level'''
                    music_name = 'Music\\level\\level' + str(11 - round_num) + '_' + str(11 - round_num) + '.mp3'
                    music = pygame.mixer.Sound(music_name)
                    music.set_volume(0.1)
                    game_bg_channel.play(music, loops=-1)

                    '''call game for each round and return value to check if it is Game Over or not, and return
                     score to display in Game Over and End scenes.'''
                    continue_game, display_score = call_duck_game(game_bg_channel, music)

                    '''If not Game Over in each level, play cut scene then minus round by one'''
                    if continue_game is not False:
                        game_bg_channel.unpause()
                        call_scene()
                        call_walk_scene(music)
                        round_num -= 1

                '''Trigger end scene'''
                if continue_game is not False:
                    con_end_scene = True

                '''If not Game Over play end scene'''
                while con_end_scene is not False:
                    con_end_scene = call_end_scene(display_score)

                '''If Game Over lead to end scene'''
                while continue_game is False:
                    game_bg_channel.stop()
                    continue_game = call_game_over_scene(display_score)

                '''Back to main menu continue playing menu music'''
                menu_music.play(loops=-1)

                clock.tick(60)

                if round_num == 0:
                    level = 1
                    heart = 10
                    score = 0

        if button_2.collidepoint((mx, my)):
            if click:
                menu_sound_channel.play(click_sound)
                menu_music.fadeout(30)
                pygame.time.delay(300)
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        '''Pic at button pos'''

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button >= 1:
                    click = True

        background = pygame.image.load('Pic\\bg\\bg_menu.png')
        screen.blit(background, (0, 0))

        cloud_1 = pygame.image.load('Pic\\bg\\bg_menu_cloud_1.png')

        rel_bg_x_cloud1 = bg_x_cloud1 % cloud_1.get_rect().width
        screen.blit(cloud_1, (rel_bg_x_cloud1 - cloud_1.get_rect().width, 0))

        if rel_bg_x_cloud1 < screen_width:
            screen.blit(cloud_1, (rel_bg_x_cloud1, 0))

        bg_x_cloud1 -= 3

        game_name = pygame.image.load('Pic\\menu_icon.png')
        screen.blit(game_name, (300, 50))
        start_button = pygame.image.load('Pic\\start_button.png')
        screen.blit(start_button, (450, 500))
        exit_button = pygame.image.load('Pic\\exit_button.png')
        screen.blit(exit_button, (450, 650))

        menu_text()
        pygame.display.update()
        clock.tick(60)


'''-----------------------------------------------------------------------------------------------'''


def menu_text():
    font = pygame.font.Font('dogicapixel.ttf', 40)
    start_text_shadow = font.render(f'START', False, (33, 73, 42))
    start_rect_shadow = start_text_shadow.get_rect(topright=(685, 530))
    screen.blit(start_text_shadow, start_rect_shadow)

    start_text = font.render(f'START', False, (255, 255, 255))
    start_rect = start_text.get_rect(topright=(690, 530))
    screen.blit(start_text, start_rect)

    exit_text_shadow = font.render(f'EXIT', False, (33, 73, 42))
    exit_rect_shadow = exit_text_shadow.get_rect(topright=(665, 680))
    screen.blit(exit_text_shadow, exit_rect_shadow)

    exit_text = font.render(f'EXIT', False, (255, 255, 255))
    exit_rect = exit_text.get_rect(topright=(670, 680))
    screen.blit(exit_text, exit_rect)


'''====================================== Duck game =============================================='''


def call_duck_game(game_bg_channel, music):
    global level, screen, status, score, heart, run_scene, walking_scene_ready, screen_width, screen_height, \
        continue_game, display_score

    ENEMIESLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMIESLASER, 800)

    pygame.time.delay(30)

    status = True
    game = Duck_Game(level, score, heart, status, game_bg_channel, music)
    while status is True or status is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ENEMIESLASER:
                game.enemies_shoot()

        screen.fill((0, 0, 0))
        background_image = 'Pic\\bg\\bg' + str(game.level) + '.png'
        background = pygame.image.load(background_image)
        screen.blit(background, (0, 0))

        '''Method in class Duck_Game'''
        continue_game = game.running_game()
        status = game.check_status()

        pygame.display.flip()

    '''updating score and heart'''

    if continue_game is not False:
        level += 1
        score = game.score
        heart = game.heart
        display_score = game.score

    else:
        heart = 10
        display_score = game.score
        score = 0
        level = 1

    return continue_game, display_score


def call_scene():
    run_scene = True

    '''Scene loop'''
    scene = Scenes(level, screen)
    while run_scene is True or run_scene is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        scene.running_scene()
        run_scene = scene.check_con()

        pygame.display.flip()


def call_walk_scene(music):
    walking_scene_ready = True
    '''Walking scene'''
    walk_scene = Walk_Scene(level, screen, music)
    while walking_scene_ready is True or walking_scene_ready is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        walk_scene.running_scene()
        walking_scene_ready = walk_scene.check_con()

        pygame.display.flip()


def call_game_over_scene(score):
    global screen
    game_over_scene_ready = True

    '''Game Over sound'''
    game_over_sound = pygame.mixer.Sound('Sound_effect\\game_over.wav')
    game_over_sound.set_volume(0.1)

    game_over_sound.play()

    '''Game over scene'''

    game_over_scene = Game_over_scene(screen, score)
    while game_over_scene_ready is True or game_over_scene_ready is None:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over_sound.stop()
                    return True

        game_over_scene_ready = game_over_scene.update()

        pygame.display.flip()


def call_intro(game_bg_channel):
    intro_ready = True

    '''Intro scene'''
    intro_scene = Intro(screen, game_bg_channel)
    while intro_ready is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        intro_ready = intro_scene.running()

        pygame.display.flip()


def call_end_scene(display_score):
    end_scene_ready = True

    '''End scene'''
    end_scene = End_scene(screen, display_score)
    while end_scene_ready is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        end_scene_ready = end_scene.running()

        pygame.display.flip()

    return end_scene_ready


##################################################################################################################
if __name__ == '__main__':
    call_main_menu()
