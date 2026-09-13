class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for st in strs:
            res += f'{len(st)}#{st}'
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            i = j+1+count
        return res

