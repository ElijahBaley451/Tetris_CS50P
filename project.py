import pygame, sys
from shapes import *
from game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((480, 640))

    clock = pygame.time.Clock()

    game = Game()
    
    # main loop of game with event menagement
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Basic screen logic
        screen.fill("black")
        game.draw(screen)

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
