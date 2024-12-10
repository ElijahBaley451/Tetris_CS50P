import pygame, random
from dataclasses import dataclass
from shapes import *
from colors import Colors

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
        # dictionary for cells position in each rotation state
        self.cells = {}
        self.cell_size = 30
        # variables for moving shapes on grid
        # they store information about the offset from starting point
        self.row_offset = 0
        self.column_offset = 0
        # variable for storing information about the offset from starting point
        self.rotation_state = 0
        self.colors = Colors.get_color()
        # to spawn block in the middle of top wall, block is moved
        self.move(0, 3)

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(
                position.row + self.row_offset,
                position.column + self.column_offset
            )
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, surface):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size -1,
                self.cell_size -1
                )
            pygame.draw.rect(surface, self.colors[self.id], tile_rect)
