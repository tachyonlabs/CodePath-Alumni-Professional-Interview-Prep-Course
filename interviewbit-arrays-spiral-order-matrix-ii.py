class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = []
        for r in range(A):
            row = []
            for c in range(A):
                row.append(0)
            matrix.append(row)

        top = left = 0
        bottom = right = A - 1
        i = 1
        r, d, l, u = 0, 1, 2, 3
        direction = r
        while i <= A**2:
            if direction == r:
                for col in range(left, right + 1):
                    matrix[top][col] = i
                    i += 1
                top += 1
            elif direction == d:
                for row in range(top, bottom + 1):
                    matrix[row][right] = i
                    i += 1
                right -= 1
            elif direction == l:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = i
                    i += 1
                bottom -= 1
            elif direction == u:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = i
                    i += 1
                left += 1

            direction = (direction + 1) % 4

        return matrix

