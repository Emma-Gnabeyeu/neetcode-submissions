class Solution:
    def lengthOfLIS_(self, nums: List[int]) -> int:
        n=len(nums)
        # the recursive function return the length of the LIS up to index i
        def dfs(i,j): # j is the index of the last element included, i the current index
            if i==n:
                return 0
            
            # either we include element i or not
            exclI = dfs(i+1,j) # we don't include the element of index i 
            if j==-1 or nums[j] < nums[i]:
                LIS_i = max(exclI, 1+dfs(i+1,i) )  # we do include the element of index i 
                return LIS_i 
            else:
                return exclI
        return dfs(0,-1)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # DP with Memoization, using a 2D index
        Memo = [[-1]*(n+1) for _ in range(n)] # memo cache of size n*(n+1)
        def dfs(i,j): # j is the index of the last element included, i the current index
            if i==n:
                return 0
            if Memo[i][j+1]!=-1: # we offset by -1 since j can range from -1 to n-1
                return Memo[i][j+1]
            # either we include the current element i or not
            LIS = dfs(i+1,j) 
            if j==-1 or nums[j] < nums[i]:
                LIS = max(LIS, 1+dfs(i+1,i) )  

            Memo[i][j+1] = LIS
            return LIS 
        return dfs(0,-1)
        