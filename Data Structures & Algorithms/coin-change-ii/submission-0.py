class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def numWays(i, target):
            if i < 0:
                return 0
            if target == 0:
                return 1
            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = numWays(i - 1, target)
            if coins[i] <= target:
                memo[(i, target)] += numWays(i, target - coins[i])
            return memo[(i, target)]
        
        return numWays(len(coins) - 1, amount)

            
        