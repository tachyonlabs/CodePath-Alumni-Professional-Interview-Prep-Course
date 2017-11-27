class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_ending_here = max_so_far = A[0]
        for ele in A[1:]:
            max_ending_here = max(max_ending_here + ele, ele)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
