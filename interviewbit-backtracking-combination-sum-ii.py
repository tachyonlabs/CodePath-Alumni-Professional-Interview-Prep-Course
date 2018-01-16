class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        """
        This wss one of those ones where I do a first solution to check for correctness,
        expecting that InterviewBit will fail it for efficiency, and that after that I
        will work on optimizing it/coming up with a more efficient approach, but instead
        it passes just fine.
        """
        combo_sums = []
        combos = [[]]
        A = sorted([x for x in A if x <= B])
        for num in A:
            temp = []
            for combo in combos:
                new_combo = combo + [num]
                total = sum(new_combo)
                if total == B and new_combo not in combo_sums:
                    combo_sums.append(new_combo)
                elif total < B:
                    temp.append(new_combo)
            combos += temp

        return combo_sums
