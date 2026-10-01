class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = max(prev + nums[i], nums[i])
            m = max(m, cur)
            prev = cur
        return m

        