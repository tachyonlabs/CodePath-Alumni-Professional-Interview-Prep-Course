class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        if not A: return []

        justified = []
        text = " ".join(A)
        while len(text) > B:
            space = text.rfind(" ", 0, B + 1)
            words = text[0:space].split()
            i = 0
            total = space
            while total < B:
                words[i] += " "
                total += 1
                if len(words) > 1:
                    i = (i + 1) % (len(words) - 1)

            justified.append(" ".join(words))
            text = text[space + 1:]

        justified.append(text + " " * (B - len(text)))

        return justified
