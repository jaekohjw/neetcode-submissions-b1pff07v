class Solution:
    dp = {}
    dp[1] = 1
    dp[2] = 2
    def climbStairs(self, n: int) -> int:
        if n <= 0: 
            return 0
        else: 
            if n in self.dp:
                return self.dp[n]
            else:
                res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                self.dp[n] = res
                return res

        
