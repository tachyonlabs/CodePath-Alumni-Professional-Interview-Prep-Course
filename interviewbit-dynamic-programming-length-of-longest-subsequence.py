class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        inc = [1] * len(A)
        dec = inc[:]
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[j] < A[i]:
                    inc[i] = max(inc[i], inc[j] + 1)
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                if A[j] < A[i]:
                    dec[i] = max(dec[i], dec[j] + 1)

        longest = 0

        for i in range(len(A)):
            longest = max(longest, inc[i] + dec[i] - 1)

        return longest
