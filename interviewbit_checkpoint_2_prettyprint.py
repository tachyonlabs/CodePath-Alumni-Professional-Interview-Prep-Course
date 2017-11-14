class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        pp = [[1]]
        for i in range(2, A + 1):
            for j in range(len(pp)):
                pp[j] = [i] + pp[j] + [i]
            pp.insert(0, [i] * (2 * i - 1))
            pp.append([i] * (2 * i - 1))

        return pp
