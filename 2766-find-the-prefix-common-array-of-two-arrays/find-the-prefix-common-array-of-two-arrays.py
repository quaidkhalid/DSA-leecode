class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # n = len(A)
        # result = [0] * n
        # # count = 0
        # for i in range(n):
        #     count = 0
        #     for A_i in range(i):
        #         for B_i in range(i):
        #             if B[B_i] == A[A_i]:
        #                 count += 1
        #                 break
        #     result[i] = count
        # return result
        n = len(A)
        ispresentA = [False] * (n+1)
        ispresentB = [False] * (n+1)
        result = [0] * n
        for i in range(n):
            ispresentA[A[i]] = True
            ispresentB[B[i]] = True
            count = 0
            for j in range(1, n+1):
                if ispresentA[j] == True and ispresentB[j] == True:
                    count += 1
            result[i] = count
        return result