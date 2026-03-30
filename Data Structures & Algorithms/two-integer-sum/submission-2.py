class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

                

        # Solution 2: Sort


        # Solution 3: Hashmap
        map = {}
        for i, value in enumerate(nums):
            map[value] = i

        for i, value in enumerate(nums):
            diff = target - value
            if diff in map and map[diff] != i:
                return [i, map[diff]]
        return []
