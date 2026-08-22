class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.lis = []
        def dfs(nums, i):
            if i == len(nums):
                self.res.append(self.lis.copy())
                return
            self.lis.append(nums[i])
            dfs(nums, i+1)
            self.lis.pop()
            dfs(nums, i+1)
        dfs(nums, 0)
        return self.res




        