import pygame

width = 1280
height = 786
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("RPGHelper")



def redrawWindow():
    window.fill((255,255,255))
    pygame.display.update()


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            redrawWindow()

main()