from Sprites.BaseBlock import Block
import Sprites.player as plr, Sprites.enemy as enemy, random, pygame
from configuration import screen_width, screen_height, get_path

num_of_enemies = 4
gr_pl = pygame.sprite.Group()
gr_en = pygame.sprite.Group()
player = plr.Player(screen_width / 2, screen_height / 2, gr_pl, path=get_path())
enemies = list()


# current_result = 0

def restart():
    global enemies, gr_en, player, gr_pl
    pygame.mixer.music.unload()
    enemies = list()
    gr_en = pygame.sprite.Group()
    gr_pl = pygame.sprite.Group()
    Block.num_of_increase_speed = 1
    Block.game_active = False
    Block.is_left_button_pressed = False
    Block.count_enemies = 0
    for i in range(num_of_enemies // 2):
        for j in range(num_of_enemies // 2):
            enemies.append(enemy.Enemy(screen_width * (1 + 2 * i) / 4, screen_height * (1 + 2 * j) / 4, gr_en,
                                       width=random.randint(20, 120),
                                       height=random.randint(20, 120)))
    # player.rect.topleft = (screen_width / 2 - 30, screen_height / 2 - 30)
    player = plr.Player(screen_width / 2, screen_height / 2, gr_pl, path=get_path())
    Block.end_time = pygame.time.get_ticks()
