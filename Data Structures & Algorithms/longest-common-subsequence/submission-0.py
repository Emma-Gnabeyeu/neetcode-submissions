class Solution:
    def longestCommonSubsequence_(self, text1: str, text2: str) -> int:
        # Brute force Recursion
        def dfs(i,j): # index i of the first string and j of the second
            if i>=len(text1) or j>=len(text2):
                return 0

            LCS = 0
            if text1[i]==text2[j]:
                LCS = 1 + dfs(i+1,j+1)
            else:
                LCS = max(dfs(i,j+1),dfs(i+1,j))
            return LCS
        return dfs(0,0)
    
    def longestCommonSubsequence_(self, text1: str, text2: str) -> int:
        # DP Memoization
        cache = [[-1]*(len(text2)) for _ in range(len(text1))] # memoization table indexed by (i,j)
        # or cache = {} and if (i,j) in cache: cache[(i,j)]
        def dfs(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if cache[i][j] !=-1:
                return cache[i][j]

            if text1[i]==text2[j]:
                cache[i][j] = 1 + dfs(i+1,j+1)
            else:
                cache[i][j] = max(dfs(i,j+1),dfs(i+1,j))

            return cache[i][j]
        return dfs(0,0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP Tabulation, reversed Bottom-up 
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)] #  table indexed by (i,j)
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] 
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]

        