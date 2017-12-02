class Solution:
    # @param S : string
    # @param T : string
    # @return a string
    def minWindow(self, S, T):
        shortest = ""
        if S and T and len(T) <= len(S):
            letters = list(T)
            counts_needed = {}
            for c in T:
                counts_needed[c] = counts_needed.get(c, 0) + 1
            curr_counts = {c: 0 for c in T}
            start = None
            end = 0

            while end < len(S):
                c = S[end]
                if c in curr_counts:
                    if start == None:
                        start = end
                    curr_counts[c] += 1
                    if letters:
                        if c in letters:
                            letters.remove(c)
                    if not letters:
                        if not shortest:
                            shortest = S[start:end + 1]
                        while curr_counts[S[start]] > counts_needed[S[start]]:
                            curr_counts[S[start]] -= 1
                            start += 1
                            while S[start] not in curr_counts:
                                start += 1

                        if end - start + 1 < len(shortest):
                            shortest = S[start:end + 1]

                end += 1

        return shortest
