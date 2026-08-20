class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.dic.get(key):
            self.dic[key] = [[timestamp, value]]
        else: self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lis = self.dic.get(key, [])
        l, r = 0, len(lis)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if lis[mid][0] <= timestamp:
                res = lis[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

        
