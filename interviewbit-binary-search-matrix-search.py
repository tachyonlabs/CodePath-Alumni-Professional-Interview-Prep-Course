class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rows = len(A)
        cols = len(A[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = (start + end) / 2
            num = A[mid / rows][mid % rows]
            if num == B:
                return 1
            elif num < B:
                start = mid + 1
            elif num > b:
                end = mid - 1

        return 0

