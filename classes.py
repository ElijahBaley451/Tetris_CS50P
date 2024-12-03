import pygame
from dataclasses import dataclass


# class which stores 8 colors of shapes in dict
class Colors:

    @classmethod
    def get_color(cls):
        return {
            0: (26, 31, 40), #grey
            1: (232, 18, 18), # red
            2: (31, 64, 216), # blue
            3: (47, 230, 23), # green   
            4: (237, 234, 4), # yellow
            5: (226, 116, 17), #orange
            6: (166, 0, 247), # purple
            7: (21, 204, 209) # cyan
            }
    

# class for grid generation in game display
class Grid:
    def __init__(self):
        # number of table rows
        self.num_rows = 20 
        # number od table columns
        self.num_col = 10 
        # size of cell wall
        self.cell_size = 30 
        # list comprehension for grid generation
        self.grid = [[0 for col in range(self.num_col)] for row in range(self.num_rows)]
        self.colors = Colors.get_color()

    # just for testing
    def print(self):
        return print(self.grid) 
    
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

# simple class which will hold tile coordinates on grid
@dataclass
class Position:
        row: int
        column: int

# parent class for block generation
class Block:
    def __init__(self, id):
        # by id value color of block will be chosen
        self.id = id
        # 
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_color()

    def draw(self, surface):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            
            tile_rect = pygame.Rect(
                tile.row * self.cell_size + 1,
                tile.column * self.cell_size + 1,
                self.cell_size -1,
                self.cell_size -1
                )
            pygame.draw.rect(surface, self.colors[self.id], tile_rect)
            
