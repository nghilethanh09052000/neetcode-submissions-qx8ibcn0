class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        insert_pos = 1  # first element is always unique
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:   # found a new unique element
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
