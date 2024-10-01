class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)    #optimal code with O(1) time complexity
        ans = [1] * n
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        suffix = 1        
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix
        
        return ans




        # n = len(nums)    #optimal code but with O(n) time complexity
        # ans = [1] * n
        # prefix = [1] * n
        # suffix = [1] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]
        
        # for i in range(n):
        #     ans[i] = prefix[i] * suffix[i]
        
        # return ans


        # n = len(nums)       #brute force approach
        # ans = [1] * n
        # for i in range(n):
        #     for j in range(n):
        #         if i != j:
        #             ans[i] *= nums[j]
        # return ans