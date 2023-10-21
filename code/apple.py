from settings import *
from random import choice
from math import sin


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()

        # use join method for the non-linux users out there
        # apparently needs to omit ".." because the path is relative to main.py
        self.surf = pygame.image.load(join('graphics', 'apple.png')).convert_alpha()

    def set_pos(self):
        # basically the pygame.Vector2(x, y) basically gets stored in a list where you have both x and y posistion and check if apple is on the snake body
        # add the coordinates to list of available positions if it isn't on the body
        available_pos = [
            pygame.Vector2(x, y)
            for x in range(COLS)
            for y in range(ROWS)
            if pygame.Vector2(x, y) not in self.snake.body
        ]
        self.pos = choice(available_pos)

    def draw(self):
        scale = 1.5 + sin(pygame.time.get_ticks() / 600) / 5
        self.scaled_surf = pygame.transform.smoothscale_by(self.surf, scale)
        self.scaled_rect = self.scaled_surf.get_rect(
            center=(
                self.pos.x * CELL_SIZE + CELL_SIZE / 2,
                self.pos.y * CELL_SIZE + CELL_SIZE / 2,
            )
        )
        self.display_surface.blit(self.scaled_surf, self.scaled_rect)
