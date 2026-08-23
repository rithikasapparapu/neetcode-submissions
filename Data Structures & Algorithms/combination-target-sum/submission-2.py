class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return         
            cur.append(nums[i])
            total += nums[i]
            dfs(cur, total, i)
            total -= nums[i]
            cur.pop()
            i += 1
            dfs(cur, total, i)
        dfs([], 0, 0)
        return res


        