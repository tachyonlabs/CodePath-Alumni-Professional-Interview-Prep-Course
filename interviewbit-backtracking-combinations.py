class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        combos = [[]]
        for i in range(k):
            new_combos = []
            for combo in combos:
                for num in range(combo[-1] + 1 if combo else 1, n + 1):
                    new_combos.append(combo + [num])

            combos = new_combos[:]

        return combos
