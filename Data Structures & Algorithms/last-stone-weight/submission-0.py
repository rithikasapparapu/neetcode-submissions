class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)
        while len(heap) >= 2:
            a = heap[0]
            heapq.heappop(heap)
            b = heap[0]
            heapq.heappop(heap)
            if a!=b: heapq.heappush(heap, -abs(a-b))
        if heap:
            return -heap[0]
        return 0

        