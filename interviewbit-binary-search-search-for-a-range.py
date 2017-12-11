class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def find_border(side, start, end):
            while start <= end:
                mid = (start + end) / 2
                if (side == left and A[mid] == B and (mid == 0 or A[mid - 1] < B)) or (side == right and A[mid] == B and (mid == len(A) - 1 or A[mid + 1] > B)):
                    return mid
                elif side == left and A[mid] >= B:
                    end = mid - 1
                elif side == left and A[mid] < B:
                    start = mid + 1
                elif side == right and A[mid] > B:
                    end = mid - 1
                elif side == right and A[mid] <= B:
                    start = mid + 1

            return -1


        left = True
        right = False
        left_border = find_border(left, 0, len(A) - 1)
        if left_border == -1:
            return [-1, -1]

        right_border = find_border(right, left_border, len(A) - 1)

        return [left_border, right_border]
