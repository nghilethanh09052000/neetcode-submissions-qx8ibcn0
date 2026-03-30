class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: Sorting
        # return sorted(s) == sorted(t)

        # Solution 2: Hashmap
        set_s = {}
        set_t = {}

        for i in s:
            if i in set_s:
                set_s[i] += 1
            else:
                set_s[i] = 0

        for i in t:
            if i in set_t:
                set_t[i] += 1
            else:
                set_t[i] = 0
        
        if len(set_s) != len(set_t): return False

        for key, value in set_s.items():

            if key not in set_t: 
                return False
     
            if value != set_t[key]:
                return False

        return True

        # Solution 3: Hash Table (Using Array)

