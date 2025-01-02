from project import main_constructor
from shapes import *

shapes = [
    IBlock(),
    OBlock(),
    TBlock(),
    JBlock(),
    LBlock(),
    SBlock(),
    ZBlock(),
    ]

def test_main_constructor():
    game = main_constructor()

def test_move_down():
    game = main_constructor()
    for _ in range(3):
        game.move_down()
    assert game.current_block.row_offset == 3

def test_inside():
    game = main_constructor()
    game.current_block.move(0, 7)
    assert game.inside() == False

    game.reset_game()

    game.current_block.move(0, 2)
    assert game.inside() == True

def test_game_lock():
    game = main_constructor()
    for _ in range(20):
        game.move_down()
    assert game.inside() == True