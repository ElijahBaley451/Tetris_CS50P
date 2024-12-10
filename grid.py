import pygame, random
from colors import Colors

class Grid:
    def __init__(self):
        # number of table rows
        self.num_rows = 20 
        # number od table columns
        self.num_col = 10 
        # size of cell wall
        self.cell_size = 30 
        # list comprehension for grid generation
        self.grid = [[0 for _ in range(self.num_col)] for _ in range(self.num_rows)]
        self.colors = Colors.get_color()

    def check_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_col:
            return True
        return False

    # main function for grid draw
    def draw(self, surface):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                # variable for color of the cell - which is zero, which indicates dark grey from Colors
                cell_value = self.grid[row][column]
                # variable for grid and squares generation - +/- for grid visibility
                cell_rect = pygame.Rect(
                    column*self.cell_size +1, 
                    row*self.cell_size +1,
                    self.cell_size -1,
                    self.cell_size -1
                )
                pygame.draw.rect(surface, self.colors[cell_value], cell_rect)