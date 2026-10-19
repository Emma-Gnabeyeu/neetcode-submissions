class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        pw2 = 0 # this variable keep track of the recent power of two
        for i in range(1,n+1):
            if i == 2**(pw2 + 1) :
                dp[i] = 1
                pw2 +=1
            else:
                dp[i] = 1 + dp[i-2**pw2]
        return dp
