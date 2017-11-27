class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        subs = []
        sub = []
        sub_start = -1

        for i, num in enumerate(A):
            if num >= 0:
                if sub_start == -1:
                    sub_start = i
                sub.append(num)
            else:
                if sub:
                    subs.append([sub, sub_start])
                    sub = []
                    sub_start = -1

        if sub:
            subs.append([sub, sub_start])

        subs.sort(key=lambda x: (-sum(x[0]), -len(x[0]), x[1]))
        return subs[0][0] if subs else []
