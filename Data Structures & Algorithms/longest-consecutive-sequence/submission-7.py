class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        m_count = 0
        for num in seen:
            if num-1 not in seen:
                count = 1
                while num+1 in seen:
                    count += 1
                    num += 1
                m_count = max(m_count, count)
        return m_count



        