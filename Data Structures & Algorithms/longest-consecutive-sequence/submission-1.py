class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        if len(nums) == 0:
            return 0
        total = float('-inf')
        for x in s:
            t = x
            if t-1 not in s:
                count = 1
                while(t+1 in s):
                    t = t+1
                    count += 1
                total = max(total, count)
        return total
            
