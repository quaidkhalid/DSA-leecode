class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        map = {}
        count = 0
        for i in range(n):
            if A[i] in map:
                map[A[i]] += 1
            else:
                map[A[i]] = 1
            if map[A[i]] == 2:
                count += 1
            if B[i] in map:
                map[B[i]] += 1
            else:
                map[B[i]] = 1
            if map[B[i]] == 2:
                count += 1
            
            result[i] = count
        return result

        # n = len(A)
        # ispresentA = [False] * (n+1)
        # ispresentB = [False] * (n+1)
        # result = [0] * n
        # for i in range(n):
        #     ispresentA[A[i]] = True
        #     ispresentB[B[i]] = True
        #     count = 0
        #     for j in range(1, n+1):
        #         if ispresentA[j] == True and ispresentB[j] == True:
        #             count += 1
        #     result[i] = count
        # return result