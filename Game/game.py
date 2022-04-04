import pygame
import sys
import random

def stop_program():
    pygame.quit()
    sys.exit()

pygame.init()
clock = pygame.time.Clock()

# main window
FPS = 60  # frames per second to update the screen
screen_width = 800  # width of the program's window, in pixels
screen_height = 800  # height in pixels
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Square")

# colors
bg_color = (255, 255, 255)
player_color = (229, 28, 0)
enemies_color = (22, 8, 159)


# Text Variables
game_font = pygame.font.Font("freesansbold.ttf", 32)

class Menu:
    def __init__(self):
        self.option_serfaces = []
        self.callbacks = []
        self.current_option_index = 0

    def append_option(self, option, callback):
        self.option_serfaces.append(game_font.render(option,False,"black"))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0,min(self.current_option_index + direction,len(self.option_serfaces)- 1))

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i,option in enumerate(self.option_serfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                pygame.draw.rect(surf, (27, 103, 213),option_rect)
            surf.blit(option,option_rect)




def run():
    class Block(pygame.sprite.Sprite):
        def __init__(self, x_pos, y_pos, path=None, width=60, height=60):
            super().__init__()
            if path is None:
                self.rect = pygame.Rect(x_pos - width / 2, y_pos - height / 2, width, height)
            else:
                self.image = pygame.image.load(path)
                self.rect = self.image.get_rect(center=(x_pos, y_pos))

        start_time = None
        end_time = None
        is_left_button_pressed = False
        game_active = False
        count_enemies = 0
        num_of_increase_speed = 1


    class Player(Block):
        def __init__(self, x_pos, y_pos, group, path=None, width=60, height=60):
            super().__init__(x_pos, y_pos, path=path, width=width, height=height)
            self.add(group)

        def update(self, sp):
            self.in_screen()
            if not (sp is None) and sp[0] <= self.rect.right and sp[0] >= self.rect.left and sp[1] <= self.rect.bottom and \
                    sp[
                        1] >= self.rect.top:
                Block.is_left_button_pressed = True
            self.timer()
            self.draw()

        def in_screen(self):
            if self.rect.top <= 0 or self.rect.bottom >= screen_height or self.rect.left <= 0 or self.rect.right >= screen_width:
                restart()

        def timer(self):
            if Block.start_time:
                timer_text = game_font.render(f"{(pygame.time.get_ticks() - Block.start_time) / 1000}", False, "black")
                if not Block.game_active:
                    timer_text = game_font.render(f"{(Block.end_time - Block.start_time) / 1000}", False, "black")
                screen.blit(timer_text, (screen_width / 2 - 40, 10))

        def draw(self):
            pygame.draw.rect(screen, player_color, self.rect)


    class Enemy(Block):
        def __init__(self, x_pos, y_pos, group, path=None, width=60, height=60):
            super().__init__(x_pos, y_pos, path=path, width=width, height=height)
            self.speed_x = 0
            self.speed_y = 0
            self.add(group)

        def update(self):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                self.speed_y *= -1
            if self.rect.left <= 0 or self.rect.right >= screen_width:
                self.speed_x *= -1

            self.launch_enemy()

            self.increase_speed_with_time()

            if self.rect.colliderect(player):
                restart()

            self.draw()

        def launch_enemy(self):
            if Block.game_active and Block.count_enemies < num_of_enemies:
                Block.count_enemies += 1
                self.speed_x = random.randint(-17, 17)
                self.speed_y = random.randint(-17, 17)
                Block.start_time = pygame.time.get_ticks()

        def increase_speed_with_time(self):
            if Block.start_time and (pygame.time.get_ticks() - Block.start_time >= 3000 * Block.num_of_increase_speed):
                self.change_speed(1.2)
                Block.num_of_increase_speed += 1

        def change_speed(self, value):
            self.speed_x *= value
            self.speed_y *= value

        def draw(self):
            pygame.draw.rect(screen, enemies_color, self.rect)


    # Game objects
    num_of_enemies = 4
    gr_pl = pygame.sprite.Group()
    gr_en = pygame.sprite.Group()
    player = Player(screen_width / 2, screen_height / 2, gr_pl)
    enemies = list()
    # Game Objects
    def restart():
        nonlocal enemies, gr_pl, gr_en
        enemies = list()
        gr_en = pygame.sprite.Group()
        Block.num_of_increase_speed = 1
        Block.game_active = False
        Block.is_left_button_pressed = False
        Block.count_enemies = 0
        for i in range(num_of_enemies // 2):
            for j in range(num_of_enemies // 2):
                enemies.append(Enemy(screen_width * (1 + 2 * i) / 4, screen_height * (1 + 2 * j) / 4, gr_en,
                                     width=random.randint(20, 120),
                                     height=random.randint(20, 120)))
        player.rect.topleft = (screen_width / 2 - 30, screen_height / 2 - 30)
        Block.end_time = pygame.time.get_ticks()


    restart()
    while True:
        sp = None
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sp = event.pos
                if not Block.game_active:
                    Block.game_active = True
                    Block.start_time = pygame.time.get_ticks()
            elif event.type == pygame.MOUSEMOTION:
                if Block.is_left_button_pressed:
                    player.rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                Block.is_left_button_pressed = False
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0

        # Visuals
        screen.fill(bg_color)
        gr_pl.update(sp)
        gr_en.update()
        # Updating window

        pygame.display.flip()
        clock.tick(FPS)

menu = Menu()
menu.append_option("Play", run)
menu.append_option("Quit", stop_program)
menu.draw(screen, 100, 100, 75)

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            stop_program()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                menu.switch(-1)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                menu.switch(1)
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                menu.select()

    screen.fill(bg_color)
    menu.draw(screen,100,100,75)
    pygame.display.flip()
    clock.tick(FPS)
