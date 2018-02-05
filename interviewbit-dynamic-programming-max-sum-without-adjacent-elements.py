class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        A[0] = [max(A[0][i], A[1][i]) for i in range(len(A[0]))]
        inclusive = exclusive = 0
        for num in A[0]:
            new_inclusive = max(inclusive, exclusive + num)
            exclusive = max(exclusive, inclusive)
            inclusive = new_inclusive

        return max(inclusive, exclusive)
