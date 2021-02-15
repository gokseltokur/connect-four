from human_vs_human import *
from human_vs_ai import *
from ai_vs_ai import *
import sys
from board import *
import pygame
import numpy as np


# argv1 -> h-h h-ai ai-ai, 
# argv2 -> eval func., 
# argv3 -> ply, 
# argv4 -> which player starts first (0-1)
def main():
    
    pygame.init()
    board = Board()

    board.print_board()
    board.draw_board(1, 2)

    # Human vs Human
    if ( int(sys.argv[1]) == 0):
        human_vs_human(board, player_turn=int(sys.argv[4]))
    # Human vs AI
    elif( int(sys.argv[1]) == 1):
        print(sys.argv[0])
        print('h-h h-ai ai-ai ', sys.argv[1])
        print('eval func., ', sys.argv[2])
        print('ply, ', sys.argv[3])
        print('which player starts first (0-1)', sys.argv[4])
        print("HR")
        human_vs_ai(board, player_turn=int(sys.argv[4]), depth=int(sys.argv[3]), evaluation_function=int(sys.argv[2]))
    # AI vs AI
    elif (int(sys.argv[1]) == 2):
        print(sys.argv[0])
        print('h-h h-ai ai-ai ', sys.argv[1])
        print('eval func1, ', sys.argv[2])
        print('eval func2, ', sys.argv[3])
        print('ply, ', sys.argv[4])
        print('which player starts first (0-1)', sys.argv[5])
        ai_vs_ai(board, player_turn=int(sys.argv[5]), depth=int(sys.argv[4]), evaluation_function1=int(sys.argv[2]), evaluation_function2=int(sys.argv[3]))


if __name__ == '__main__':
    main()


