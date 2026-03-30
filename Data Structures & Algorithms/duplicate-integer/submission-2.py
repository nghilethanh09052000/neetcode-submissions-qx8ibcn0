class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Solution 1: Brute Force
        # Space Complexity: O(1)
        # Time Complexity: O(n)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
              
        #         if nums[i] == nums[j]:
        #             return True
        # return False 

        # Solution 2: Hash
        return len(nums) > len(set(nums))


        # Solution 3: Hashset Length

        # Solution 4: Sorting