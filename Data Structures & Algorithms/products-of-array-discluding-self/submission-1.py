import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            data = 1
            for j in range(n):
                if i == j:
                    continue
                data *= nums[j]
            res[i] = data
        return res