class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        words = {}
        for i, word in enumerate(A):
            sword = "".join(sorted(list(word)))
            words[sword] = words.get(sword, []) + [i + 1]

        return sorted(words[k] for k in words)
