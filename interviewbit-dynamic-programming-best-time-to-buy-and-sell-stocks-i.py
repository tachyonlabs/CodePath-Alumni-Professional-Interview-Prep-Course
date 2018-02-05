class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A or len(A) < 2:
            return 0

        max_so_far = max_ending_here = A[1] - A[0]
        for i in range(2, len(A)):
            max_ending_here = max(max_ending_here + A[i] - A[i - 1], A[i] - A[i - 1])
            max_so_far = max(max_so_far, max_ending_here)

        return max(max_so_far, 0)
