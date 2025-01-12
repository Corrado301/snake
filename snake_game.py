from sys import exit
import pygame

from settings import Settings
from snake import Snake

pygame.init()


class SnakeGame:

    def __init__(self):

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()

        self.snake = Snake(self)

    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()
            self._update_snake()

            self.clock.tick(self.settings.fps)

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_RIGHT:
                    self.snake.move_right = True

                    self.snake.move_left = False
                    self.snake.move_up = False
                    self.snake.move_down = False

                if event.key == pygame.K_LEFT:
                    self.snake.move_left = True

                    self.snake.move_right = False
                    self.snake.move_up = False
                    self.snake.move_down = False

                if event.key == pygame.K_UP:
                    self.snake.move_up = True

                    self.snake.move_right = False
                    self.snake.move_left = False
                    self.snake.move_down = False

                if event.key == pygame.K_DOWN:
                    self.snake.move_down = True

                    self.snake.move_right = False
                    self.snake.move_left = False
                    self.snake.move_up = False

    def _update_screen(self):

        self.screen.fill(self.settings.screen_color)
        self.screen.blit(self.snake.image, self.snake.rect)

        pygame.display.flip()

    def _update_snake(self):

        self.snake.update_snake()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run_game()
