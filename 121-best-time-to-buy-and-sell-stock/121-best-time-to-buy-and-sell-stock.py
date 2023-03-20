class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        buy_day = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy_day]:
                buy_day = i
            profit = prices[i] - prices[buy_day] 
            if profit > max_profit:
                max_profit = profit
        return max_profit
