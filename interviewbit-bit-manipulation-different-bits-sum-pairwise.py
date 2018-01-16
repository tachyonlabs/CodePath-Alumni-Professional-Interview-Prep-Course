class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        bits = []
        for i in range(32):
            bit = 0
            for num in A:
                if num & 2 ** i:
                    bit += 1

            bits.append(bit)

        return sum((len(A) - bit) * bit * 2 for bit in bits) % (10 ** 9 + 7)
