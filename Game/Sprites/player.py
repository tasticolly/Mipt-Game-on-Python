import pygame
from Sprites.BaseBlock import Block
from configuration import screen_height, screen_width, screen, game_font, data,sound_destroy,name_image
from methods import gameRestart, authorization

player_color = (229, 28, 0)


class Player(Block):
    def __init__(self, x_pos, y_pos, group, path=None, width=60, height=60):
        super().__init__(x_pos, y_pos, path=path, width=width, height=height)
        self.add(group)

    def update(self, sp):
        self.in_screen()
        if self.mouse_on_player(sp):
            Block.is_left_button_pressed = True
        self.timer()
        self.draw()

    def mouse_on_player(self, sp):
        return not (sp is None) and sp[0] <= self.rect.right and sp[0] >= self.rect.left and sp[
            1] <= self.rect.bottom and sp[1] >= self.rect.top

    def in_screen(self):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height or self.rect.left <= 0 or self.rect.right >= screen_width:
            sound_destroy.play()
            gameRestart.restart()

    def timer(self):
        if Block.start_time:
            timer_text = game_font.render(f"{(pygame.time.get_ticks() - Block.start_time) / 1000}", False, "black")
            if not Block.game_active:
                timer_text = game_font.render(f"{(Block.end_time - Block.start_time) / 1000}", False, "black")
                if authorization.best_result < (Block.end_time - Block.start_time) / 1000:
                    authorization.best_result = (Block.end_time - Block.start_time) / 1000
                    data.save(authorization.login, authorization.best_result)
            screen.blit(timer_text, (screen_width / 2 - 40, 10))

    def draw(self):
        if name_image is None:
            pygame.draw.rect(screen, player_color, self.rect)
        else:
            screen.blit(self.image,self.rect)