class TicTacToe :
    def __init__(self):
        self.current_turn = "0"
        self.board = ["."] * 9
        # [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        # self.board[row][col]

    def check_winner(self):
        check = self.current_turn
        # -, /
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check \
                or self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
                return check

        # \/
        if (self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check) \
                or (self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check):
            return check

        if not "." in self.board:
            return "d"

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def set(self, row, col):
        if self.get(row, col) == ".":
            self.current_turn = "X" if self.current_turn == "0" else "0"
            self.board[(row * 3) + col] = self.current_turn

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board):
            s += v
            if i % 3 == 2:
                s += "\n"
        return s

ttt = TicTacToe()
print(ttt)
ttt.set(0, 0)
ttt.set(1, 1)
ttt.set(0, 1)
ttt.set(1, 2)
ttt.set(0, 2)
print(ttt)

print(ttt.check_winner())