class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        steps = 0
        row, col = X[0], Y[0]
        for i in range(1, len(X)):
            steps += max(abs(row - X[i]), abs(col - Y[i]))
            row, col = X[i], Y[i]

        return steps
