class Solution:
    def minCostClimbingStairs_(self, cost: List[int]) -> int:
        # for i \geq 0, denote by dfs(i) the min cost to reach the top of the staircase from position i, we have : dfs(i) = cost[i] + min(dfs(i+1),dfs(i+2))
        def dfs(i): # recursion approach
            if i>= len(cost):
                return 0
            else:
                return cost[i] + min(dfs(i+1),dfs(i+2))
        return min(dfs(0),dfs(1))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up DP
        n= len(cost)
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]
            

        