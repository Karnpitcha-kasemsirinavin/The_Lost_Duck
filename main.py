import pygame
import sys
from duck_game import Duck_Game
from scenes import Scenes, Walk_Scene, Game_over_scene, Intro, End_scene

pygame.init()
'''=============================== Setup ================================================'''
status = True
level = 1
score = 0
heart = 10
continue_game = True
restart = True
display_score = 0
round_num = 10
# check = True

run_scene = False
walking_scene_ready = False
intro_ready = True
end_scene_ready = True
con_end_scene = False

bg_x = 0
click = False
start_game = False

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

'''======================================================================================='''

def draw_text(screen,text,size,color,x,y):
    pygame.init()
    font = pygame.font.Font('dogicapixelbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

'''---------------------------------- Main menu ------------------------------------------'''

def call_main_menu():
    global click, start_game, screen, run_scene, walking_scene_ready, bg_x, round_num, continue_game, score, \
        display_score, con_end_scene

    bg_x_cloud1 = 0
    menu_music = pygame.mixer.Sound('Music\\Guitar-Gentle.mp3')
    menu_music.set_volume(0.2)


    game_bg_channel = pygame.mixer.Channel(1)
    menu_sound_channel = pygame.mixer.Channel(0)

    click_sound = pygame.mixer.Sound('Sound_effect\\clicking_sound.wav')
    click_sound.set_volume(0.3)

    game_bg_channel.play(menu_music)

    while True:

        continue_game = True
        round_num = 1
        clock = pygame.time.Clock()

        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(450, 500, 300, 100) ###left top width height
        button_2 = pygame.Rect(450, 650, 300, 100)

        if button_1.collidepoint((mx, my)):
            if click:
                menu_sound_channel.play(click_sound)
                menu_music.fadeout(30)
                menu_music.fadeout(30)
                pygame.time.delay(300)


                clock = pygame.time.Clock()


                music_name = 'Music\\level\\level1_1.mp3'
                music = pygame.mixer.Sound(music_name)

                while round_num != 0 and continue_game is not False:
                    '''Call intro scene for first time'''
                    if round_num == 10:
                        call_intro()


                    music_name = 'Music\\level\\level' + str(11-round_num) + '_' + str(11-round_num) + '.mp3'

                    music = pygame.mixer.Sound(music_name)
                    music.set_volume(0.2)

                    game_bg_channel.play(music, loops=-1)

                    continue_game, display_score = call_duck_game(game_bg_channel, music)

                    if continue_game is not False:
                        game_bg_channel.pause()
                        game_bg_channel.play(music)
                        call_scene()
                        call_walk_scene(music)
                        round_num -= 1

                    # music.fadeout(30)

                    # if pygame.mixer.music.get_busy() is True:
                    #     music.fadeout(10)

                if continue_game is not False:
                    con_end_scene = True

                while con_end_scene is not False:
                    con_end_scene = call_end_scene()

                while continue_game is False:

                    music.stop()
                    continue_game = call_game_over_scene(display_score)

                menu_music.play(loops=-1)

                clock.tick(60)
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
        screen.blit(cloud_1, (rel_bg_x_cloud1 - cloud_1.get_rect().width, 0 ))


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

    start_text = font.render(f'START', False, (255,255,255))
    start_rect = start_text.get_rect(topright= (690,530))
    screen.blit(start_text, start_rect)

    exit_text_shadow = font.render(f'EXIT', False, (33, 73, 42))
    exit_rect_shadow = exit_text_shadow.get_rect(topright=(665, 680))
    screen.blit(exit_text_shadow, exit_rect_shadow)

    exit_text = font.render(f'EXIT', False, (255,255,255))
    exit_rect = exit_text.get_rect(topright= (670,680))
    screen.blit(exit_text, exit_rect)

'''====================================== Duck game =============================================='''
def call_duck_game(game_bg_channel, music):
    global bg_x, level, screen, status, score, heart, run_scene, walking_scene_ready, screen_width, screen_height, \
        continue_game, display_score

    ENEMIESLASER = pygame.USEREVENT + 1  ###
    pygame.time.set_timer(ENEMIESLASER, 800)

    pygame.time.delay(300)

    status = True
    game = Duck_Game(level, score, heart, status, game_bg_channel, music)
    while status is True or status is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ENEMIESLASER:
                game.enemies_shoot()


        screen.fill(((0, 0, 0)))
        background_image = 'Pic\\bg\\bg' + str(game.level) + '.png'
        background = pygame.image.load(background_image)
        screen.blit(background, (0, 0))


        '''Method in class Duck_Game'''
        continue_game = game.running_game()
        status = game.check_status()

        pygame.display.flip()
        # print(continue_game)


    '''updating score and heart'''

    if continue_game != False:
        level += 1
        score = game.score
        heart = game.heart

    else:
        heart = 10
        display_score = game.score
        score = 0

        '''If want to make a replay don't set level'''

        level = 1

    return continue_game,display_score





def call_scene():

    run_scene = True
    '''Scene loop'''
    scene = Scenes(level, screen)
    while run_scene == True or run_scene == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(((0, 0, 0)))
        # background_image = 'Pic\\bg\\bg' + str(game.level) + '.png'


        scene.runnning_scene()
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


    '''Game over scene'''

    game_over_scene = Game_over_scene(screen, score)
    while game_over_scene_ready is True or game_over_scene_ready is None:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



        game_over_scene_ready = game_over_scene.update()


        # if game_over_scene_ready == False:
        #     return True

        pygame.display.flip()

def call_intro():

    intro_ready = True


    '''Intro scene'''
    intro_scene = Intro(screen)
    while intro_ready is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        intro_ready = intro_scene.running()

        pygame.display.flip()


def call_end_scene():

    end_scene_ready = True

    '''End scene'''
    end_scene = End_scene(screen)
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