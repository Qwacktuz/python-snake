from settings import *
from snake2 import Snake
from apple2 import Apple

class Main:
    def __init__(self):
        # general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # The display surface is the main screen
        pygame.display.set_caption('Snake')

        # game objects 
        # pygame.Rect defines the (left side (y), top side (x), width, height)
        # Double for loops are awesome inside list comprehension
        # Alternative way to write this
#         result = []
# for row in range(ROWS):
#     for col in range(0, COLS, 2):
#         x = (col + int(row % 2 == 0)) * CELL_SIZE
#         y = row * CELL_SIZE
#         rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
#         result.append(rect)
        self.bg_rects = [pygame.Rect((col + int(row % 2 == 0)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) for col in range(0, COLS, 2) for row in range(ROWS)]

        self.snake = Snake()
        
        # The apple object needs to know where the snake is in order to spawn correctly
        self.apple = Apple(self.snake)


    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rect)

    # Pygame event loop
    def run(self):
        while True:
            # always have a end condition in a while loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # updates
            self.snake.move()

            self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()

# basically only runs the code inside the if block only if i am directly executing this python file
if __name__ == '__main__':
    main = Main()
    main.run()