class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        prod = (nums[-1]-1) * (nums[-2]-1)
        return prod
        