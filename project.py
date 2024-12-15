import pygame
import sys
from shapes import *
from game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((480, 640))

    clock = pygame.time.Clock()

    game = Game()

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 300)

    # main loop of game with event menagement
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_SPACE:
                    game.rotate_block()
            if event.type == GAME_UPDATE:
                game.move_down()


        # Basic screen logic
        screen.fill("black")
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
