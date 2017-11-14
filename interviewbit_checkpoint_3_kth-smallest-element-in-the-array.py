class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        sorted_A = sorted(A)
        return sorted_A[k - 1]
