class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0, len(nums)):
            l = 0
            r = len(nums)-1
            while l < r:
                if l == i: l += 1
                elif r == i: r -= 1
                elif nums[l] + nums[r] + nums[i] == 0:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
        return [list(item) for item in res]





        