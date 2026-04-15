from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for n in range(len(t) + 1):
            dp[0][n] = 0
        for m in range(len(s) + 1):
            dp[m][0] = 1 
        
        for m in range(1, len(s) + 1):
            for n in range(1, len(t) + 1):
                dp[m][n] = dp[m - 1][n]
                if s[m - 1] == t[n - 1]:
                    dp[m][n] += dp[m-1][n-1]
        
        return dp[-1][-1]
    
        