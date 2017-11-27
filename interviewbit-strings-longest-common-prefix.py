class Solution:
    # @param A : list of strings
    # @return a strings
    def check_letter(self, arr, i):
        c = arr[0][i]
        for s in arr[1:]:
            if i == len(s) or c != s[i]:
                return False

        return True

    def longestCommonPrefix(self, A):
        for j in range(len(A[0])):
            if not self.check_letter(A, j):
                return A[0][:j]

        return A[0]
