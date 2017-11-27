class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        elif A == 1:
            return [1, 1]
        else:
            row = [1, 1]
            for i in xrange(A - 1):
                temp_row = [1]
                for j in xrange(len(row) - 1):
                    temp_row.append(row[j] + row[j + 1])

                row = temp_row + [1]
            return row

