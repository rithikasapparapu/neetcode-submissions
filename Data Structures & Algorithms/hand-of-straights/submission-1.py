class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        d = {}
        for x in hand:
            d[x] = d.get(x, 0) + 1
        
        while d:
            for x in list(d):
                if not x-1 in d:
                    for i in range(groupSize):
                        if x + i not in d:
                            return False
                        if d[x + i] <= 1:
                            del d[x + i]
                        else:
                            d[x + i] -= 1
                    break
        return True





        