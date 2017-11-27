class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        one = [x + i for i, x in enumerate(A)]
        two = [x - i for i, x in enumerate(A)]

        return max(abs(min(one) - max(one)), abs(min(two) - max(two)))
