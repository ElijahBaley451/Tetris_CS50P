import pygame, sys
from classes import Grid


def main():
    pygame.init()

    screen = pygame.display.set_mode((480, 640))

    clock = pygame.time.Clock()

    game_grid = Grid()
    

    # main loop of game with event menagement
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Basic screen logic
        pygame.display.update()
        screen.fill("black")
        game_grid.draw(screen)
        clock.tick(60)


    
def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
