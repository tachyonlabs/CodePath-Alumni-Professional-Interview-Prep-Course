import math

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        return math.factorial(2 * A) / (math.factorial(A) * math.factorial(A + 1))
