class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if not B:
            return []
        sub_len = len(B[0])
        subs_len = sub_len * len(B)
        if len(B[0]) * len(B) > len(A):
            return []

        i = 0
        indices = []
        starting = -1
        subs = list(B)
        checking = False
        while i <= len(A) - subs_len:
            if A[i:i + sub_len] in subs:
                checking = True
                j = i
                while A[j:j + sub_len] in subs:
                    if starting == -1:
                        starting = j
                    subs.remove(A[j:j + sub_len])
                    j += sub_len

            if checking:
                if not subs:
                    indices.append(starting)
                starting = -1
                subs = list(B)
                checking = False

            i += 1

        return indices
