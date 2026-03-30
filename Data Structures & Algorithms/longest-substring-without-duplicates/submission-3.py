class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        max_length = 0

        for R in range(len(s)):
            while s[R] in seen:   # shrink window until no duplicate
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            max_length = max(max_length, R - L + 1)

        return max_length