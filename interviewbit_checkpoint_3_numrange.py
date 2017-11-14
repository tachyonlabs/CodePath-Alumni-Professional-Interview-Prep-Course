class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        if not A:
            return 0

        cont_sub_count = 0
        start = end = 0
        running_total = A[start]
        while start < len(A):
            if running_total >= B and running_total <= C:
                cont_sub_count += 1
                if end < len(A) - 1:
                    end += 1
                    running_total += A[end]
                else:
                    start += 1
                    if start < len(A):
                        running_total = A[start]
                    end = start
            elif end < len(A) - 1 and running_total < B:
                end += 1
                running_total += A[end]
            else:
                start += 1
                if start < len(A):
                    running_total = A[start]
                end = start

        return cont_sub_count

sol = Solution()
print sol.numRange([10, 5, 1, 0, 2], 6, 8), "should be 3"
print sol.numRange([ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ], 99, 269), "should be 58"
print sol.numRange([ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ], 98, 290), "should be 84"
