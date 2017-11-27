import re

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        return 1 if A and re.search("^-{0,1}\d*((\.\d+){0,1}(e-{0,1}\d+){0,1})$", A) else 0
