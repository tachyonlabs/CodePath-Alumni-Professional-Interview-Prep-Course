class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        self.fibs = [0, 1]

    def climbStairs(self, A):
        while A >= len(self.fibs) - 2:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])

        return self.fibs[A + 1]
