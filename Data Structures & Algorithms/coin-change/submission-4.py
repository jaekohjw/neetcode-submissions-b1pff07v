class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for target in range(c, amount + 1):
                dp[target] = min(dp[target], dp[target - c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

        