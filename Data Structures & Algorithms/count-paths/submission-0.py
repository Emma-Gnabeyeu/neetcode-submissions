class Solution:
    def uniquePaths_(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] # DP Bottom-up , from the destination Backward.
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += dp[i + 1][j] + dp[i][j+1]
        return dp[0][0]
    
    def uniquePaths(self, m: int, n: int) -> int:
        Memo = [[-1]*n for _ in range(m)] # DP Top-dow , with memo.
        def dfs(i,j):
            if i == m-1 and j==n-1:
                return 1
            if i>=m or j >=n:
                return 0
            if Memo[i][j] !=-1:
                return Memo[i][j]
            res = dfs(i,j+1) + dfs(i+1, j)
            Memo[i][j] = res
            return res
        return dfs(0,0)