from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) :
        # Solution 1: Hash Table
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ ord(c) - ord('a') ] += 1
            res[tuple(count)].append(s)
        return list(res.values())


        # Solution 2: Sorting & Hashmap
        # {'hat': ['hat'], 'cat': ['cat', 'act'] }
        
        d = defaultdict(list)
        for str in strs:
            sort_str = "".join(sorted(str))
            d[sort_str].append(str)
        
        return [i for i in d.values()]