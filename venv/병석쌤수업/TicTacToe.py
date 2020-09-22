class TicTacToe :
    def __init__(self):
        self.current_turn = "0"
        self.board = ["."] * 9
        # [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        # self.board[row][col]

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def set(self, row, col):
        if self.get(row, col) == ".":
            self.current_turn = "X" if self.current_turn == "0" else "0"
            self.board[(row * 3) + col] = self.current_turn