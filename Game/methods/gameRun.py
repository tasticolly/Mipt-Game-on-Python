import pygame
import random
from methods import gameRestart
from configuration import screen, bg_color, FPS, clock, stop_program,sound_select
from Sprites.BaseBlock import Block


def run():
    gameRestart.restart()
    while True:
        sp = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_program()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sp = event.pos
                if not Block.game_active and gameRestart.player.mouse_on_player(sp):
                    Block.game_active = True
                    Block.start_time = pygame.time.get_ticks()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(f'Sounds/GameMusic/{random.randint(1, 8)}.mp3')
                    pygame.mixer.music.play(-1)
            elif event.type == pygame.MOUSEMOTION:
                if Block.is_left_button_pressed:
                    gameRestart.player.rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Block.is_left_button_pressed = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Block.start_time = None
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(f'Sounds/MenuMusic/{random.randint(1, 3)}.mp3')
                    pygame.mixer.music.play(-1)
                    sound_select.play()
                    return 0

        # Visuals
        screen.fill(bg_color)
        gameRestart.gr_pl.update(sp)
        gameRestart.gr_en.update()
        # Updating window

        pygame.display.flip()
        clock.tick(FPS)
