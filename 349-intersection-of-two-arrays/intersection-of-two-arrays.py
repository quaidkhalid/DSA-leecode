class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        x = set1.intersection(set2)
        return list(x)






























        # my_dict={}
        # res = []
        # for n in nums1:
        #     if n in my_dict:
        #         my_dict[n] += 1
        #     else:
        #         my_dict[n] = 1

        # for i in nums2:
        #     if i in my_dict and my_dict[i] != 0 and i not in res:
        #         my_dict[i] -= 1
        #         res.append(i)
        # return res
        