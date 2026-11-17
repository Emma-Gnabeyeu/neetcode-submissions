class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row_tab = [0]*n 
        colum_tab= [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    colum_tab[j] = 1
                    row_tab[i] = 1
        for i in range(n):
            for j in range(m):
                if row_tab[i] == 1 or colum_tab[j] == 1:
                    matrix[i][j] = 0
        

        

        
        