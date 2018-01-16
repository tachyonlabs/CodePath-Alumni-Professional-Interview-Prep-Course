class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        # using Heap's algorithm (I had to look at my code from one of the previous times I've used it)
        def heaps(length, data, permutations):
            if length == 1:
                permutations.append(data[:])
            else:
                for i in range(length):
                    heaps(length - 1, data, permutations)
                    if length % 2:
                        data[0], data[length - 1] = data[length - 1], data[0]
                    else:
                        data[i], data[length - 1] = data[length - 1], data[i]

            return permutations

        return heaps(len(A), A, [])
