class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

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

        
