from collections import deque

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        dest = [F, E]
        source = [D, C]
        rows = B
        cols = A
        queue = deque([source + [0]])
        dont_check_again = [[False for c in range(cols + 1)] for r in range(rows + 1)]
        dont_check_again[D][C] = True
        while queue:
            row, col, steps = queue.popleft()
            if [row, col] == dest:
                return steps
            for y, x in directions:
                new_y, new_x = row + y, col + x
                if new_y >= 1 and new_y <= rows and new_x >= 1 and new_x <= cols and not dont_check_again[new_y][new_x]:
                    queue.append([new_y, new_x, steps + 1])
                    dont_check_again[new_y][new_x] = True

        return -1
