import pygame

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



def redrawWindow():
    window.fill((255,255,255))
    window.blit(main_panel, main_panel_pos)
    window.blit(temp_bookmarks, bookmarks_pos)
    window.blit(map, map_pos)
    window.blit(chat, chat_pos)
    pygame.display.update()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            redrawWindow()

main()