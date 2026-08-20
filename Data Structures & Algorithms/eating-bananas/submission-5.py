class Solution:
    def isfeasible(self, piles, h, k):
        res = 0
        for pile in piles:
            quo = (pile//k)
            rem = pile%k
            if rem: res += quo + 1
            else: res += quo
        return res <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            if self.isfeasible(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l
        

        