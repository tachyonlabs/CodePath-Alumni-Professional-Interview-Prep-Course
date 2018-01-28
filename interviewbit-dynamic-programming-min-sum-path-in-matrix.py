class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        for r in range(len(A) - 1, -1, -1):
            for c in range(len(A[0]) - 1, -1, -1):
                if r < len(A) - 1 and c < len(A[0]) - 1:
                    A[r][c] += min(A[r + 1][c], A[r][c + 1])
                elif r < len(A) - 1:
                    A[r][c] += A[r + 1][c]
                elif c < len(A[0]) - 1:
                    A[r][c] += A[r][c + 1]

        return A[0][0]
