class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        def match(piece):
            return needle == piece

        for i in range(0, len(haystack) - len(needle) + 1):
            if match(haystack[i: i + len(needle)]):
                return i

        return -1
