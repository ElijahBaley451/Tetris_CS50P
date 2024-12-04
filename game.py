from shapes import *
from classes import *
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