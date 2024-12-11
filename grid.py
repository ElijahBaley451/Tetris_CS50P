import pygame
from colors import Colors


class Grid:
    def __init__(self):
        """
        num_rows and num_col holds number of rows and columns of grid
        cell_size represents length/width of grid tile
        colors return values from Colors dict
        """
        self.num_rows = 20
        self.num_col = 10
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
                # cell_value assign to each cell starting value of 0, which corresponds to cell color (dark grey)
                cell_value = self.grid[row][column]
                # in this variable each cell of grid is generated
                # cell_value assign to each cell starting value of 0
                # arguments which are passed do draw.rect method are modified, to make grid visible
                cell_rect = pygame.Rect(
                    column * self.cell_size + 1,
                    row * self.cell_size + 1,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(surface, self.colors[cell_value], cell_rect)
