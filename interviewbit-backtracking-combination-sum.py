class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def get_sets(s):
            sum_s = sum(s)
            if sum_s == B:
                s_list = sorted(list(s))
                if s_list not in sol_sets:
                    sol_sets.append(s_list)
            else:
                for n in A:
                    if sum_s + n <= B:
                        get_sets(s + (n,))

        A.sort()
        sol_sets = []
        for num in A:
            get_sets((num,))
        return sol_sets
