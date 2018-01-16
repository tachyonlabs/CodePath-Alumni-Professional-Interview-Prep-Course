class Solution:
    # @param A : integer
    # @return a list of list of strings
    def can_place_queen(self, r, c, queens):
        for qr, qc in queens:
            if r == qr or c == qc or r + c == qr + qc or r - c == qr - qc:
                return False

        return True

    def format_board(self, coords):
        board = []
        for r, c in coords:
            board.append("." * c + "Q" + "." * (len(coords) - c - 1))

        return board

    def find_valid_boards(self, n, row=0, queens=tuple()):
        for c in range(n):
            if self.can_place_queen(row, c, queens):
                if row == n - 1:
                    self.valid.append(queens + ((row, c),))
                else:
                    self.find_valid_boards(n, row + 1, queens + ((row, c),))

    def solveNQueens(self, A):
        self.valid = []
        self.find_valid_boards(A)
        return [self.format_board(board) for board in self.valid]
