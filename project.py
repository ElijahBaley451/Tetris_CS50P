import pygame, sys
from classes import Grid

def main():
    pygame.init() # engine initialization
    screen = pygame.display.set_mode((300, 600)) # game screen resolution
    pygame.display.set_caption("Tetris CS50P")
    
    clock = pygame.time.Clock() # game clock, by which we choose refresh rate

    game_grid = Grid()
    game_grid.print_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")
        game_grid.draw(screen)

        pygame.display.update()

        clock.tick(60)

def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
