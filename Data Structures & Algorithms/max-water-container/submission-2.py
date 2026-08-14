class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            maxarea = max(maxarea, (j-i)*min(heights[i], heights[j]))
            if heights[i] == min(heights[i], heights[j]):
                i += 1
            elif heights[j] == min(heights[i], heights[j]):
                j -= 1
        return maxarea

        