class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num] +=1
                continue
            res[num] = 1
        data = dict(sorted(res.items(), key = lambda x: x[1], reverse=True))
        return list(data.keys())[:k]