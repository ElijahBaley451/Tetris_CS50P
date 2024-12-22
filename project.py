import pygame
import sys
from shapes import *
from game import Game
from colors import Colors


def main():

    # game engine initialization
    pygame.init()

    screen = pygame.display.set_mode((480, 620))

    # fonts for game labels
    main_font = pygame.font.Font("joystix_monospace.otf", 18)
    small_font = pygame.font.Font("joystix_monospace.otf", 8)

    # variables related with score displaying
    score_text = main_font.render("Score", True, Colors.get_color()[8])
    score_rect = pygame.Rect(327, 50, 120, 50)

    # variables related to next block hint renndering
    next_block_text = main_font.render("Next Block", True, Colors.get_color()[8])
    next_block_rect = pygame.Rect(317, 280, 150, 150)

    # variable related top rendering game over
    game_over_text = main_font.render("Game Over", True, Colors.get_color()[8])


    # game clock
    clock = pygame.time.Clock()

    # game constructor
    game = Game()
    

    # user event with timer. timer acts as counter which allows 
    # the block's downward movement at regular intervals
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 300)

    # main loop of game with event menagement
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game.game_over == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.reset_game()

            # key mapping used forf playing game
            if event.type == pygame.KEYDOWN and game.game_over == False:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_SPACE:
                    game.rotate_block()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()


        # Basic user interface logic
        # variable for score holding and rendereing
        score_counter = main_font.render(f"{game.score}", True, Colors.get_color()[8])


        # background and labels generation
        screen.fill("black")
        screen.blit(score_text, (350, 20, 50, 50))
        screen.blit(next_block_text, (318, 250, 50, 50))
        

        # logic for Game Over rendering
        if game.game_over == True:
            screen.blit(game_over_text, (320, 470, 50, 50))


        # rendering rectangles which displays score and next block
        pygame.draw.rect(screen, Colors.get_color()[9], score_rect, 0, 10)

        pygame.draw.rect(screen, Colors.get_color()[9], next_block_rect, 0, 10)


        # displaying player score
        screen.blit(score_counter, (335, 63, 50, 50))
        game.draw(screen)


        # logic for displaying next block hint
        if game.next_block.id == 4:
            game.next_block.draw(screen, 242, 325)
        elif game.next_block.id == 7:
            game.next_block.draw(screen, 213, 310)
        else:
            game.next_block.draw(screen, 227, 325)


        pygame.display.update()
        clock.tick(60)


def function_1(): ...


def function_2(): ...


def function_n(): ...


if __name__ == "__main__":
    main()
