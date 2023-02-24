import pygame

class MenuButtons(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position

class ChatInput(MenuButtons):
    def __init__(self):
        super().__init__()
        message = ''

    def InputMessage(self):
        pass

    def CheckCommand(self):
        pass
