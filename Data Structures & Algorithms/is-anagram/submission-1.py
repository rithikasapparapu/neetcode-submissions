class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0] * 26
        if len(s) != len(t):
            return False
        for chs, cht in zip(s, t):
            d[ord(chs)-97] += 1
            d[ord(cht)-97] -= 1
        if d == [0]*26:
            return True
        return False




        