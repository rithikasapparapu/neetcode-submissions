class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        seen = set()
        count = 0
        for ch in s:
            count += 1
            d[ch] -= 1
            seen.add(ch)
            if d[ch] == 0:
                seen.remove(ch)
            if not seen:
                res.append(count)
                count = 0
        return res


        