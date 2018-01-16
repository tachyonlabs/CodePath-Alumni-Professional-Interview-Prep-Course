class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        # maybe this should be in bit manipulation instead
        return [num ^ (num >> 1) for num in range(2**A)]
