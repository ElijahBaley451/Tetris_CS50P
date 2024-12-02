from classes import Block, Position
import pygame

class Square(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1,0)]
        }
