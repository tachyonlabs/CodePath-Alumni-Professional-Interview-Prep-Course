class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A, B = map(int, A.split(".")), map(int, B.split("."))
        if len(A) < len(B):
            A += [0] * (len(B) - len(A))
        elif len(A) > len(B):
            B += [0] * (len(A) - len(B))

        for i in range(len(A)):
            if A[i] > B[i]:
                return 1
            if A[i] < B[i]:
                return -1

        return 0
