class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum += i
        leftsum = 0
        rightsum = 0
        maxsplit = 0
        for i in range(len(nums)-1):
            leftsum += nums[i]
            rightsum = sum - leftsum
            if leftsum >= rightsum:
                maxsplit += 1

        return maxsplit
        