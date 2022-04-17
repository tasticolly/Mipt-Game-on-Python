import pygame, random
from methods import gameRestart
from Sprites.BaseBlock import Block
from configuration import screen_height, screen_width, screen, sound_destroy

enemies_color = (22, 8, 159)


class Enemy(Block):
    def __init__(self, x_pos, y_pos, group, path=None, width=60, height=60):
        super().__init__(x_pos, y_pos, path=path, width=width, height=height)
        self.speed_x = 0
        self.speed_y = 0
        self.start_speed_x = 0
        self.start_speed_y = 0
        self.add(group)

    speed_zone = 12

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1
        self.launch_enemy()

        self.increase_speed_with_time()

        if self.rect.colliderect(gameRestart.player):
            sound_destroy.play()
            gameRestart.restart()

        self.draw()

    def launch_enemy(self):
        if Block.game_active and Block.count_enemies < gameRestart.num_of_enemies:
            Block.count_enemies += 1
            self.speed_x = random.randint(-Enemy.speed_zone, Enemy.speed_zone)
            self.speed_y = random.randint(-Enemy.speed_zone, Enemy.speed_zone)
            self.start_speed_x = abs(self.speed_x)
            self.start_speed_y = abs(self.speed_y)

            Block.start_time = pygame.time.get_ticks()

    def increase_speed_with_time(self):
        if Block.start_time:
            self.change_speed(Enemy.calculate_speed_coefficient())

    def change_speed(self, value):
        self.speed_x = self.start_speed_x * value * self.sign(self.speed_x)
        self.speed_y = self.start_speed_y * value * self.sign(self.speed_y)

    def draw(self):
        pygame.draw.rect(screen, enemies_color, self.rect)

    @staticmethod
    def calculate_speed_coefficient():
        return 1 + (pygame.time.get_ticks() - Block.start_time) / 20000

    @staticmethod
    def sign(value):
        if value > 0:
            return 1
        elif value == 0:
            return 0
        else:
            return -1
