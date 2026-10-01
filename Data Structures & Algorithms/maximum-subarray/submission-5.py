class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            m = max(m, cur)
        return m

        