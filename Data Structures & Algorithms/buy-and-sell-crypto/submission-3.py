class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        max_pro = 0
        for price in prices:
            if price < smallest:
                smallest = price
            max_pro = max(max_pro, price-smallest)
        return max_pro
            
        