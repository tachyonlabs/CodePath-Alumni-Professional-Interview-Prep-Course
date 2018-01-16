class Solution:
    # @param A : integer
    # @return a list of strings
    def all_parens(self, n, s="", opens=1, closes=0):
        if len(s) == n * 2:
            self.parens.append(s)
        else:
            if opens < n:
                self.all_parens(n, s + "(", opens + 1, closes)
            if closes < opens:
                self.all_parens(n, s + ")", opens, closes + 1)

    def generateParenthesis(self, A):
        if A == 0:
            return []

        self.parens = []
        self.all_parens(A, "(")
        return self.parens
