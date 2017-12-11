import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        size = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)
        heap = []
        for anum in A:
            for bnum in B:
                pair_sum = anum + bnum
                if len(heap) < size:
                    heapq.heappush(heap, pair_sum)
                else:
                    if pair_sum > heap[0]:
                        heapq.heappushpop(heap, pair_sum)
                    else:
                        break

        return sorted(list(heap), reverse=True)
