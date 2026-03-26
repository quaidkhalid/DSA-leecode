class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False

        