class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        newset = set(nums)
        for num in newset:
            if nums.count(num) == 1:
                return num
        