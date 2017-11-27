class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A.insert(0, 0)
        for i in range(len(A) - 1, -1, -1):
            if A[i] < 9:
                A[i] += 1
                break
            else:
                A[i] = 0

        start = 0
        while A[start] == 0:
            start += 1

        return A[start:]
