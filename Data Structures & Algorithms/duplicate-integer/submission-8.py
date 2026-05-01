class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution 1: Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) ):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Solution 2: Hash Length
        # return len(set(nums)) != len(nums)


        # Solution 3: Brute Force + Hash
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False