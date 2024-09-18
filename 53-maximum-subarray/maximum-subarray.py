class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # curr_sum = 0
        # max_sum = -float('inf')
        # for num in nums:
        #     curr_sum += num
        #     max_sum = max(curr_sum, max_sum)
        #     if curr_sum < 0:
        #         curr_sum = 0
        # return max_sum

'''
this question is done by kadane's algorithm, see apna college for this algorithm
'''

        