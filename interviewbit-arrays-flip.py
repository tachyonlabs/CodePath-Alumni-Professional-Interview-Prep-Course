class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if not "0" in A:
            return []

        nums = [-1 if d == "1" else 1 for d in A]
        max_starting_here = max_so_far = start = end = float("-inf")
        max_start = max_end = 0
        for i, num in enumerate(nums):
            if num > max_starting_here + num:
                start = i
                end = i
                max_starting_here = num
            else:
                max_starting_here += num
                end += 1

            if max_starting_here > max_so_far:
                max_start = start
                max_end = end
                max_so_far = max_starting_here

        return [max_start + 1, max_end + 1]
