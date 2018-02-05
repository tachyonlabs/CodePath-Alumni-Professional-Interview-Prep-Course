class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        max_p = 0
        own = False
        bought_price = None
        for i in range(len(A)):
            if not own and i != len(A) - 1 and A[i + 1] > A[i]:
                own = True
                bought_price = A[i]
            elif own and (i == len(A) - 1 or A[i + 1] < A[i]):
                own = False
                max_p += A[i] - bought_price

        return max_p
