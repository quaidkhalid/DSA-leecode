class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(nlogn) complexity by apna college lec 11, DSA series

        # nums.sort()
        # freq = 1
        # ans = nums[0]
        # n = len(nums)
        # for i in range(1, n):
        #     if nums[i] == nums[i-1]:
        #         freq += 1
                
        #     else:
        #         freq = 1
        #         ans = nums[i]

        #     if freq > (n//2):
        #         return ans
        # return ans

        #optimized approch Moore's voting algo
        freq = 0
        ans = 0
        for i in range(len(nums)):
            if freq == 0:
                ans = nums[i]
            if ans == nums[i]:
                freq += 1
            else:
                freq -= 1
        return ans