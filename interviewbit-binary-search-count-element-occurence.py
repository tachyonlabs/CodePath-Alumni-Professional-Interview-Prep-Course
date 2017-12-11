class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == B:
                count = 1
                i = mid - 1
                while i >= 0 and A[i] == B:
                    count += 1
                    i -= 1
                i = mid + 1
                while i < len(A) and A[i] == B:
                    count += 1
                    i += 1
                return count
            elif A[mid] < B:
                start = mid + 1
            elif A[mid] > B:
                end = mid - 1

        return 0
