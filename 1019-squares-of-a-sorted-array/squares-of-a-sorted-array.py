class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = pow(nums[i],2)
        # res = sorted(nums)
        # return res 
        res = []
        left , right = 0 , len(nums) - 1

        while left <= right:
            if (nums[left]**2) < (nums[right]**2):
                res.append(nums[right]**2)
                right -= 1
            else:
                res.append(nums[left]**2)
                left += 1
        return res[::-1]
        