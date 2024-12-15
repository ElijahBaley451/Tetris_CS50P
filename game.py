"""
game.py contain Game class, which is resposible for menaging objects in game logic
"""

from shapes import *
from block import *
from grid import Grid
import random
from random import randint

chosen_numbers = []

class Game:
    """
    grid is an object constructor based on imported Grid class
    list blocks hold imported blocks
    current_block and next_block hold randomly selected block from blocks
    """

    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            IBlock(),
            OBlock(),
            TBlock(),
            JBlock(),
            LBlock(),
            SBlock(),
            ZBlock(),
        ]
        print("First generated blocks")
        self.current_block = self.random_block()
        self.next_block = self.random_block()

    # method for generating random block from blocks list
    """def random_block(self):
        ind = randint(0, 6)
        print(ind)
        chosen_numbers.append(ind)
        print(chosen_numbers)
        block = blocks[ind]
        return block"""

    def random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [
            IBlock(),
            OBlock(),
            TBlock(),
            JBlock(),
            LBlock(),
            SBlock(),
            ZBlock(),
        ]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block


    # method which draws selected by current_block method block on grid
    def draw(self, surface):
        self.grid.draw(surface)
        self.current_block.draw(surface)


    # methods for moving block on grid
    # move method is used on current block. Arguments for move method
    # corresponds to movements on the grid
    # each movement of a block means checking whether the block has not moved beyond the limits, by inside method
    # if the block moves outside the grid, the movement is reversed
    def move_left(self):
        self.current_block.move(0, -1)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(0, 1)


    def move_right(self):
        self.current_block.move(0, 1)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(0, -1)


    def move_down(self):
        self.current_block.move(1, 0)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(-1, 0)
            self.lock_block()


    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        print("next blok staje sie current blokiem")
        self.current_block = self.next_block
        print("generowanie kolejnego bloku")
        self.next_block = self.random_block()
        self.grid.clear_row()

    
    def block_collision(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.check_empty(tile.row, tile.column) == False:
                return False
        return True


    # Method for rotating block. Each time when block is rotated
    # rotation_state is incrementing. To prevent overclocking of rotation_state
    # there is bool to check if rotation_state is not greater than the length of the dictionary
    def rotate_block(self):
        if self.current_block.rotation_state == len(self.current_block.cells) - 1:
            self.current_block.rotation_state = 0
        else:
            self.current_block.rotation_state += 1

        if self.inside() == False or self.block_collision() == False:
            if self.current_block.rotation_state == 0:
                self.current_block.rotation_state = len(self.current_block.cells) - 1
            else:
                self.current_block.rotation_state -= 1
        

    # method which check, if block after move is still oinside game grid
    def inside(self):
        # every tile from
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.check_inside(tile.row, tile.column) == False:
                return False
        return True
