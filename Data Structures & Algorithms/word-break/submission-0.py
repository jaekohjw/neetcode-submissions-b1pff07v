class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[-1] * (n + 1) for i in range(n + 1)]
        
        def helper(i, j):
            if i == j:
                return False
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i:j] in wordDict:
                dp[i][j] = True
                return dp[i][j] 

            res = False
            for k in range(i, j):
                if helper(i, k) and helper(k, j):
                    res = True
                    break
            
            dp[i][j] = res
            return res

        return helper(0, len(s))
