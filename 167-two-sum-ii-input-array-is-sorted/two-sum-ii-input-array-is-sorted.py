class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif  numbers[l] + numbers[r] > target:
                r -= 1
            else:
                res.append(l+1)
                res.append(r+1)
                return res
        

        # l = 0
        # while l < len(numbers)-1:
        #     for i in range(l+1, len(numbers)):
        #         if numbers[l] + numbers[i] == target:
        #             return [l+1, i+1]
        #     l += 1