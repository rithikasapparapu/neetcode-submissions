class Solution:
    def key_of(self, s):
        lis = [0] * 26
        for ch in s:
            lis[ord(ch)-97] += 1
        return tuple(lis)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            if self.key_of(s) in d:
                d[self.key_of(s)].append(s)
            else:
                d[self.key_of(s)] = [s]
        res = []
        for lis in d.values():
            res.append(lis)
        return res


        