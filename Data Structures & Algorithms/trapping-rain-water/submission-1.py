class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l<r:
            if height[l] <= height[r]:
                l += 1
                cur_water = maxLeft-height[l] if maxLeft > height[l] else 0
                res += cur_water 
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                cur_water = maxRight-height[r] if maxRight > height[r] else 0
                res += cur_water 
                maxRight = max(maxRight, height[r])
        return res
            


        