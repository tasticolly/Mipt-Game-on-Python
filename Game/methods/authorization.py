import pygame
import main
from configuration import game_font, screen, stop_program, screen_height, screen_width, data,sound_select
from time import sleep

# Personal Data
login = ""
best_result = 0

big_login_message = "Nickname is too long"
empty_login_message = "Nickname is empty"


def authorization():
    global login, best_result
    login = ""
    message = empty_login_message
    backSpaceActive = False
    input_rect = pygame.Rect(screen_height / 2 - 210, screen_width / 2 - 20, 420, 40)
    passive_color = 'lightblue3'
    wrong_color = (255, 51, 0)
    color = passive_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_program()

            elif event.type == pygame.KEYDOWN:
                color = passive_color
                if event.key == pygame.K_BACKSPACE:
                    backSpaceActive = True
                    color = passive_color
                elif event.key == pygame.K_RETURN:
                    if (login == ""):
                        color = wrong_color
                        message = empty_login_message
                    else:
                        if (not data.find(login)):
                            data.save(login, 0)
                        best_result = data.get(login)
                        sound_select.play()
                        main.main()
                elif event.key != pygame.K_ESCAPE:
                    login += event.unicode
                    if len(login) > 20:
                        color = wrong_color
                        message = big_login_message
                        login = login[:-1]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    backSpaceActive = False
        if backSpaceActive:
            sleep(0.11)
            login = login[:-1]
        screen.fill((255, 255, 255))

        login_surface = game_font.render(login, True, "black")
        init_surface = game_font.render("Input your nickname", True, "blue")

        if color == wrong_color:
            wrong_surface = game_font.render(message, True, "red")
            screen.blit(wrong_surface, (input_rect.x + 45, input_rect.y + 50))

        input_rect.width = max(input_rect.width, login_surface.get_width() + 5)
        pygame.draw.rect(screen, color, input_rect)

        screen.blit(init_surface, (input_rect.x + 45, input_rect.y - 40))
        screen.blit(login_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()


# if __name__ == 'login':
authorization()
