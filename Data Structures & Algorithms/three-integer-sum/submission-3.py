class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i<len(nums):
            while i!=0 and i<len(nums) and nums[i] == nums[i-1]:
                i += 1
            k, l = i+1, len(nums)-1
            while k<l:
                if nums[k] + nums[l] + nums[i] == 0:
                    res.append([nums[i], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k<l and nums[k] == nums[k-1] and nums[l] == nums[l+1]:
                        k += 1
                        l -= 1
                elif nums[k] + nums[l] + nums[i] < 0:
                    k += 1
                else:
                    l -= 1
            i += 1
        return res
            


        