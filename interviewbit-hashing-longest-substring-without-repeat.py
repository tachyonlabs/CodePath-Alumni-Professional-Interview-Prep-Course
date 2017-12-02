class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if len(A) <= 1:
            return len(A)

        current = ""
        longest = 0
        letters = {}
        for i, letter in enumerate(A):
            if letter not in letters:
                current += letter
            else:
                for j in range(current.index(letter)):
                    del letters[current[j]]
                current = A[letters[letter] + 1:i + 1]
            longest = max(longest, len(current))
            letters[letter] = i

        return longest
