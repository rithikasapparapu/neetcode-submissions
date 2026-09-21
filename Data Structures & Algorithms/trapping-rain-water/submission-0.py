class Solution:
    def trap(self, height: List[int]) -> int:
        # [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
        # [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
        # [0, 0, 2, 0, 2, 3, 2, 0, 0, 0]
        right = [0]*len(height)
        val_right = float('-inf')
        for i in range(len(height)-1, -1, -1):
            val_right = max(val_right, height[i])
            right[i] = val_right
        res = 0
        left = float('-inf')
        for i in range(len(height)):
            left = max(left, height[i])
            water = min(left, right[i]) - height[i] if min(left, right[i]) > height[i] else 0
            res += water
        return res







        