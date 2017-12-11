import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        """
        Python's heapq data structure is a minheap, so I had to put the values in as value * -1,
        and then just convert back and forth when popping/pushing from/to the heap.
        """
        heap = [-num for num in B]
        heapq.heapify(heap)
        total = 0
        for time in range(A):
            if not heap:
                # if all the chocolates are already gone, or were never there, no more time needed
                break
            candies = -heapq.heappop(heap)
            total += candies
            heapq.heappush(heap, -(candies / 2))

        return total % 1000000007
