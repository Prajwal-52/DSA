class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_prices = float('inf')
        max_profit = 0
        for i in range(0,n):
            if prices[i] < min_prices:
                min_prices = prices[i]
            if prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices
        return max_profit
        