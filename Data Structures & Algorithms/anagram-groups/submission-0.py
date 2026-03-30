class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp_strs = []
        mp = set()

        for i in range(len(strs)):
            
            if strs[i] in mp: continue

            data = []

            for j in range(i, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    data.append(strs[j])
                    mp.add(strs[j])
            grp_strs.append(data)

        return grp_strs