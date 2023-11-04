import pygame, copy
from sudoku_generator import SudokuGenerator
from constants import *
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty, sudoku_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # two sets of board to compare user answer with the solution
        self.board = sudoku_board
        # self.board = copy.deepcopy(sudoku_board)

        self.board_rows = len(self.board)  # number of rows
        self.board_cols = len(self.board[0])  # number of columns

        # Create cells based on sudoku_board values
        self.cells = [[Cell(self.board[row][col], row, col, self.screen)
                       for col in range(self.board_cols)]
                      for row in range(self.board_rows)]

    def draw(self):
        # Calculate the width and height of the board
        BOARD_WIDTH = 9 * CELL_SIZE
        BOARD_HEIGHT = 9 * CELL_SIZE

        # Calculate the starting position
        board_start_x = (WIDTH - BOARD_WIDTH) // 2
        board_start_y = (HEIGHT - BOARD_HEIGHT) // 2 - 70  # move board up ~ 70 px

        # Draw the cells
        for row in self.cells:
            for cell in row:
                cell_rect = pygame.Rect(board_start_x + cell.col * CELL_SIZE, board_start_y + cell.row * CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, SCREEN_COLOR, cell_rect)
                cell.draw(self.screen)

        # Draw the squares for the board
        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_start_x, board_start_y + (3 * i) * CELL_SIZE),
                             (board_start_x + BOARD_WIDTH, board_start_y + (3 * i) * CELL_SIZE),
                             BOARD_LINE_WIDTH)

        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_start_x + (3 * i) * CELL_SIZE, board_start_y),
                             (board_start_x + (3 * i) * CELL_SIZE, board_start_y + BOARD_HEIGHT),
                             BOARD_LINE_WIDTH)

    # Marks the cell at (row, col) in the board as the current selected cell
    def select(self, row, col):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if i == row and j == col:
                    self.cells[i][j].selected = True
                else:
                    self.cells[i][j].selected = False

    # returns a tuple of the (row, col) of the cell which was clicked
    def click(self, x, y):
        # Calculate the width and height of the board
        BOARD_WIDTH = 9 * CELL_SIZE
        BOARD_HEIGHT = 9 * CELL_SIZE

        # Calculate the starting position
        board_start_x = (WIDTH - BOARD_WIDTH) // 2
        board_start_y = (HEIGHT - BOARD_HEIGHT) // 2 - 70  # move board up ~ 70 px

        # if coordinates inside the board (which calculated by adding board's width and height to the starting points)
        if board_start_x <= x < board_start_x + BOARD_WIDTH and board_start_y <= y < board_start_y + BOARD_HEIGHT:
            clicked_row = (y - board_start_y) // CELL_SIZE
            clicked_col = (x - board_start_x) // CELL_SIZE
            return (clicked_row, clicked_col)

        return None

    # allows user to remove the cell values and sketched value that are filled by themselves
    def clear(self):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if self.cells[i][j].selected:
                    # check if it's an empty cell in the original board
                    if self.board[i][j] == 0:
                        self.cells[i][j].sketched_value = 0
                        self.cells[i][j].value = 0

    # if cell is selected and value is currently 0, set sketched value to value
    def sketch(self, value):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].selected:
                    if self.board[col][row] == 0:
                        self.cells[col][row].set_sketched_value(value)

    def place_number(self, value):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].selected:
                    if self.board[col][row] == 0:
                        self.cells[col][row].sketched_value = 0
                        self.cells[col][row].set_cell_value(value)

    # resets cells in board to original values and removes sketched values
    def reset_to_original(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                self.cells[row][col].value = self.original[row][col]
                self.cells[row][col].sketched_value = 0

    # determine if board is full by checking each cell
    # if cell value == 0 return false
    # if no cells == 0 return true (board is full)
    def is_full(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].value == 0:
                    return False
        return True

    # set cell.value to cell.sketched_value for each cell
    def update_board(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].sketched_value != 0:
                    self.cells[col][row].value = self.cells[col][row].sketched_value

    # check if value of cell == 0 and return that cells col and row
    def find_empty(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].value == 0 and self.cells[col][row].sketched_value == 0:
                    return col, row

    # checks if value in each cell is valid in col, row, and box
    # returns true if correctly solved
    def check_board(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                num = self.cells[col][row].value
                if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row, col, num):
                    return True
        return False
