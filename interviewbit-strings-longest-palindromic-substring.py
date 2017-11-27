class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        def get_pal(s, f):
            while s >= 0 and f < len(A) and A[s] == A[f]:
                pal = A[s:f + 1]
                s -= 1
                f += 1

            return pal if len(pal) > len(longest) else longest

        longest = A[0]
        i = 0
        while len(A) - i >= len(longest) / 2:
            if i < len(A) - 1 and A[i] == A[i + 1]:
                longest = get_pal(i, i + 1)

            if i < len(A) - 2 and A[i] == A[i + 2]:
                longest = get_pal(i, i + 2)

            i += 1

        return longest
