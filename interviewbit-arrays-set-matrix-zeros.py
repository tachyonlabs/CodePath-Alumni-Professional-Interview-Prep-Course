class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        zero_rows = {}
        zero_cols = {}
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 0:
                    zero_rows[row] = 1
                    zero_cols[col] = 1

        for row in zero_rows:
            A[row] = [0] * len(A[0])

        for col in zero_cols:
            for row in range(len(A)):
                A[row][col] = 0

        return A
