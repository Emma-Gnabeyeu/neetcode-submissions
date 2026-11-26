class Solution:
    def rob_(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        Memo = [[-1]*2 for _ in range(len(nums))] # Memoization Top-down
        def dfs(i,index): # index ==0, we take the first elt, index=1, we drop and take the last
            if i>=len(nums) or (index==0 and i==len(nums)-1):
                return 0
            if Memo[i][index]!=-1:
                return Memo[i][index]
            Memo[i][index] = max(nums[i]+dfs(i+2, index), dfs(i+1, index))
            return Memo[i][index]
        return max(dfs(0,0),dfs(1, 1))

    def rob(self, nums: List[int]) -> int:
        def helper_func(tab: List[int]) -> int:
            if not tab:
                return O
            if len(tab)==1:
                return tab[0]
            dp = [0]*len(tab) #  Bottom-up
            dp[0] = tab[0]
            dp[1] = max(tab[0],tab[1])
            for i in range(2, len(tab)):
                dp[i] = max(tab[i]+dp[i-2], dp[i-1])
            return dp[-1]

        if len(nums)==1:
            return nums[0]
        return max(helper_func(nums[:-1]),helper_func(nums[1:]))

            

        