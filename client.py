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

def main():
    clock = pygame.time.Clock()
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