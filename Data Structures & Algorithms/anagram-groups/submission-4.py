class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for st in strs:
            ar = [0]*26
            for char in st:
                ar[ord(char)-97] += 1
            d[tuple(ar)].append(st)
        for lis in d.values():
            res.append(lis)
        return res

        


        