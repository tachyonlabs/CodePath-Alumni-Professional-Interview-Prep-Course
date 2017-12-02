class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if not numerator:
            return "0"
        sign = ""
        if numerator < 0 and denominator < 0:
            numerator, denominator = abs(numerator), abs(denominator)
        elif numerator < 0 or denominator < 0:
            sign = "-"
            numerator, denominator = abs(numerator), abs(denominator)

        remainders = {}
        div, mod = numerator / denominator, numerator % denominator
        if mod == 0:
            return sign + str(div)
        else:
            fraction = sign + str(div) + "."
            pos = len(fraction)
            remainders[mod] = pos
        while mod != 0:
            mod *= 10
            pos += 1
            div, mod = mod / denominator, mod % denominator
            fraction += str(div)
            if mod in remainders:
                fraction = fraction[:remainders[mod]] + "(" + fraction[remainders[mod]:] + ")"
                break
            else:
                remainders[mod] = pos

        return fraction
