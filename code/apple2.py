from settings import *
from random import choice


class Apple:
    def __init__(self, snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()

        # use join method for the non-linux users out there
        # apparently needs to omit ".." because the path is relative to main.py
        self.surface = pygame.image.load(
            join("graphics", "apple.png")
        ).convert_alpha()

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
        self.display_surface.blit(
            self.surface,
            pygame.Rect(
                self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
        )
