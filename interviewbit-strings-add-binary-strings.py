class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        A, B = "0" + A, "0" + B
        if len(A) > len(B):
            B = "0" * (len(A) - len(B)) + B
        elif len(B) > len(A):
            A = "0" * (len(B) - len(A)) + A

        arrA, arrB = [map(int, list(x)) for x in [A, B]]
        carry = 0
        for i in range(len(arrA) - 1, -1, -1):
            temp = arrA[i] + arrB[i] + carry
            arrA[i], carry = temp % 2, temp / 2

        return "".join(map(str, arrA)).lstrip("0")
