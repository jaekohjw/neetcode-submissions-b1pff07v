from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @cache 
        def numWays(i):
            if i > len(s) - 1:
                return 1
            if i == len(s) - 1:
                return 1 if s[i] != "0" else 0
            if s[i] == "0":
                return 0 
            if int(s[i:i+2]) > 26:
                return numWays(i + 1)
            return numWays(i + 1) + numWays(i + 2)

        if len(s) == 1:
            return 1 if s[0] != "0" else 0
        return numWays(0)
