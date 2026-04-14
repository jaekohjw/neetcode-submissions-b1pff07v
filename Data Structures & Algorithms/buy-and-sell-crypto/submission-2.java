class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int curProfit = 0;
        int buyDay = 0;
        int sellDay = 1;

        while (sellDay < prices.length) {
            curProfit = prices[sellDay] - prices[buyDay];
            if (curProfit > maxProfit) {
                maxProfit = curProfit;
            }
            else if (curProfit < 0) {
                buyDay = sellDay;
            }
            sellDay = sellDay + 1;
        }

        return maxProfit;
    }
}
