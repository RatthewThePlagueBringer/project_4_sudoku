from board import Board


class SudokuGenerator:
    def __init__(self, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells

    def get_board(self):
        pass

    def print_board(self):
        pass

    def valid_in_row(self, row, num):
        pass

    def valid_in_col(self, col, num):
        pass

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass

    def generate_sudoku(self, removed):
        pass
