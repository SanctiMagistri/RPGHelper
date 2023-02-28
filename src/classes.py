import pygame

class DiceButtons(pygame.sprite.Sprite):
    def __init__(self, pic_path, position, clicked_pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.path = pic_path
        self.path_clicked = clicked_pic_path

    def update(self, is_clicked):
        if is_clicked == True:
            self.image = pygame.image.load(self.path_clicked)
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
