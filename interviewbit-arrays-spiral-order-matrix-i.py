class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        top, right, bottom, left = 0, len(A[0]) - 1, len(A) - 1, 0
        r, d, l, u = 0, 1, 2, 3
        direction = r
        while top <= bottom and left <= right:
            if direction == r:
                for i in range(left, right + 1):
                    result.append(A[top][i])
                top += 1
            elif direction == d:
                for i in range(top, bottom + 1):
                    result.append(A[i][right])
                right -= 1
            elif direction == l:
                for i in range(right, left - 1, -1):
                    result.append(A[bottom][i])
                bottom -= 1
            elif direction == u:
                for i in range(bottom, top - 1, -1):
                    result.append(A[i][left])
                left += 1
            direction = (direction + 1) % 4

        return result
