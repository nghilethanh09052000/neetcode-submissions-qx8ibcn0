class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Solution 1: Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
              
        #         if nums[i] == nums[j]:
        #             return True
        # return False 
        
        # Space Complexity: O(1)
        # Time Complexity: O(n2)

        # Solution 2: Hash

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # Space Complexity: O(n)
        # Time Complexity: O(n)
    


        # Solution 3: Hashset Length

        return len(nums) > len(set(nums))

        # Space Complexity: O(n)
        # Time Complexity: O(1)

        # Solution 4: Sorting
        # sorted_nums = sorted(nums)
        # for i in range(1, len(sorted_nums)):
    
        #     if sorted_nums[i] == sorted_nums[i-1]:
        #         return True
        # return False
        # Space Complexity: O(n) + O(logN)
        # Time Complexity: O(n)