class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        """
        This was simplified by the constraint that you can only add characters to the beginning of
        the string, so I'm just checking is the whole string a palindrome, is the string length - 1
        a palindrome, and so on, with the characters needed being string length - palindrome length
        """
        def is_pal(s):
            if len(s) <= 1:
                return True
            else:
                return s[0] == s[-1] and is_pal(s[1:-1])

        if len(A) <= 1:
            return 0

        for i in range(len(A), 0, -1):
            if is_pal(A[:i]):
                return len(A) - i
