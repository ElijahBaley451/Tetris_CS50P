"""
game.py contain Game class, which is resposible for menaging objects in game logic
"""

from shapes import *
from block import *
from grid import Grid
import random


class Game:
    """
    grid is an object constructor based on imported Grid class
    list blocks hold imported blocks
    current_block and next_block hold randomly selected block from blocks
    """
    # WARNING - SELF.BLOCKS HOLDS PROTOTYPES, NOT OBJECT CONSTRUCTORS
    # it prevents operational errors of interpreter garbage collector
    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            IBlock,
            OBlock,
            TBlock,
            JBlock,
            LBlock,
            SBlock,
            ZBlock,
        ]
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.game_over = False
        self.score = 0


    def score_update(self, rows_cleared):
        self.score += (100 * rows_cleared) * rows_cleared

    # method for generating random block from blocks list
    # program calls prototype from self.blocks, and initiate construction on return
    # to avoid problem with selecting an already called object
    def random_block(self):
        return random.choice(self.blocks)()


    # method which draws selected by current_block method block on grid
    def draw(self, surface):
        self.grid.draw(surface)
        self.current_block.draw(surface)


    """
    methods for moving block on grid. Arguments for move method
    corresponds to movements on the grid. Each movement of a block means checking whether 
    the block has not moved beyond the grid limits, by inside method.
    If the block moves outside the grid, the movement is reversed. block_collision checks
    whether block hits another block or not
    """
    def move_left(self):
        self.current_block.move(0, -1)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(0, 1)


    def move_right(self):
        self.current_block.move(0, 1)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(0, -1)


    # move_down method has emplemented logic for locking block in position, after it
    # bootom or another locked block
    def move_down(self):
        self.current_block.move(1, 0)
        if self.inside() == False or self.block_collision() == False:
            self.current_block.move(-1, 0)
            self.lock_block()


    # if block_collision return false, block is locked in position
    # grid tiles values matching with block position, take on values of block id
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.random_block()
        points = self.grid.clear_row()
        self.score_update(points)
        if self.block_collision() == False:
            self.game_over = True

    
    # This method checks, if grid tiles matching with block position are empty
    # via check_empty method from Grid class
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
        

    # method which check, if block after move is still inside game grid
    def inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.check_inside(tile.row, tile.column) == False:
                return False
        return True
    
    # method which resets grid, generated blocks and flag game_over
    # when called in game loop, after losing
    def reset_game(self):
        self.grid = Grid()
        self.game_over = False
        self.current_block = self.random_block()
        self.next_block = self.random_block()
