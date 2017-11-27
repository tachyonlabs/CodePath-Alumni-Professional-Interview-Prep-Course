class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        last_char = len(A) - 1
        while last_char >= 0 and A[last_char] == " ":
            last_char -= 1

        for j in range(last_char, -1, -1):
            if A[j] == " ":
                return last_char - j

        return last_char + 1
