import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20 # twenty rows
        self.num_col = 10 # ten columns
        self.cell_size = 30 # cell size (30x30 in pixels)
        self.grid = [[0 for column in range(self.num_col)] for row in range(self.num_rows)]
        self.colors = self.cell_colors() # dict of colors

    def print_grid(self):
        print(self.grid)

    def cell_colors(self):

        return {
            0: (26, 31 ,40), # dark grey
            1: (47, 230, 23), # green
            2: (232, 18, 18), # red
            3: (226, 116, 17), # orange
            4: (237, 234, 4), # yellow
            5: (166, 0, 247), # purple
            6: (21, 204, 209), # cyan
            7: (13, 64, 216) # blue
        }
    
    def draw(self, surface):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size +1,
                    row * self.cell_size +1,
                    self.cell_size -1,
                    self.cell_size -1
                )
                pygame.draw.rect(
                    surface,
                    self.colors[cell_value],
                    cell_rect
                )