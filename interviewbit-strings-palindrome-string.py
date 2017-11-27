import re

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = re.sub("[^a-z\d]", "", A.lower())
        return 1 if A == A[::-1] else 0
