class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        codebook = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40],
                    ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        integer = 0
        i = 0
        for roman, dec in codebook:
            while A[i:].startswith(roman):
                integer += dec
                i += len(roman)
                if i == len(A):
                    break

            if i == len(A):
                break

        return integer
