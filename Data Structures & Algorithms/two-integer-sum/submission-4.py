class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 4, 1, 7, 1] 5
        hash_map = {}
        for i, num in enumerate(nums):
            if target-num in hash_map:
                return [hash_map[target-num], i]
            hash_map[num] = i




        