class Solution:
    def is_pal(self, strng):
        return strng == strng[::-1]

    def get_pals(self, s, i, pal):
        if i == len(s):
            self.pals.append(pal)
        for j in range(i + 1, len(s) + 1):
            print s[i:j]
            if self.is_pal(s[i:j]):
                self.get_pals(s, j, pal + (s[i:j],))

    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        self.pals = []
        self.get_pals(A, 0, ())
        return self.pals
