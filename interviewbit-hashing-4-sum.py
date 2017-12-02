class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A.sort()
        pairs = {}
        solution_set = []
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                val = A[i] + A[j]
                pairs[val] = pairs.get(val, []) + [[A[i], A[j], i, j]]

        for val in pairs:
            if B - val in pairs:
                for a, b, i, j in pairs[val]:
                    for c, d, k, l in pairs[B - val]:
                        if len(set([i, j, k, l])) == 4:
                            sorted_abcd = sorted([a, b, c, d])
                            if sorted_abcd not in solution_set:
                                solution_set.append(sorted_abcd)

        return sorted(solution_set)
