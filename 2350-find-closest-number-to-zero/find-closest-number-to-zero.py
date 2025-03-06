class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]
        for x in nums:
            if abs(x)<abs(closest) or (abs(x)==abs(closest) and x>closest):
                closest=x
        return closest
        