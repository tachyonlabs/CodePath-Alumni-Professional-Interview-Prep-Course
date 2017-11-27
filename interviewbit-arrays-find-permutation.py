class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        """
        Just walk through an array of size B increasing or decreasing numbers as necessary,
        keeping track of the current largest and smallest numbers, and then make a pass
        over the array adding (1 - smallest) to each number so they'll all be positive. I
        would have gotten more points and a faster time except that InterviewBit kept
        giving me a "Internal Error. We are working on fixing this issue ASAP" when I
        would click Submit.
        """
        smallest = largest = 1
        results = [1] * B
        for i, c in enumerate(A):
            if c == "I":
                results[i + 1] = largest + 1
                largest += 1
            else:
                results[i + 1] = smallest - 1
                smallest -= 1

        return [num + (1 - smallest) for num in results]
