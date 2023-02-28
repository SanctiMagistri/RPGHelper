import pygame
from src.components import *

width = 1600
height = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("RPGHelper")



def redraw_window():
    window.fill((255,255,255))
    window.blit(main_panel, main_panel_pos)
    window.blit(temp_bookmarks, bookmarks_pos)
    window.blit(map, map_pos)
    window.blit(chat, chat_pos)

    chat_buttons_group.draw(window)

    pygame.display.update()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_cords = pygame.mouse.get_pos()
                for dice in chat_buttons_group:
                    if dice.rect.collidepoint(mouse_cords):
                        dice.update(is_clicked=True)

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_cords = pygame.mouse.get_pos()
                for dice in chat_buttons_group:
                    if dice.rect.collidepoint(mouse_cords):
                        dice.update(is_clicked=False)

            redraw_window()

main()