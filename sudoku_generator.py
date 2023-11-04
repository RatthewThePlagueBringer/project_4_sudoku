import math, copy, random

class SudokuGenerator:
    def __init__(self, size, removed_cells):
        self.row_length = size
        self.removed_cells = removed_cells
        # Create an empty board with '-' as cells
        self.board = [['-' for i in range(self.row_length)] for j in range(self.row_length)]
        # Calculate the size of each box (3x3 subgrid)
        self.box_length = int(math.sqrt(self.row_length))

    def get_board(self):
        # Return the board's current state
        return self.board

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()

    # Determines if num is contained in the specified row (horizontal) of the board
    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # Determines if num is contained in the specified column (vertical) of the board
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def valid_in_box(self, row_start, col_start, num):
        box_row = row_start - row_start % int(math.sqrt(self.row_length))
        box_col = col_start - col_start % int(math.sqrt(self.row_length))
        for i in range(box_row, box_row + int(math.sqrt(self.row_length))):
            for j in range(box_col, box_col + int(math.sqrt(self.row_length))):
                if self.board[i][j] == num:
                    return False
        return True

    # Returns if it is valid to enter num at (row, col) in the board
    def is_valid(self, row, col, num):
        if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row, col, num):
            return True
        return False

    # Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.choice(nums)
                while not self.is_valid(i, j, num):
                    num = random.choice(nums)
                self.board[i][j] = num
                nums.remove(num)
        return self.board

    # Fills the three boxes along the main diagonal of the board
    def fill_diagonal(self):
        boxes = [0, 3, 6]
        for box in boxes:
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(box, box + 3):
                for j in range(box, box + 3):
                    num = random.choice(nums)
                    while not self.is_valid(i, j, num):
                        num = random.choice(nums)
                    self.board[i][j] = num
                    nums.remove(num)

    # Returns a completely filled board (provided)
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # constructs a solution by calling fill_diagonal and fill_remaining (provided)
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # Removes the appropriate number of cells from the board
    # randomly generating (row, col) coordinates of the board and setting the value to 0
    def remove_cells(self):
        # Create a set to store the coordinates of removed cells
        removed_cells = set()
        # Number of cells to remove
        cells_to_remove = self.removed_cells

        for i in range(cells_to_remove):
            while True:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if (row, col) not in removed_cells and self.board[row][col] != 0:
                    break

            # Set cell value to 0 for empty cells
            self.board[row][col] = 0
            # Add the (row, col) coordinate to 'removed_cells' set
            removed_cells.add((row, col))

    # def fill_cell(self, row, col, num):
    #     # Check if the provided row and column are within the bounds of the board
    #     if 1 <= row < self.row_length and 1 <= col < self.row_length:
    #         # Check if the provided number is valid for the cell
    #         if self.is_valid(row, col, num):
    #             self.board[row][col] = num
    #             print(f"Number {num} successfully filled in cell ({row}, {col}).")
    #         else:
    #             print(f"Invalid number {num} for cell ({row}, {col}).")
    #     else:
    #         print("Invalid cell coordinates. Please enter valid row and column values.")
    #
    # def check_winning(self):
    #     if 0 not in self.board:
    #         return True
    #     return False


# def generate_sudoku(size, removed):
#     sudoku = SudokuGenerator(size, removed)
#     sudoku.fill_values()
#     board = sudoku.get_board()
#     sudoku.remove_cells()
#     board = sudoku.get_board()
#     return board

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    original_board = copy.deepcopy(board)
    sudoku.remove_cells()
    board = sudoku.get_board()
    return [board, original_board]