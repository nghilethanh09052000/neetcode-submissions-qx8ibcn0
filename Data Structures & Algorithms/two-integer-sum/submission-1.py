class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            data = target - value
            if data in seen:
                return [seen[data], i]
            
            seen[value] = i