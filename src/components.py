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

dice4 = DiceButtons("img/chat/dice4.png", [chat_pos[0]+60, 605], "img/chat/dice4clicked.png")
chat_buttons_group.add(dice4)

dice6 = DiceButtons("img/chat/dice6.png", [chat_pos[0]+125, 605], "img/chat/dice6clicked.png")
chat_buttons_group.add(dice6)

dice8 = DiceButtons("img/chat/dice8.png", [chat_pos[0]+180, 605], "img/chat/dice8clicked.png")
chat_buttons_group.add(dice8)

dice10 = DiceButtons("img/chat/dice10.png", [chat_pos[0]+235, 605], "img/chat/dice10clicked.png")
chat_buttons_group.add(dice10)

dice12 = DiceButtons("img/chat/dice12.png", [chat_pos[0]+90, 670], "img/chat/dice12clicked.png")
chat_buttons_group.add(dice12)

dice20 = DiceButtons("img/chat/dice20.png", [chat_pos[0]+150, 670], "img/chat/dice20clicked.png")
chat_buttons_group.add(dice20)

dice100 = DiceButtons("img/chat/dice100.png", [chat_pos[0]+200, 670], "img/chat/dice100clicked.png")
chat_buttons_group.add(dice100)
