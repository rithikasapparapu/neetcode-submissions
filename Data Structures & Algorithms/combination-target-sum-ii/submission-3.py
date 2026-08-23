class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return         
            cur.append(candidates[i])
            total += candidates[i]
            dfs(cur, total, i+1)
            total -= candidates[i]
            cur.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(cur, total, i+1)
        dfs([], 0, 0)
        return res
        