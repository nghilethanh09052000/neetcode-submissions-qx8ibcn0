from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) :
        # Solution 1: Hashmap


        # Solution 2: Sorting & Hashmap
        # {'hat': ['hat'], 'cat': ['cat', 'act'] }
        
        d = defaultdict(list)
        for str in strs:
            sort_str = "".join(sorted(str))
            d[sort_str].append(str)
        
        return [i for i in d.values()]