class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        return " ".join(A.strip().split()[::-1])
    