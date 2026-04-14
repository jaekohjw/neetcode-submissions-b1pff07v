from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1, dp2 = 1, 0 

        for i in range(n - 1, -1, -1):
            cur = 0
            if s[i] != "0":
                cur += dp1
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    cur += dp2
            dp1, dp2 = cur, dp1
        
        return dp1
