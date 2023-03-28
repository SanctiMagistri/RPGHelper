import pygame
from src.scripts import throw_dice

pygame.font.init()




class Button:
    def __init__(self, text, pos, size, font, font_size, bg, func):
        self.position = pos
        self.size = size
        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, True, 'black')
        self.background = bg
        self.func = func
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.background)
        self.surface.blit(self.text, (0,0))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.text_center = (self.position[0]+((self.size[0] - self.text.get_width())/2),
                            self.position[1]+((self.size[1] - self.text.get_height())/2))
    def draw(self, screen):
        screen.blit(self.surface, self.position)
        pygame.draw.rect(screen, self.background, self.rect)
        screen.blit(self.text, self.text_center)

class LoginPanelButton(Button):
    def __init__(self, text, pos, size, font, font_size, bg, func):
        super(LoginPanelButton, self).__init__( text, pos, size, font, font_size, bg, func)
    def handle_event(self, event, data):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.func(data):
                    return True
                else: return False
            else: return False
        else: return False


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
    def __init__(self, position, size, color_active, color_inactive, txt_func, font, font_size, text = ''):
        self.rect = pygame.Rect(position, size)
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.text_surface = self.font.render(text, True, self.color)
        self.active = False
        self.txt_func = txt_func

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    print(self.txt_func(self.text)) #===============PRINT======================
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = self.font.render(self.text, True, 'black')

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class LoginBox(InputBox):
    def __init__(self, position, size, color_active, color_inactive, txt_func, font, font_size, text = ''):
        super(LoginBox, self).__init__(position, size, color_active, color_inactive, txt_func, font, font_size, text = '')

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect)
