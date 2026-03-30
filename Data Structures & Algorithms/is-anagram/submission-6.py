class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: Sorting
        return sorted(s) == sorted(t)

        # Solution 2: Hashmap
        # return len(s) == len(t) and set(s) == set(t)

        # Solution 3: Hash Table (Using Array)

