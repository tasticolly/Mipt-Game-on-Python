import pygame
from methods import authorization
from Interface.gameMenu import Menu
from configuration import stop_program, screen, bg_color
from methods.gameRun import run
from Interface import RatingTable


def main():
    menu = Menu(100, 100, 75)
    menu.append_option("Play", run)
    menu.append_option("Rating Table", RatingTable.runTable)
    menu.append_option("Change User", authorization.authorization)
    menu.append_option("Quit", stop_program)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_program()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    menu.switch(-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    menu.switch(1)
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    menu.select()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu.mouse_in_block(menu.option_serfaces[menu.current_option_index].get_rect(),
                                       menu.current_option_index):
                    menu.select()

        screen.fill(bg_color)
        menu.draw(screen)
        pygame.display.flip()
