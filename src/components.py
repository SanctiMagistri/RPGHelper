import pygame

from .classes import *
from .scripts import check_command, pass_func, login, register

# ===== FONTS =====
DICE_INPUT_FONT = 'fnt/newt-serif.serifbold.otf'
CHAT_INPUT_FONT = 'fnt/fff-forward.regular.ttf'

# ===== BACKGROUNDS =====
logging_screen = pygame.Surface((1600,900))
logging_screen.fill('burlywood')
logging_screen_pos = (0,0)

main_panel = pygame.Surface((350,900))
main_panel.fill((255,255,0))
main_panel_pos = (0,0)

temp_bookmarks = pygame.Surface((50,900))
temp_bookmarks.fill((255,0,255))
bookmarks_pos = (0 + main_panel.get_width(),0)

map = pygame.Surface((900,900))
map.fill((100,100,100))
map_pos = (bookmarks_pos[0] + temp_bookmarks.get_width(),0)

chat_background = pygame.Surface((300,900))
chat_background.fill('navajowhite2')

chat = pygame.Surface((300,900))
chat_pos = (map_pos[0] + map.get_width(),0)
chat.fill('white')
chat = pygame.image.load("img/chat/chat2.png")

dice_group = pygame.sprite.Group()


# ===== DICE BUTTONS =====
dice4 = DiceButtons("img/chat/dice4.png", [chat_pos[0]+75, 610], "img/chat/dice4clicked.png", 4)
dice_group.add(dice4)

dice6 = DiceButtons("img/chat/dice6.png", [chat_pos[0]+150, 610], "img/chat/dice6clicked.png", 6)
dice_group.add(dice6)

dice8 = DiceButtons("img/chat/dice8.png", [chat_pos[0]+225, 610], "img/chat/dice8clicked.png", 8)
dice_group.add(dice8)

dice10 = DiceButtons("img/chat/dice10.png", [chat_pos[0]+75, 690], "img/chat/dice10clicked.png", 10)
dice_group.add(dice10)

dice12 = DiceButtons("img/chat/dice12.png", [chat_pos[0]+150, 690], "img/chat/dice12clicked.png", 12)
dice_group.add(dice12)

dice20 = DiceButtons("img/chat/dice20.png", [chat_pos[0]+225, 690], "img/chat/dice20clicked.png", 20)
dice_group.add(dice20)

dice100 = DiceButtons("img/chat/dice100.png", [chat_pos[0]+150, 770], "img/chat/dice100clicked.png", 100)
dice_group.add(dice100)


# ===== INPUT BOXES =====
login_box = LoginBox([600, 300], [300, 50] , pass_func, DICE_INPUT_FONT, 30)
password_box = LoginBox([600, 400], [300, 50] , pass_func, DICE_INPUT_FONT, 30)
login_panel_boxes = [login_box, password_box]

commandbox = InputBox([chat_pos[0]+23,837], [254,45], check_command, DICE_INPUT_FONT, 30)
chat_box = InputBox([chat_pos[0]+23, 526], [255,31], pass_func, CHAT_INPUT_FONT, 12)
input_boxes = [commandbox, chat_box]

# ===== BUTTONS =====
LoginButton = LoginPanelButton("Zaloguj", (600, 500), (125, 50), DICE_INPUT_FONT, 20, 'chartreuse3', login)
RegisterButton = LoginPanelButton("Zarejestruj", (775,500),(125,50), DICE_INPUT_FONT, 20, 'darkgoldenrod3', register)
login_panel_buttons = [LoginButton, RegisterButton]

