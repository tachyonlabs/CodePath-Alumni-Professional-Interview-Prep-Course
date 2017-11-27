class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        counts = {}
        max_num = 0
        for num in A:
            if num in counts:
                repeated = num
            else:
                counts[num] = 1

        num = 1
        while True:
            if num not in counts:
                return [repeated, num]
            num += 1
