from classes import Block, Position

class OBlock(Block):
    def __init__(self):
        # by super init id value is passed 
        super().__init__(id = 4)
        # position of each shape will be described in dict. 
        # each key will represent another position of shape after rotating
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1,0)]
        }


class IBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            1: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            2: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
            3: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)]
        }


class TBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 0)],
            1: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 1)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 2)]
        }


class JBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }


class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }


class SBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(0, 1), Position(0, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(2, 0), Position(2, 1), Position(1, 1), Position(1, 2)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2 ,2)],
            3: [Position(0, 2), Position(1, 2), Position(1, 1), Position(2, 1)]
        } 