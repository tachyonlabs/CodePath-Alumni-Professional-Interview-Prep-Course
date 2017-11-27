class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        def get_row(num):
            # apparently the numbers aren't quite so big that you can't multiply one of
            # them by a single digit
            return [0] * num + map(int, list(str(int_A * B[len(B) - num - 1]))[::-1])

        int_A = int(A)
        B = map(int, list(B))
        # I'm just multiplying the first number by the digits of the second one at a time,
        # converting the temporary results to arrays of digits, and adding the columns manually
        start_row = get_row(0)
        for i in range(1, len(B)):
            next_row = get_row(i)
            carry = 0
            start_row += [0] * (len(next_row) - len(start_row)) + [0]
            next_row += [0] * (len(start_row) - len(next_row)) + [0]
            for j in range(len(start_row)):
                temp = start_row[j] + next_row[j] + carry
                start_row[j] = temp % 10
                carry = temp / 10

        # and back to a non-reversed-order string
        return "".join(map(str, start_row)).rstrip("0")[::-1] or "0"
