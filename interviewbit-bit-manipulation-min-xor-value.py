class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        min_diff = float("inf")
        for i in range(len(A) - 1):
            min_diff = min(min_diff, A[i + 1] ^ A[i])

        return min_diff
