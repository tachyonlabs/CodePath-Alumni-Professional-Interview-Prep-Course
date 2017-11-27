from math import log10

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        return int(int(A) > 1 and log10(int(A)) / log10(2) % 1 == 0)
