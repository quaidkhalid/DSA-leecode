class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # zero = 0
        # r = 0
        # l = 0 
        # lenn = 0 
        # maxlen = 0
        # while r < len(nums):
        #     if nums[r] == 0:
        #         zero += 1
        #     if zero > k:
        #         while nums[l] != 0 and l < len(nums):
        #             l += 1
        #         l+=1
        #         zero -= 1
        #     else:
        #         len = r - 1 + 1
        #     maxlen = max(maxlen, lenn)    
        #     r += 1   
        # return maxlen   
        zero_count = 0
        left = 0
        right = 0
        length = 0
        max_length = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            if zero_count > k:
                while nums[left] != 0 and left < len(nums):
                    left += 1
                left += 1
                zero_count -= 1

            else:
                length = right - left + 1

            max_length = max(max_length, length)
            right += 1

        return max_length           
    
    
        