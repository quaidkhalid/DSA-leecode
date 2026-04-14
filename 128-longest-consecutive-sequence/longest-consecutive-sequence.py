class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:  My first brute force but it does not work on arry like
        #     return 0        [1,2,6,7,8]
        # res = []
        # nums.sort()
        # # print(nums)
        # for i in range(1, len(nums)):
        #     if nums[i]-nums[i-1] == 1:
        #         res.append(nums[i])
        # return len(res)+1
        num_set = set(nums)          # removes duplicates + O(1) lookup
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                current = n
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
