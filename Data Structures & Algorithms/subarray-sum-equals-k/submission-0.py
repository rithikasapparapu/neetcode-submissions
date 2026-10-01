class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            res = res + dic.get(prefix-k, 0)
            dic[prefix] = dic.get(prefix, 0) + 1
        return res

        