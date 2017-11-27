class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        greater = 0
        if A[-1] == 0:
            return 1

        for i in range(len(A) - 2, -1, -1):
            if A[i + 1] > A[i]:
                greater = len(A) - i - 1
            if A[i] == greater:
                return 1

        return -1
