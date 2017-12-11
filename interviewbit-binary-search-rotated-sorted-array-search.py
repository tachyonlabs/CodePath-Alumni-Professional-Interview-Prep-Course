class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        def find_pivot():
            low, high = 1, len(A) - 1
            while low <= high:
                mid = (low + high) / 2
                if A[mid - 1] > A[mid]:
                    return mid
                if A[mid] > A[0]:
                    low = mid + 1
                else:
                    high = mid - 1

        if not A:
            return -1

        if len(A) == 1:
            return 0 if A[0] == B else -1

        low, high = 0, len(A) - 1
        if A[0] > A[-1]:
            pivot = find_pivot()
            if B >= A[0]:
                low, high = 0, pivot - 1
            else:
                low, high = pivot, len(A) - 1

        while low <= high:
            mid = (low + high) / 2
            if A[mid] == B:
                return mid
            if A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1

        return -1
