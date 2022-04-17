import pygame

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
