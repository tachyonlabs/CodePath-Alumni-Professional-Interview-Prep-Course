class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start = 0
        end = A
        while start <= end:
            mid = (start + end) / 2
            squared = mid ** 2
            if squared == A:
                return mid
            elif squared < A:
                start = mid + 1
            elif squared > A:
                end = mid - 1

        return start - 1
