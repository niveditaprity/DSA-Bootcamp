class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = max(prices)
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
            profit = max(profit, prices[i] - minPrice)
        return profit