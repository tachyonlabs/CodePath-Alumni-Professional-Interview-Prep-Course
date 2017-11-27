class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        codebook = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
                    [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        roman_numeral = ""
        for decimal, roman in codebook:
            while A >= decimal:
                roman_numeral += roman
                A -= decimal

        return roman_numeral
