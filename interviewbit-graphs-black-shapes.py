class Solution:
    # @param A : list of strings
    # @return an integer
    def clear_black_shape(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.A[row][col] = "O"
        stack = [(row, col)]
        while stack:
            rr, cc = stack.pop()
            for y, x in directions:
                new_r, new_c = rr + y, cc + x
                if new_r >= 0 and new_r < len(self.A) and new_c >= 0 and new_c < len(self.A[0]) and self.A[new_r][new_c] == "X":
                    self.A[new_r][new_c] = "O"
                    stack.append((new_r, new_c))

    def black(self, A):
        self.A = [list(row) for row in A]
        black_shapes_count = 0
        for r in range(len(A)):
            for c in range(len(A[0])):
                if self.A[r][c] == "X":
                    black_shapes_count += 1
                    self.clear_black_shape(r, c)

        return black_shapes_count
