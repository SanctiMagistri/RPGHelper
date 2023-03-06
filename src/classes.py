import pygame
from src.scripts import throw_dice

pygame.font.init()

FONT = pygame.font.Font(None, 32)
COLOR_INACTIVE = pygame.Color('bisque')
COLOR_ACTIVE = pygame.Color('bisque3')
class DiceButtons(pygame.sprite.Sprite):
    def __init__(self, pic_path, position, clicked_pic_path, dice):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.path = pic_path
        self.path_clicked = clicked_pic_path
        self.dice = dice

    def update(self, is_clicked):
        if is_clicked == True:
            self.image = pygame.image.load(self.path_clicked)
            throw = throw_dice([], 1, self.dice)
            print(throw)
        else:
            self.image = pygame.image.load(self.path)


class InputBox:
    def __init__(self, position, size, text = ''):
        self.rect = pygame.Rect(position, size)
        self.color = COLOR_INACTIVE
        self.text = text
        self.text_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text) # MAKE HERE HANDLE COMMAND

                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)