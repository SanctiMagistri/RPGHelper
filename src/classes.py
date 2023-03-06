import pygame
from src.scripts import throw_dice

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


class ChatInput(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position
        message = ''

    def InputMessage(self):
        pass

    def CheckCommand(self):
        pass
