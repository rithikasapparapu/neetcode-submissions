class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_count = 0
        tot = 0
        for r, ch in enumerate(s):
            d[ch] = d.get(ch, 0) + 1
            max_count = max(max_count, d[ch])
            while (r-l+1) - max_count > k:
                d[s[l]] -= 1
                l += 1 
            tot = max(tot, r-l+1)
        return tot


        