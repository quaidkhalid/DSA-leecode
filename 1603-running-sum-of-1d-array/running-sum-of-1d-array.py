class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add = 0
        arr = []
        for i in range(len(nums)):
            add += nums[i]
            arr.append(add)
        return arr
        
        