class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0, count1, count2= 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 1

        idx = 0
        for r in range(count0):
            nums[idx] = 0
            idx += 1

        for w in range(count1):
            nums[idx] = 1
            idx += 1

        for b in range(count2):
            nums[idx] = 2
            idx += 1

        return nums
        
        """
        Do not return anything, modify nums in-place instead.
        """
        