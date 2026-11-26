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
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        Memo = [-1]*(n+1)
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
        