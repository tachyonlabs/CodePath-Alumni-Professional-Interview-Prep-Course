class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        nge_stack = []
        output = []
        for num in A[::-1]:
            nge = -1
            while nge_stack:
                test_num = nge_stack.pop()
                if test_num > num:
                    nge = test_num
                    nge_stack.append(nge)
                    break

            output.append(nge)
            nge_stack.append(num)

        return output[::-1]
