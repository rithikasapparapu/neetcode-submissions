class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # a = [1]*len(nums)
        # b = [1]*len(nums)
        # for i in range(1, len(nums)):
        #     a[i] = a[i-1]*nums[i-1]
        #     b[len(nums)-i-1] = b[len(nums)-i]*nums[len(nums)-i]
        # return [a[i]*b[i] for i in range(len(nums))]
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



        