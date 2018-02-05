class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A or len(A) < 2:
            return 0

        maxes = [[0 for i in range(len(A))] for j in range(2)]

        # modified Kadane's
        maxes[0][1] = max_ending_here = max_so_far = A[1] - A[0]
        for i in range(2, len(A)):
            max_ending_here = max(max_ending_here + A[i] - A[i - 1], A[i] - A[i -1])
            max_so_far = max(max_so_far, max_ending_here)
            maxes[0][i] = max_so_far

        if maxes[0][-1] <= 0:
            return 0

        if len(A) < 4:
            return maxes[0][-1]

        max_diff = -A[0]

        for i in range(1, len(A)):
            max_for_one_or_two = max(maxes[1][i - 1], A[i] + max_diff)
            maxes[1][i] = max_for_one_or_two
            max_diff = max(max_diff, maxes[0][i] - A[i])

        # a workaround for some kind of bug I still have, maxes[1][-1] should be enough :-(
        return max(maxes[0][-1], maxes[1][-1])
