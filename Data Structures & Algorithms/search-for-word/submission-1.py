class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we opt for recursive (BFS) backtracking
        row, colum = len(board), len(board[0])
        path = set() # to avoid reusing preveous character
        def dfs(r,c, i): # i is the current character, r and c the current row and colums      
            if (i == len(word)):
                return True
            if ((r<0) or (c<0) 
                or (r>=row) or  (c>=colum) 
                or (word[i]!= board[r][c])
                or (r,c) in path): # if the r,c is inside our path set, it has already been seen.
                return False
            # now we find the character we need
            path.add((r,c))
            result = dfs(r+1,c,i+1) or dfs(r-1,c,i+1)  or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c)) # cleaning up, no need for (r,c) anymore
            return result
        # brute force, go through the table and run dfs on it
        for r in range(row):
            for c in range(colum):
                if dfs(r,c, 0):
                    return True
        return False
          
        