class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        min_word_len = float("inf")
        max_word_len = float("-inf")
        dictionary = {}
        # putting the words in a hash for faster lookups, plus getting min and max word length
        # so we don't waste time looking up substrings that are too small or too large
        for word in B:
            dictionary[word] = 1
            min_word_len = min(min_word_len, len(word))
            max_word_len = max(max_word_len, len(word))

        # to keep track of positions where the substring to the left can be successfully divided into words
        we_can_do_it_to_here = [False] * (len(A) + 1)
        we_can_do_it_to_here[0] = True

        for i in range(min_word_len, len(A) + 1):
            for j in range(max(0, i - max_word_len), i - min_word_len + 1):
                if we_can_do_it_to_here[j] and A[j:i] in dictionary:
                    we_can_do_it_to_here[i] = True
                    break

        return int(we_can_do_it_to_here[-1])
