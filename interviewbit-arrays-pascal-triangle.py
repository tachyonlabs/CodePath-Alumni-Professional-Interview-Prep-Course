class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        triangle = [[1], [1, 1]]
        for i in range(A - 2):
            row = [1]
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])

            triangle.append(row + [1])

        return triangle[:A]

