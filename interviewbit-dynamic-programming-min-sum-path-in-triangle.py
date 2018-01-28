class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        if len(A) == 1:
            return A[0][0]

        print A
        for r in range(len(A) - 2, -1, -1):
            for c in range(len(A[r])):
                A[r][c] += min(A[r + 1][c], A[r + 1][c + 1])
                print A

        return A[0]
