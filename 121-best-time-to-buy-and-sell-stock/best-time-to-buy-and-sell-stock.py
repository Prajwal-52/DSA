class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=float("inf")
        max_profit=0
        for i in range(0,n):
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i] - min_price > max_profit:
                max_profit=prices[i] - min_price
        return max_profit
        