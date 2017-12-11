class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B > len(A):
            return []

        window = {}
        for num in A[:B]:
            window[num] = window.get(num, 0) + 1

        distinct = [len(window)]
        for i in range(len(A) - B):
            remkey = A[i]
            if window[remkey] == 1:
                del window[remkey]
            else:
                window[remkey] -= 1

            addkey = A[i + B]
            window[addkey] = window.get(addkey, 0) + 1
            distinct.append(len(window))

        return distinct
