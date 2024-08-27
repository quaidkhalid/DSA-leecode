class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        A = []
        zeros = [0] * row
        for i in range(col):
            A.append(zeros.copy())

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                A[c][r] = matrix[r][c]

        return A
        