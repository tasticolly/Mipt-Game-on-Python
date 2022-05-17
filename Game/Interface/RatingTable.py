import pygame
from configuration import game_font, screen, stop_program, screen_height, screen_width, data, sound_select
from methods import authorization

header_nick = "Nickname:"
header_result = "Best result:"
header_top = "TOP 10 RESULTS"
text_result = "Your best result is: "
text_position = "Position in rating: "

top_f = pygame.font.Font("freesansbold.ttf", 48)
login_f = pygame.font.Font("freesansbold.ttf", 42)
name_f = pygame.font.Font("Fonts/DejaVuSansMono.ttf", 32)


class RatingTable:
    def __init__(self, dict_shellve, x, y, option_y_padding):
        dictionary = {k: dict_shellve[k] for k in dict_shellve.keys()}
        sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
        self.table = {k: v for k, v in sorted_tuples}
        self.option_y_padding = option_y_padding
        self.x = x
        self.y = y
        self.position = list(self.table.keys()).index(authorization.login) + 1

    def get_position(self):
        return list(self.table.keys()).index(authorization.login) + 1

    def draw(self, surf):

        surf.blit(game_font.render(header_nick, True, "blue"), (self.x - 25, self.y))
        surf.blit(game_font.render(header_result, True, "blue"), (self.x + 320, self.y))
        for i, login in enumerate(self.table.keys()):
            if (i == 10):
                break
            position_font = game_font.render(str(i + 1) + '.', True, "black")
            login_font = name_f.render(login, True, "black")
            result_font = game_font.render(str(self.table[login]), True, "black")
            rect_pos = position_font.get_rect()
            rect_pos.topright = (self.x - 110, self.y + (i + 1) * self.option_y_padding)
            surf.blit(login_font, (self.x - 100, self.y + (i + 1) * self.option_y_padding - 5))
            surf.blit(result_font, (self.x + 350, self.y + (i + 1) * self.option_y_padding))
            surf.blit(position_font, rect_pos)


def runTable():
    table = RatingTable(data.file, 200, 70, 40)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_program()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sound_select.play()
                    return 0
        screen.fill((255, 255, 255))
        table.draw(screen)
        login_font = login_f.render(authorization.login, True, (255, 102, 204))
        login_rect = login_font.get_rect()
        login_rect.center = (screen_width / 2, 3 * screen_height / 4)

        screen.blit(top_f.render(header_top, True, "black"), (screen_width / 4, 10))
        screen.blit(login_font, login_rect)
        screen.blit(game_font.render(text_result + str(authorization.best_result), True, "black"),
                    (220, 3 * screen_height / 4 + 50))
        screen.blit(game_font.render(text_position + str(table.position), True, "black"),
                    (220, 3 * screen_height / 4 + 100))

        pygame.display.flip()
