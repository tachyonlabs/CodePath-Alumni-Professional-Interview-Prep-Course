class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        largest = -1
        sorted_A = sorted([[x, i] for i, x in enumerate(A)])
        indices = [x[1] for x in sorted_A]
        indexmax = [indices[-1]]
        for i in range(len(indices) - 2, -1, -1):
            indexmax.append(max(indexmax[-1], indices[i]))

        indexmax.reverse()

        for i in range(len(A)):
            largest = max(largest, indexmax[i] - indices[i])

        return largest
