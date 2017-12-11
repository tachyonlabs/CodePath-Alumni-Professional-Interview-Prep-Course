class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
        if len(A) == B:
            return max(A)

        low = max(A)
        high = sum(A)
        while low <= high:
            mid = (low + high) / 2
            students = 1
            sump = 0
            for book in A:
                if sump + book > mid:
                    students += 1
                    sump = book
                else:
                    sump += book

            if students <= B:
                high = mid - 1
            else:
                low = mid + 1

        return low
