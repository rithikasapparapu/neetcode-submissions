class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, x in enumerate(points):
            heapq.heappush(heap, (-(x[0]**2+x[1]**2), i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[x[1]] for x in heap]
        
        