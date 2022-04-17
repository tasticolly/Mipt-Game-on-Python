import pygame
from configuration import game_font, sound_select


class Menu:
    def __init__(self, x, y, option_y_padding):
        self.option_serfaces = []
        self.callbacks = []
        self.current_option_index = -1
        self.option_y_padding = option_y_padding
        self.x = x
        self.y = y

    def append_option(self, option, callback):
        self.option_serfaces.append(game_font.render(option, False, "black"))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_serfaces) - 1))
        sound_select.play()

    def select(self):
        sound_select.play()
        self.callbacks[self.current_option_index]()

    def mouse_in_block(self, option_rect, i):
        mouse_position = pygame.mouse.get_pos()
        return (self.x < mouse_position[0] < self.x + option_rect.width) and (
                self.y + i * self.option_y_padding < mouse_position[
            1] < self.y + i * self.option_y_padding + option_rect.height)

    def draw(self, surf):

        for i, option in enumerate(self.option_serfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (self.x, self.y + i * self.option_y_padding)

            if self.mouse_in_block(option_rect, i):
                if self.current_option_index != i:
                    sound_select.play()
                self.current_option_index = i

            if i == self.current_option_index:
                pygame.draw.rect(surf, (27, 103, 213), option_rect)

            surf.blit(option, option_rect)
