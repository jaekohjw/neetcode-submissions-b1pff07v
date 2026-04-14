class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = - prices[0]
        sold = 0
        free = 0
    
        for i in range(1, len(prices)):
            prev_held = held
            prev_sold = sold
            prev_free = free

            held = max(prev_held, prev_free - prices[i])
            sold = prev_held + prices[i]
            free = max(prev_free, prev_sold)
        
        return max(sold, free)




        