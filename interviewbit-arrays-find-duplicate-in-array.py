class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        counts = {}
        for num in A:
            if num in counts:
                return num
            else:
                counts[num] = 1

        return -1
