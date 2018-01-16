from math import log
from sys import maxint


class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        """
        It's easy to use shift for floor division by multiples of 2, but I wasn't sure how
        to do it for other divisors -- I entered this as my brute-force solution, expecting
        it to get passed for correctness but failed for time efficiency, and then after that
        I would probably get a hint and work on a more time-efficient bit-manipulation
        solution, but instead it passed just fine.
        """
        if divisor == 1: return dividend
        if abs(divisor) > abs(dividend): return 0
        # faking integer behavior in C that does not apply in Python
        if dividend == -2147483648 and divisor == -1: return 2147483647
        if dividend < 0 and divisor < 0: dividend, divisor = -dividend, -divisor

        count = 0
        while dividend >= divisor:
            dividend -= divisor
            count += 1

        return count
