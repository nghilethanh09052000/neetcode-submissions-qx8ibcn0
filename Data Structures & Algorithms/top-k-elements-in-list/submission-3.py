from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Solution 1: Hashmap
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_items[:k]]
        


        # Solution 2: Brute Force


        # Solution 4: Sorting


        # Solution 5: Min-Heap

        # Solution 6: Bucket Sortr