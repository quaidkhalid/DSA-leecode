class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        map = {}
        for num in nums1:
            map[num] = map.get(num, 0) + n
        for num in nums2:
            map[num] = map.get(num,0) + m

        res = 0
        for num in map:
            if map[num] % 2 != 0:
                res ^= num
        return res

        