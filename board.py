import numpy as np
import pygame


class Board:
    def __init__(self):
        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (50, 50, 50)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        # self
        self.rows = 6
        self.columns = 7

        # create empty self
        self.board = self.create_board()

        # square size of the screen
        self.square_size = 100
        # piece radius of the screen
        self.radius = int(self.square_size / 2 - 5)

        # height and width of the screen
        self.width = self.columns * self.square_size
        self.height = (self.rows + 1) * self.square_size

        # size of the screen
        self.size = (self.width, self.height)

        # set screen for the game
        self.screen = pygame.display.set_mode(self.size)

    # create board with zeros
    def create_board(self):
        board = np.zeros((self.rows, self.columns))
        return board

    # place the piece on board
    def place_piece(self, row, column, piece):
        self.board[row][column] = piece

    # check if the place for piece empty
    def is_empty(self, column):
        if self.board[self.rows - 1][column] == 0:
            return True
        else:
            return False

    def get_next_row(self, column):
        for row in range(self.rows):
            if self.board[row][column] == 0:
                return row

    def print_board(self):
        print('--- STATE ---')
        printer = np.flip(self.board.copy(), 0)
        for i in range(self.rows):
            for j in range(self.columns):
                if int(printer[i][j]) == 1:
                    print('R ', end='')
                elif int(printer[i][j]) == 2:
                    print('Y ', end='')
                else:
                    print('0 ', end='')
            print()
        print()

    def get_valid_locations(self):
        valid_locations = []
        for column in range(self.columns):
            if self.board[self.rows - 1][column] == 0:
                valid_locations.append(column)
        return valid_locations

    def check_win(self, piece):
        # Check horizontal locations for win
        for column in range(self.columns - 3):
            for row in range(self.rows):
                if (self.board[row][column] == piece 
                        and self.board[row][column + 1] == piece 
                        and self.board[row][column + 2] == piece 
                        and self.board[row][column + 3] == piece):
                    return True

        # Check vertical locations for win
        for column in range(self.columns):
            for row in range(self.rows - 3):
                if (self.board[row][column] == piece 
                        and self.board[row + 1][column] == piece 
                        and self.board[row + 2][column] == piece 
                        and self.board[row + 3][column] == piece):
                    return True

        # Check positively sloped diagonals
        for column in range(self.columns - 3):
            for row in range(self.rows - 3):
                if (self.board[row][column] == piece 
                        and self.board[row + 1][column + 1] == piece 
                        and self.board[row + 2][column + 2] == piece 
                        and self.board[row + 3][column + 3] == piece):
                    return True

        # Check negatively sloped diagonals
        for column in range(self.columns - 3):
            for row in range(3, self.rows):
                if (self.board[row][column] == piece 
                        and self.board[row - 1][column + 1] == piece 
                        and self.board[row - 2][column + 2] == piece 
                        and self.board[row - 3][column + 3] == piece):
                    return True
        #return False

    def draw_board(self, player_1, player_2):
        for column in range(self.columns):
            for row in range(self.rows):
                pygame.draw.rect(self.screen, self.white, (
                    column * self.square_size, row * self.square_size + self.square_size, self.square_size,
                    self.square_size))
                pygame.draw.circle(self.screen, self.gray, (
                    int(column * self.square_size + self.square_size / 2),
                    int(row * self.square_size + self.square_size + self.square_size / 2)), self.radius)

        for column in range(self.columns):
            for row in range(self.rows):
                if self.board[row][column] == player_1:
                    pygame.draw.circle(
                        self.screen,
                        self.red,
                        (
                            int(column * self.square_size + self.square_size / 2),
                            self.height - int(row * self.square_size + self.square_size / 2)
                        ),
                        self.radius
                    )
                elif self.board[row][column] == player_2:
                    pygame.draw.circle(
                        self.screen,
                        self.yellow,
                        (
                            int(column * self.square_size + self.square_size / 2),
                            self.height - int(row * self.square_size + self.square_size / 2)
                        ),
                        self.radius
                    )
        pygame.display.update()
