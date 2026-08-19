class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        t = n
        while True:
            s = str(t)
            su = 0
            for ch in s:
                su += int(ch) ** 2
            if su == 1:
                return True
            if su in seen:
                return False
            seen.add(su)
            t = su


        