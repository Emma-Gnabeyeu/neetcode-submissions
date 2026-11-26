class Solution:
    def rob_(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i):
            # if i==n-1:
            #    return nums[i]
            if i>=n:
                return 0
            return max(nums[i]+dfs(i+2), dfs(i+1))

        return dfs(0)
    def rob_2(self, nums: List[int]) -> int:
        n = len(nums) 
        Memo = [-1]*n #  Memoization
        def dfs(i):
            # if i==n-1:
            #    return nums[i]
            if i>=n:
                return 0
            if Memo[i] != -1:
                return Memo[i]
            Memo[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return Memo[i]

        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        if not nums: # Botom up
            return 0
        n = len(nums)
        if n==1:
            return nums[0]
        dp = [0]*n # Bottom up
        dp[0]=nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]

        