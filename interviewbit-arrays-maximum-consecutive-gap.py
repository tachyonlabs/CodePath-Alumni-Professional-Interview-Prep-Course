class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        sorted_A = sorted(list(A))
        max_gap = 0
        for i in range(len(A) - 1):
            max_gap = max(max_gap, sorted_A[i + 1] - sorted_A[i])

        return max_gap
