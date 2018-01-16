class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if not A:
            return 0

        if B == 0:
            return 1
        elif B % 2:
            return ((A % C) * self.Mod(A, B - 1, C)) % C
        else:
            x = self.Mod(A, B / 2, C)
            return x ** 2 % C
