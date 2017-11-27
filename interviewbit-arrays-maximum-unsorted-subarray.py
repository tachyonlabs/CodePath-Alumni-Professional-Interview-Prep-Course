class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        sortedA = sorted(A)
        start = -1
        for i in range(len(A)):
            if A[i] != sortedA[i]:
                if start == -1:
                    start = i
                else:
                    end = i

        return [start, end] if start != -1 else [-1]
