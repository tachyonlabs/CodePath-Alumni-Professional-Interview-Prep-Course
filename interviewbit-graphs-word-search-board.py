class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def __init__(self):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.bad = {}

    def word_search(self, r, c, idx):
        if idx == len(self.word):
            return True
        if (r, c, idx) in self.bad or r < 0 or c < 0 or r >= len(self.A) or c >= len(self.A[r]):
            return False
        if self.A[r][c] != self.word[idx]:
            self.bad[(r, c, idx)] = 1
            return False
        return any(self.word_search(r + y, c + x, idx + 1) for y, x in self.directions)

    def exist(self, A, B):
        # InterviewBit is putting a space on the end of at least one test case :-(!!!
        self.word = B.strip()
        self.A = A
        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] == B[0] and self.word_search(row, col, 0):
                    return 1

        return 0
