class Solution:
    def searchInRow(self,matrix, target, row):
        n = len(matrix[0])
        st, end = 0, n-1
        
        while st <= end:
            mid = st + (end-st)// 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                st = mid + 1
            else:
                end = mid - 1

        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0])
        strow, endrow = 0, m-1
        
        while strow <= endrow:
            midRow = strow + (endrow - strow) // 2
            if target >= matrix[midRow][0] and target <= matrix[midRow][n-1]:
                return self.searchInRow(matrix, target, midRow)

            elif target >= matrix[midRow][n-1]:
                strow = midRow + 1
            else:
                endrow = midRow - 1

        return False
        