class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        num = 0
        i = 0
        multiplier = 1
        while i < len(A) and A[i] == " ":
            i += 1

        for char in A[i:]:
            if char in "0123456789":
                num = num * 10 + ord(char) - 48
            elif char == "+":
                pass
            elif char == "-":
                multiplier = -1
            else:
                break

        num *= multiplier

        if num > 0:
            return min(num, 2147483647)
        else:
            return max(num, -2147483648)
