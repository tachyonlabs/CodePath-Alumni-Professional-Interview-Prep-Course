class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        def check_nine(nine):
            nums = {}
            for num in nine:
                if num != ".":
                    if num in nums:
                        return False
                    else:
                        nums[num] = 1

            return True

        # rows
        for row in A:
            if not check_nine(row):
                return False

        # columns
        for c in range(9):
            column = []
            for r in range(9):
                column.append(A[r][c])

            if not check_nine(column):
                return False

        # sub-boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub_box = A[r][c:c + 3] + A[r + 1][c:c + 3] + A[r + 2][c:c + 3]
                if not check_nine(sub_box):
                    return False

        return True
