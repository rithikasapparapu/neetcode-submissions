class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        total = 0
        for x in s:
            if x-1 not in s:
                count = 1
                while(x+1 in s):
                    x = x+1
                    count += 1
                total = max(total, count)
        return total
            
