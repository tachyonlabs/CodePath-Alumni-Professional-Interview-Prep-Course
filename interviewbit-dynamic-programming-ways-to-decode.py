import re

class Solution:
    # @param A : string
    # @return an integer
    def count_decodings(self, A, i):
        if i >= len(A) - 1:
            return 1
        if self.counts[i] != -1:
            return self.counts[i]
        if A[i + 1] == "0":
            count = self.count_decodings(A, i + 2)
        elif A[i] > "2" or (A[i] == "2" and A[i + 1] > "6") or (i <= len(A) - 3 and A[i + 2] == "0"):
            count = self.count_decodings(A, i + 1)
        else:
            count = self.count_decodings(A, i + 1) + self.count_decodings(A, i + 2)

        self.counts[i] = count
        return count

    def numDecodings(self, A):
        if A[0] == "0" or re.search("[0,3-9]0", A):
            return 0

        self.counts = [-1] * len(A)
        return self.count_decodings(A, 0)
