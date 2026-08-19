class CountSquares:

    def __init__(self):
        self.d = {}

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] = self.d.get(tuple(point), 0) + 1  

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.d:
            if abs(px - x) == abs(py - y) and px != x and py != y:
                if (px, y) in self.d and (x, py) in self.d:
                    res += self.d[(x, y)] * self.d[(px, y)] * self.d[(x, py)]
        return res


        

        
