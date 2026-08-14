class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        d = {}
        for ch in s1:
            d[ch] = d.get(ch, 0) + 1
        d1 = {}
        for k in range(0, len(s1)):
            d1[s2[k]] = d1.get(s2[k], 0) + 1
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if d1 == d:
                return True
            if r + 1 < len(s2): d1[s2[r+1]] = d1.get(s2[r+1], 0) + 1
            r += 1
            if d1.get(s2[l]) == 1:
                del d1[s2[l]]
            else:
                d1[s2[l]] = d1.get(s2[l]) - 1
            l += 1
        return False




