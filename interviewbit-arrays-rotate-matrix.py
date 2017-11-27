class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        top = left = 0
        bottom = right = len(A) - 1
        while top < bottom:
            for i in range(right - left):
                temp = A[top][left + i]
                A[top][left + i] = A[bottom - i][left]
                A[bottom - i][left] = A[bottom][right - i]
                A[bottom][right - i] = A[top + i][right]
                A[top + i][right] = temp

            top += 1
            left += 1
            bottom -= 1
            right -= 1

        return A
