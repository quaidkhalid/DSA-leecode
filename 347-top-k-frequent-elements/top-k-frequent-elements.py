class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dictt:
                dictt[nums[i]] = 1
            else:
                dictt[nums[i]] += 1
        print(dictt)
        heap = []
        for key, value in dictt.items():
            heapq.heappush(heap,(-value, key))
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
        