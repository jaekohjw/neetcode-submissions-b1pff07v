class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        def numWays(i, target):
            if i < 0:
                return 0
            if target == 0:
                return 1
            if dp[i][target] != -1:
                return dp[i][target]

            dp[i][target] = numWays(i - 1, target)
            if coins[i] <= target:
                dp[i][target] += numWays(i, target - coins[i])
            return dp[i][target]
        
        return numWays(len(coins) - 1, amount)
            
        