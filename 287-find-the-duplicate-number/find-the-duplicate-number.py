class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict={}
        for i in nums:
            if i in my_dict:
                return i
            else:
                my_dict[i] = 1
        