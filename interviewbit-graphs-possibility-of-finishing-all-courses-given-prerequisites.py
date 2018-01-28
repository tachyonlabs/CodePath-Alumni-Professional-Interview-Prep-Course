class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def is_cycle(self, num):
        if num in self.black:
            return False
        if num in self.gray:
            return True
        del self.white[num]
        self.gray[num] = 1
        return any([self.is_cycle(n) for n in self.course_list[num]])

    def solve(self, A, B, C):
        self.white = {i: 1 for i in range(1, A + 1)}
        self.gray = {}
        self.black = {}
        self.course_list = [[] for i in range(A + 1)]
        for i in range(len(B)):
            self.course_list[C[i]].append(B[i])

        for i in range(1, A + 1):
            if self.is_cycle(i):
                return 0
            else:
                keys = self.gray.keys()
                for key in keys:
                    del self.gray[key]
                    self.black[key] = 1

        return 1
