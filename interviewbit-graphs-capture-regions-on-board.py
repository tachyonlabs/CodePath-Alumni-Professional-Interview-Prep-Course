class Solution:
    # @param A : list of list of chars
    def capture(self, r, c):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [(r, c)]
        to_fill = [(r, c)]
        self.A_copy[r][c] = "X"
        surrounded = True
        while stack:
            row, col = stack.pop()
            for y, x in directions:
                new_r, new_c = row + y, col + x
                if new_r < 0 or new_r == len(self.A) or new_c < 0 or new_c == len(self.A[0]):
                    surrounded = False
                else:
                    if self.A_copy[new_r][new_c] == "O":
                        self.A_copy[new_r][new_c] = "X"
                        stack.append((new_r, new_c))
                        to_fill.append((new_r, new_c))

        if surrounded:
            for row, col in to_fill:
                self.A[row][col] = "X"

    def solve(self, A):
        self.A = [list(row) for row in A]
        A_copy = [list(row) for row in A]
        self.A_copy = A_copy
        for row in range(len(A)):
            for col in range(len(A[0])):
                if self.A_copy[row][col] == "O":
                    self.capture(row, col)

        # this is kind of screwy because it wants you to modify
        # the original array rather than return anything
        for i in range(len(A)):
            A[i] = "".join(self.A[i])
