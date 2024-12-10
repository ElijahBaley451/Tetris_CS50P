from shapes import *
from block import *
from grid import Grid
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), OBlock(), TBlock(), JBlock(), LBlock(), SBlock(), ZBlock()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()

    def random_block(self):
        block = random.choice(self.blocks)
        return block
    
    def draw(self, surface):
        self.grid.draw(surface)
        self.current_block.draw(surface)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.inside() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.inside() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.inside() == False:
            self.current_block.move(-1, 0)

    def inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.check_inside(tile.row, tile.column) == False:
                return False
        return True