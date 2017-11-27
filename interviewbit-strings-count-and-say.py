# see https://www.interviewbit.com/problems/count-and-say/

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        seq = ["1"]
        for i in range(A - 1):
            temp_seq = []
            group = seq[0]
            count = 1
            for digit in seq[1:]:
                if digit == group:
                    count += 1
                else:
                    temp_seq += [str(count), group]
                    group = digit
                    count = 1

            temp_seq += [str(count), group]

            seq = temp_seq[:]

        return "".join(seq)
