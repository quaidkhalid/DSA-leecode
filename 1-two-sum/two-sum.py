class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j
        # return 
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]],i]
            else:
                my_dict[target-nums[i]] = i