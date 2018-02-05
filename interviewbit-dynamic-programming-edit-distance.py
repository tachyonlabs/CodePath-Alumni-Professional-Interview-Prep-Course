class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp_table = []
        dp_table.append([i for i in range(len(A) + 1)])
        for i in range(1, len(B) + 1):
            dp_table.append([i] + [0] * len(A))

        A, B = " " + A, " " + B

        for b in range(1, len(B)):
            for a in range(1, len(A)):
                if A[a] != B[b]:
                    dp_table[b][a] = min(dp_table[b][a - 1], dp_table[b - 1][a], dp_table[b - 1][a - 1]) + 1
                else:
                    dp_table[b][a] = dp_table[b - 1][a - 1]

        return dp_table[-1][-1]
