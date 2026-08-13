class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        total = 0
        for r, price in enumerate(prices):
            while price < prices[l]:
                l += 1
            total = max(total, price - prices[l])
        return total


        