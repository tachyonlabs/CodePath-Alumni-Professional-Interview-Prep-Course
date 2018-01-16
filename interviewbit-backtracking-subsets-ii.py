class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        subsets = {(): 1}
        if A:
            A.sort()
            for num in A:
                for sub in subsets.keys():
                    subsets[sub + (num,)] = 1

        return sorted(list(sub) for sub in subsets)
