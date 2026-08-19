class Solution:
    # could not solve by myself, took hint
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_count = 0
        tot = 0
        for r, ch in enumerate(s):
            d[ch] = d.get(ch, 0) + 1
            while (r-l+1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1 
            tot = max(tot, r-l+1)
        return tot


        