from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def ED(m, n):
            if m < 0:
                return n + 1
            if n < 0:
                return m + 1

            return min(
                ED(m, n - 1) + 1,
                ED(m - 1, n) + 1,
                ED(m - 1, n - 1) + (0 if word1[m] == word2[n] else 1)
            )
        
        return ED(len(word1) - 1, len(word2) - 1)