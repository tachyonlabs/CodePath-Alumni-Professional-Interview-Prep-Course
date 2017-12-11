class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if len(A) == 1:
            return A[0]
        if A[-1] > A[0]:
            return A[0]

        start = 0
        end = len(A) - 2
        while start <= end:
            mid = (start + end) / 2
            print A[mid:mid + 2]
            if A[mid] > A[mid + 1]:
                return A[mid + 1]
            elif A[mid] > A[start]:
                start = mid + 1
            else:
                end = mid
