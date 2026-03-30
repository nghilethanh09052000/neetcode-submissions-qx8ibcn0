class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        # 1. Map character frequencies of s1
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        # 2. Map the first window of s2 (same length as s1)
        window = {}
        for i in range(n1):
            window[s2[i]] = window.get(s2[i], 0) + 1

        # 3. Check if the first window is a match
        if window == target:
            return True

        # 4. Slide the window
        for i in range(n1, n2):
            # Add the character entering from the right
            new_char = s2[i]
            window[new_char] = window.get(new_char, 0) + 1
            
            # Remove the character leaving from the left
            old_char = s2[i - n1]
            if window[old_char] == 1:
                del window[old_char] # Clean up to keep dictionary small
            else:
                window[old_char] -= 1

            # Check if the updated window matches
            if window == target:
                return True

        return False