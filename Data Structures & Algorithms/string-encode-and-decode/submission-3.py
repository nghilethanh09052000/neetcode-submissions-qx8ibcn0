class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the position of '#'
            j = s.find('#', i)
            length = int(s[i:j])        # substring before '#' = length
            i = j + 1                   # move past '#'
            res.append(s[i:i+length])   # slice directly using length
            i += length                 # move i forward
        return res