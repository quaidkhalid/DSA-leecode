class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        srow, erow, scol, ecol = 0, m-1, 0, n-1
        ans = []
        while srow <= erow and scol <= ecol:
            #top
            for i in range(scol, ecol+1):
                ans.append(matrix[srow][i])

            #right
            for j in range(srow+1, erow+1):
                ans.append(matrix[j][ecol])

            #bottom
            for i in range(ecol-1, scol-1, -1):
                if srow == erow:
                    break
                ans.append(matrix[erow][i])

            #left
            for j in range(erow-1, srow, -1):
                if scol == ecol:
                    break
                ans.append(matrix[j][scol])

            srow += 1
            erow -= 1
            scol += 1
            ecol -= 1

        return ans