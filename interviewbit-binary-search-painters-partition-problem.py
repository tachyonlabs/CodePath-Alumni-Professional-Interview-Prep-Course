class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        if not C:
            return 0

        low, high = max(C) * B, sum(C) * B

        if len(C) <= A:
            return low % 10000003

        if A == 1:
            return high % 10000003

        while low <= high:
            med = (low + high) / 2
            painter = 1
            boards = 0
            for board in C:
                if boards + board * B <= med:
                    boards += board * B
                else:
                    painter += 1
                    boards = board * B

            if painter <= A:
                high = med - 1
            else:
                low = med + 1

        return low % 10000003
