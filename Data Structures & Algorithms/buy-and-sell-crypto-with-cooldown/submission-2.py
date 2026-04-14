class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        Held = [0] * n
        Sold = [0] * n
        Free = [0] * n
        Held[0] = - prices[0]

        for i in range(1, n):
            Held[i] = max(Held[i - 1], Free[i - 1] - prices[i])
            Sold[i] = Held[i - 1] + prices[i]
            Free[i] = max(Free[i - 1], Sold[i - 1])
        
        return max(Held[n - 1], Sold[n - 1], Free[n - 1])




        