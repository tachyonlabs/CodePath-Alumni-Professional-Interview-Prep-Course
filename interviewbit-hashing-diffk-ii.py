class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 2:
            return 0

        nums = {A[0]: 1}
        for num in A[1:]:
            if num - B in nums or num + B in nums:
                return 1
            else:
                nums[num] = 1

        return 0
