class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res,count=0,0
        # for i in nums:
        #     if count==0:
        #         res = i
        #     if res ==i:
        #         count+=1
        #     else:
        #         count-=1
        # return res
        # x = []
        # for i in nums:
        #     if i in x:
        #         count += 1
        #     else:
        #         count[i] = 1
        # return count
        # O(nlogn) complexity by apna college

        nums.sort()
        freq = 1
        ans = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                freq += 1
                
            else:
                freq = 1
                ans = nums[i]

            if freq > (n//2):
                return ans
        return ans
