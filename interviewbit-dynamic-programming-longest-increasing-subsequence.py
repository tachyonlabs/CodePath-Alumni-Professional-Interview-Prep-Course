class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        counts = [1] * len(A)
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[j] < A[i]:
                    counts[i] = max(counts[i], counts[j] + 1)

        return max(counts)
