class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        nums = {}
        for i, num in enumerate(A):
            nums[num] = nums.get(num, []) + [i]

        for i, num in enumerate(A):
            target = B - num
            if target in nums and nums[target][0] < i:
                return [nums[target][0] + 1, i + 1]

        return []
