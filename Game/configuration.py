import random

import pygame
import sys
from statistic import Save


def stop_program():
    pygame.quit()
    sys.exit()


def get_path():
    return f"Images/{random.randint(1, 3)}.png"


pygame.init()

# main window
FPS = 60  # frames per second to update the screen
screen_width = 800  # width of the program's window, in pixels
screen_height = 800  # height in pixels
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Square")
clock = pygame.time.Clock()

data = Save.Save()
# colors
bg_color = (255, 255, 255)

# Text Variables
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Music
pygame.mixer.music.load(f'Sounds/MenuMusic/{random.randint(1, 3)}.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

# Sounds
sound_destroy = pygame.mixer.Sound("Sounds/c1eba7e3b886a1f.mp3")
sound_destroy.set_volume(0.3)
sound_select = pygame.mixer.Sound("Sounds/select1.mp3")
sound_select.set_volume(2)

# Images
name_image = get_path()
