class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we transpose the matrix
        for raw in range(len(matrix)):
            for colum in range(raw+1,len(matrix[0])):
                tmp = matrix[raw][colum]
                matrix[raw][colum] = matrix[colum][raw]
                matrix[colum][raw] = tmp
        # now, we try to reverse rows
        for raw in range(len(matrix)):
            matrix[raw].reverse()

        