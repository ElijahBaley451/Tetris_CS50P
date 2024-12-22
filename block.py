"""
block.py holds two classes - Position for holding coordinates and Block
for all actions related to block. Block class acts as parent class for all 7 
blocks, which acts as standalone classes inheriting from Block class.
"""


import pygame
from dataclasses import dataclass
from shapes import *
from colors import Colors


# Class which will hold tile coordinates on grid, as dataclass
@dataclass
class Position:
        row: int
        column: int


# Parent class for block generation
class Block:
    def __init__(self, id):
        """
        By id value, color is assigned to block
        cells dictionary hold coordinates of each tile in rotation state
        cell_size hold value which express lenght/width of cell on grid
        row_offset and column_offset store information about the offset from starting point for moving blocks on grid
        rotation_state hold value corresponding do key on dict, which represents coordinates of rotated block
        """
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_color()
        # to spawn block in the middle of top wall, block is moved
        self.move(0, 4)


    # method which modify tile coordinates by offset value
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns


    # method which returns actual coordinates of each tile of shape
    # starting coordinates of each tile are modified by offset values 
    # which are returned by move method
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


    # draw method draws block on grid
    # every tile position is modified by offset values by assigning to the tiles variable
    # get_cell_positions method.
    # in next step, we render each tile from tiles on grid using Rect method
    # arguments for Rect are modified, to make the grid visible
    def draw(self, surface, offset_x = 1, offset_y = 1):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x +  tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size ,
                self.cell_size -1,
                self.cell_size -1
                )
            pygame.draw.rect(surface, self.colors[self.id], tile_rect)
