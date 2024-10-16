class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = nums[::2]
        odds = nums[1::2]

        for i in range(len(evens)):
            for j in range(len(evens)-i-1):
                if evens[j] > evens[j+1]:
                    evens[j],evens[j+1] = evens[j+1],evens[j]

        for i in range(len(odds)):
            for j in range(len(odds)-i-1):
                if odds[j] < odds[j+1]:
                    odds[j],odds[j+1] = odds[j+1],odds[j]


        res = []
        even_idx = 0
        odd_idx = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[even_idx])
                even_idx += 1
            else:
                res.append(odds[odd_idx])
                odd_idx += 1
        return res
        