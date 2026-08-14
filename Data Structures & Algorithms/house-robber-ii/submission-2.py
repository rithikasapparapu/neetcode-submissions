class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        nums1 = nums[0:len(nums)-1]
        nums2 = nums[1:len(nums)]

        dp = [0] * len(nums1)
        dp[0] = nums1[0]
        dp[1] = max(nums1[0], nums1[1])
        for i in range(2, len(nums1)):
            dp[i] = max(dp[i-2] + nums1[i], dp[i-1])
        res = dp[len(nums1)-1]

        dp = [0] * len(nums2)
        dp[0] = nums2[0]
        dp[1] = max(nums2[0], nums2[1])
        for i in range(2, len(nums2)):
            dp[i] = max(dp[i-2] + nums2[i], dp[i-1])
        return max(dp[len(nums2)-1], res)