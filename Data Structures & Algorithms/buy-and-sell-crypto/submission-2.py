class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_pro = 0
        while r < len(prices):
            while prices[r] < prices[l]:
                l += 1
            max_pro = max(max_pro, prices[r]-prices[l])
            r += 1
        return max_pro

        