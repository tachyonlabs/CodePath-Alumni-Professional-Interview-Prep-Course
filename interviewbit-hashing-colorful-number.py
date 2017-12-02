class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        def mul_digits(str_num):
            return reduce(lambda x, y: x * y, [int(d) for d in str_num])

        products = {}
        str_A = str(A)
        for i in range(1, len(str_A) + 1):
            for j in range(0, len(str_A) - i + 1):
                product = mul_digits(str_A[j:j + i])
                print str_A[j:j + i], product
                if product in products:
                    return 0
                products[product] = 1

        return 1
