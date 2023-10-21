from settings import *
from snake import Snake
from apple import Apple


class Main:
    def __init__(self):
        # ---------- general ----------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # The display surface is the main screen
        pygame.display.set_caption("Totally Not A Google Snake Clone")

        # ---------- game objects ----------
        # pygame.Rect defines the (left side (y), top side (x), width, height)
        # Double for loops are awesome inside list comprehension
        self.bg_rects = [
            pygame.Rect(
                (col + int(row % 2 == 0)) * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            for col in range(0, COLS, 2)
            for row in range(ROWS)
        ]

        self.snake = Snake()

        # The apple object needs to know where the snake is in order to spawn correctly
        self.apple = Apple(self.snake)

        # ---------- Timer ----------
        # calls every 200 ms / 5 times per second
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 100)
        self.game_started = False

        # ---------- Audio ----------
        self.crunch_sound = pygame.mixer.Sound(join('audio', 'crunch.wav'))
        self.bg_music = pygame.mixer.Sound(join('audio', 'Arcade.ogg'))
        self.bg_music.set_volume(0.5)
        self.bg_music.play(-1)

    def draw_bg(self):
        self.display_surface.fill(LIGHT_GREEN)
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rect)

    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.snake.direction = (
                pygame.Vector2(1, 0)
                if self.snake.direction.x != -1
                else self.snake.direction
            )
        if keys[pygame.K_LEFT]:
            self.snake.direction = (
                pygame.Vector2(-1, 0)
                if self.snake.direction.x != 1
                else self.snake.direction
            )
        if keys[pygame.K_UP]:
            self.snake.direction = (
                pygame.Vector2(0, -1)
                if self.snake.direction.y != 1
                else self.snake.direction
            )
        if keys[pygame.K_DOWN]:
            self.snake.direction = (
                pygame.Vector2(0, 1)
                if self.snake.direction.y != -1
                else self.snake.direction
            )

    def collision(self):
        # Apple
        if self.snake.body[0] == self.apple.pos:
            self.snake.has_eaten = True
            self.apple.set_pos()
            self.crunch_sound.play()

        # Game over
        # Basically check if it collides with itself or is outside of the window (COLS and ROWS)
        if (
            self.snake.body[0] in self.snake.body[1:]
            or not 0 <= self.snake.body[0].x < COLS
            or not 0 <= self.snake.body[0].y < ROWS
        ):
            self.snake.reset()
            self.game_started = False

    def run(self):
        # ---------- Event loop ----------
        while True:
            for event in pygame.event.get():
                # always have a condition to stop the loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.update_event and self.game_started:
                    self.snake.move()
                if event.type == pygame.KEYDOWN and not self.game_started:
                    self.game_started = True

            # ---------- Updates ----------
            self.user_input()
            self.collision()

            # ---------- Drawing ----------
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()

            pygame.display.update()


# basically only runs the code inside the if block only if i am directly executing this python file
if __name__ == '__main__':
    main = Main()
    main.run()
