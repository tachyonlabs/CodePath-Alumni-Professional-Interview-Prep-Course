class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        third = len(A) / 3
        counts = {}
        for num in A:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > third:
                return num

        return -1
