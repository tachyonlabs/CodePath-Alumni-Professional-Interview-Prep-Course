class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        min_possible = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] >= min_possible - i:
                min_possible = i
            if min_possible == 0:
                return 1

        return 0
