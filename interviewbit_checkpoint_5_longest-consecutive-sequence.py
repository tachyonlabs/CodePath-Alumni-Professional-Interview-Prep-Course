class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hash_A = {num: True for num in A}
        longest_con_seq = 0

        for num in hash_A:
            if hash_A[num]:
                length = 1
                hash_A[num] = False

                higher = num + 1
                while higher in hash_A:
                    length += 1
                    hash_A[higher] = False
                    higher += 1

                lower = num - 1
                while lower in hash_A:
                    length += 1
                    hash_A[lower] = False
                    lower -= 1

                longest_con_seq = max(longest_con_seq, length)

        return longest_con_seq
