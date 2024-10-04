class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for val in points:
            curr = val[0]**2 + val[1]**2
            heapq.heappush(heap,(curr, val))
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res
        