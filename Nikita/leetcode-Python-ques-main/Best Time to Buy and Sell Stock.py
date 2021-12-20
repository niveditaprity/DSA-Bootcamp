class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        profit=0
        min=prices[0]
        for i in range(1,n):
            if min>prices[i]:
                min=prices[i]
            profit=max(profit,prices[i]-min)
        return profit
                
