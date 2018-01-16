class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        keypad = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        letter_combinations = list(keypad[int(str(A)[0])])
        for digit in str(A)[1:]:
            temp = []
            for combo in letter_combinations:
                for letter in keypad[int(digit)]:
                    temp.append(combo + letter)

            letter_combinations = temp

        return letter_combinations
