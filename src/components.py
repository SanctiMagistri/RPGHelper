import pygame
from .classes import *

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

chat = pygame.image.load("img/chat/chat_2.png")

# chat_input = ChatInput("img/chat/chat_input_2.png", [chat_pos[0]+150, 550])
# #TEMPORARY
# chat_buttons_group.add(chat_input)

dice4 = DiceButtons("img/chat/dice4.png", [chat_pos[0]+55, 605], "img/chat/dice4clicked.png")
chat_buttons_group.add(dice4)

dice6 = DiceButtons("img/chat/dice6.png", [chat_pos[0]+110, 605], "img/chat/dice6clicked.png")
chat_buttons_group.add(dice6)