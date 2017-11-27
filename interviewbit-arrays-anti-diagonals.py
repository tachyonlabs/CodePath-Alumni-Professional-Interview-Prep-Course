class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        anti_diags = []
        for i in range(len(a[0])):
            ad = []
            r, c = 0, i
            while r < len(a) and c >= 0:
                ad.append(a[r][c])
                r += 1
                c -= 1
            anti_diags.append(ad)

        for i in range(1, len(a)):
            ad = []
            r, c = i, len(a[0]) - 1
            while r < len(a) and c >= 0:
                ad.append(a[r][c])
                r += 1
                c -= 1
            anti_diags.append(ad)

        return anti_diags
