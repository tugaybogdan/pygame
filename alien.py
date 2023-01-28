import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """" Класс для одного пришельца """

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen

        # Скачивание изображения пришельца 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляеться в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Изображение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
