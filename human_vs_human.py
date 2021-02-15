from board import *
import pygame
import sys
import math


def human_vs_human(board, player_turn):
    game_over = False
    turn = player_turn
    while not game_over:
        if len(board.get_valid_locations()) == 0:
            label = pygame.font.SysFont("monospace", 24).render("DRAW!", 0, board.white)
            board.screen.blit(label, (40, 10))
            pygame.display.update()
            game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(
                    board.screen,
                    board.gray,
                    (0, 0, board.width, board.square_size)
                )
                position_x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(
                        board.screen,
                        board.red,
                        (position_x, int(board.square_size / 2)),
                        board.radius
                    )
                else:
                    pygame.draw.circle(
                        board.screen,
                        board.yellow,
                        (position_x, int(board.square_size / 2)),
                        board.radius
                    )
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print('------------------------------')
                pygame.draw.rect(
                    board.screen,
                    board.gray,
                    (0, 0, board.width, board.square_size)
                )
                position_x = event.pos[0]
                column = int(math.floor(position_x / board.square_size))
                if turn == 0:

                    if board.is_empty(column):
                        row = board.get_next_row(column)
                        board.place_piece(row, column, 1)

                        if board.check_win(1):
                            label = pygame.font.SysFont("monospace", 24).render("Red wins!", 1, board.red)
                            board.screen.blit(label, (40, 10))
                            game_over = True
                else:

                    if board.is_empty(column):
                        row = board.get_next_row(column)
                        board.place_piece(row, column, 2)

                        if board.check_win(2):
                            label = pygame.font.SysFont("monospace", 24).render("Yellow wins!", 2, board.yellow)
                            board.screen.blit(label, (40, 10))
                            game_over = True

                board.print_board()
                board.draw_board(1, 2)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)


if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    board.print_board()
    board.draw_board(1, 2)
    human_vs_human(board, player_turn)
