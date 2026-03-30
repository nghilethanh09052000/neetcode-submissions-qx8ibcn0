import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        
        # Case 1: more than one zero → all results are 0
        if zero_count > 1:
            return [0] * len(nums)
        
        # Case 2: exactly one zero
        if zero_count == 1:
            total = 1
            for num in nums:
                if num != 0:
                    total *= num
            res = [0] * len(nums)
            res[nums.index(0)] = total
            return res
        
        # Case 3: no zero → safe to divide
        total = math.prod(nums)
        return [total // num for num in nums]