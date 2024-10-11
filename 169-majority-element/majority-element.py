class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        freq = 1 
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                freq += 1
            else:
                freq = 1
                ans = nums[i]

            if freq > (n//2):
                return ans
        return ans