import pygame
from src.classes import *

width = 1600
height = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("RPGHelper")

main_panel = pygame.Surface((350,900))
main_panel.fill((255,255,0))
main_panel_pos = (0,0)

temp_bookmarks = pygame.Surface((50,900))
temp_bookmarks.fill((255,0,255))
bookmarks_pos = (0 + main_panel.get_width(),0)

map = pygame.Surface((900,900))
map.fill((100,100,100))
map_pos = (bookmarks_pos[0] + temp_bookmarks.get_width(),0)

chat = pygame.Surface((300,900))
chat.fill((50,150,200))
chat_pos = (map_pos[0] + map.get_width(),0)


chat_buttons_group = pygame.sprite.Group()

chat = pygame.image.load("img/chat/chat.png")
dice4 = MenuButtons("img/chat/dice_d4_v4.png", [chat_pos[0]+55, 700])
chat_buttons_group.add(dice4)

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
            redraw_window()

main()