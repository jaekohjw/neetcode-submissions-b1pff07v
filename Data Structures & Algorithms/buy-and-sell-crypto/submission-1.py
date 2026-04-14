class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 1 

        while j <= len(prices) - 1:
            profit = prices[j] - prices[i]
            print(j)
            if profit < 0: 
                i = j
            elif (profit > max_profit):
                max_profit = profit
            j = j + 1
        
        return max_profit



        