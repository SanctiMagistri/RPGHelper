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

    chat_buttons_group.update()
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
                if dice4.rect.collidepoint(mouse_cords):
                    dice4.on_click()
                if dice6.rect.collidepoint(mouse_cords):
                    dice6.on_click()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_cords = pygame.mouse.get_pos()
                if dice4.rect.collidepoint(mouse_cords):
                    dice4.on_release()
                if dice6.rect.collidepoint(mouse_cords):
                    dice6.on_release()

            redraw_window()

main()