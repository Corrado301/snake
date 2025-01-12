import pygame

from settings import Settings


pygame.init()


class Snake:

    def __init__(self, snake_game):

        self.settings = Settings()
        self.screen_rect = snake_game.screen_rect

        self.color = self.settings.snake_color

        self.image = pygame.surface.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def update_snake(self):

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.snake_speed

        elif self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.snake_speed

        elif self.move_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.snake_speed

        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.snake_speed
