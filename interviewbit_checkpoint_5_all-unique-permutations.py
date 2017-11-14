class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def heaps_algorithm(length, data, permutations):
            # heap's algorithm is what I've used previously when not using itertools.permutations
            if length == 1:
                permutations[tuple(data)] = 1
            else:
                for i in range(length):
                    heaps_algorithm(length - 1, data, permutations)
                    if length % 2:
                        data[0], data[length - 1] = data[length - 1], data[0]
                    else:
                        data[i], data[length - 1] = data[length - 1], data[i]

            return permutations

        return [list(perm) for perm in heaps_algorithm(len(A), A, {})]
