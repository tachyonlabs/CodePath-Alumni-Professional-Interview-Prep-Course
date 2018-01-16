class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        digits = [x for x in map(int, list(bin(A)[2:]))][::-1]
        digits += [0] * (32 - len(digits))
        return int("".join(map(str, digits)), 2)
