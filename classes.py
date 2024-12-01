import pygame

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
    

class Grid:
    def __init__(self):
        self.num_rows = 20 # number of table rows
        self.num_col = 10 # number od table columns
        self.cell_size = 30 # size of cell wall
        # list comprehension for grid generation
        self.grid = [[0 for col in range(self.num_col)] for row in range(self.num_rows)]
        self.colors = Colors.get_color()

    def print(self):
        return print(self.grid) 
    
    def draw(self, surface):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                # variable for coordinates of actually procesed cell
                cell_value = self.grid[row][column]
                #
                cell_rect = pygame.Rect(
                    column*self.cell_size +1, 
                    row*self.cell_size +1,
                    self.cell_size -1,
                    self.cell_size -1
                )
                pygame.draw.rect(surface, self.colors[cell_value], cell_rect)
