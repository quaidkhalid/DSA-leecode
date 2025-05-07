import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for i in range(len(stones)):
        #     stones[i] = stones[i] * -1
        # heapq.heapify(stones)
        # while len(stones) > 1:
        #     x = heapq.heappop(stones)
        #     y = heapq.heappop(stones)
            
        #     if y > x:
        #         heapq.heappush(stones,x-y)
        # if len(stones) > 0:
        #     return -stones[0]
        # return 0     
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if abs(first) > abs(second):
                heapq.heappush(stones, -(abs(first)-abs(second)))  

        return -stones[0] if stones else 0   