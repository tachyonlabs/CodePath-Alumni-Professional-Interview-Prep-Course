class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        counts = {}
        for num in A:
            if num in counts:
                del counts[num]
            else:
                counts[num] = 1

        for key in counts:
            return key
