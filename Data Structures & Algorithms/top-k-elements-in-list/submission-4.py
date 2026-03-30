from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Solution 1: Hashmap + Sort
        # n is len(nums),  k: top element, u: Unique element
        # In Worse case u <= n
        # d = defaultdict(int)

        # for num in nums: # O(n)
        #   d[num] += 1 # O(u)

        # sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)  # Time: O(u log u)
        # return [key for key, value in sorted_items[:k]]  # O(k)
        

        # Solution 2: Min-Heap
        
        import heapq

        d = defaultdict(int)
        heap = []
        res = []

        # { '3': 3, '2': 2, '1': 1 }
        for num in nums:
            d[num] += 1 

        for i in d.keys():
            heapq.heappush( heap, (d[i], i) )
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        # Solution 3: Bucket Sort






