import pygame

from src.components import *

pygame.init()
pygame.font.init()

width = 1600
height = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("RPGHelper")

# ===== FONTS =====
CHATBOX_FONT = pygame.font.Font('fnt/newt-serif.serifbold.otf', 30)

def redraw_window():
    window.fill((255,255,255))
    window.blit(main_panel, main_panel_pos)
    window.blit(temp_bookmarks, bookmarks_pos)
    window.blit(map, map_pos)
    window.blit(chat_background, chat_pos)
    window.blit(chat, chat_pos)

    dice_group.draw(window)

    for box in input_boxes:
        box.draw(window)

    pygame.display.update()

def login():
    logged_in = False
    log_state = False
    while logged_in is False:
        window.blit(logging_screen, logging_screen_pos)

        for logbox in login_panel_boxes:
            logbox.draw(logging_screen)

        for logbuttons in login_panel_buttons:
            logbuttons.draw(logging_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for logbox in input_boxes:
                logbox.handle_event(event)

            for logbuttons in login_panel_buttons:
                log_state_temp = logbuttons.handle_event(event, ("login","passwd"))
                if log_state_temp is True:
                    log_state = log_state_temp

            if event.type == pygame.MOUSEBUTTONUP:
                logged_in = log_state

        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    login()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_cords = pygame.mouse.get_pos()
                for dice in dice_group:
                    if dice.rect.collidepoint(mouse_cords):
                        dice.update(is_clicked=True)

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_cords = pygame.mouse.get_pos()
                for dice in dice_group:
                    if dice.rect.collidepoint(mouse_cords):
                        dice.update(is_clicked=False)

            for box in input_boxes:
                box.handle_event(event)

        redraw_window()
        clock.tick(60)

main()