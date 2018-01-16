class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        counts = {}
        for num in A:
            counts[num] = counts.get(num, 0) + 1

        for num in A:
            if counts[num] == 1:
                return num
