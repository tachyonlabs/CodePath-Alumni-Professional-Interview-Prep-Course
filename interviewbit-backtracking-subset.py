class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        subsets = [[]]
        for num in A:
            subsets += [sub + [num] for sub in subsets]

        return sorted(subsets)
