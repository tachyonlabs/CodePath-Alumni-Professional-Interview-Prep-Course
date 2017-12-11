class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0 or d == 1:
            return 0

        if n == 0:
            return 1
        elif n % 2:
            return ((x % d) * self.pow(x, n - 1, d)) % d
        else:
            y = self.pow(x, n / 2, d)
            return y ** 2 % d
