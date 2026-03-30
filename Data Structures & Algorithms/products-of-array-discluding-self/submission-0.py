import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
        return res