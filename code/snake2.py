from settings import * 

class Snake:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # create one point for every col in range (aka make the snake body from the start length)
        # (5, 5), (4, 5), (3, 5)
        # this is a list with three pygame.Vector2(x, y) points 
        self.body = [pygame.Vector2(START_COL - col, START_ROW) for col in range(START_LENGTH)]

        self.direction = pygame.Vector2(1, 0)
    
    def move(self):
        # 1. copy the list because immutability let's gooo
        body_copy = self.body[:]
        # 2. Get the head, aka the first coordinate in the list and move it in the direction
        new_head = body_copy[0] + self.direction
        # 3. Insert the new head at index 0
        body_copy.insert(0, new_head)
        # 4. Update the original body
        self.body = body_copy[:]

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.display_surface, 'blue', rect)