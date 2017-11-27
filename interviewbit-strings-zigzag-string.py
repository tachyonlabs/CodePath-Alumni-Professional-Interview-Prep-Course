class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A

        converted = [""] * B
        row = 0
        down, up = 1, -1
        direction = down
        for char in A:
            converted[row] += char
            if row == 0 and direction == up:
                direction = down
            elif row == B - 1:
                direction = up

            row += direction

        return "".join(converted)
