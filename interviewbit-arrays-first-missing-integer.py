class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = [num if num >= 0 and num <= len(A) else 0 for num in A]
        i = 0
        while i < len(A) - 1:
            if A[i] != 0 and A[i] != i + 1:
                if A[i] == A[A[i] - 1]:
                    i += 1
                else:
                    temp = A[i]
                    A[i] = A[temp - 1]
                    A[temp - 1] = temp
            else:
                i += 1

        for i, num in enumerate(A):
            if num != i + 1:
                return i + 1

        return len(A) + 1
