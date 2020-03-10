class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        minPrice = prices[0]
        profit = 0
        for p in prices[1:]:
            profit = max(profit, p-minPrice)
            minPrice = min(minPrice,p)
        return profit
        