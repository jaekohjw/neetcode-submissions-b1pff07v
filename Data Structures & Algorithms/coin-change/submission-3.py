class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0


        for i in range(0, n):
            for target in range(1, amount + 1):
                if coins[i] > target:
                    dp[i][target] = dp[i - 1][target]
                else:
                    leave = dp[i - 1][target]
                    res = dp[i][target - coins[i]]
                    take = res + 1 if res != -1 else -1 
                    options = [x for x in [take, leave] if x != -1]  # Bug 4 fixed
                    dp[i][target] = min(options) if options else -1

        return dp[n - 1][amount]
                 

        