from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def lcs(s1, s2, m, n):

            if m < 0 or n < 0:
                return 0
            
            if s1[m] == s2[n]:
                return 1 + lcs(s1, s2, m - 1, n - 1)
            
            return max(lcs(s1, s2, m - 1, n), lcs(s1, s2, m, n - 1))

        return lcs(text1, text2, len(text1) - 1, len(text2) - 1)
        