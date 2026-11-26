class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        Memo = {n:1}
        def dfs(i):
            if i==n:
                return 1
            if s[i]=="0": #i == 0 and s[i]==0:
                return 0
            if i in Memo:
                return Memo[i]

            result = dfs(i+1) # in the case, we take elt i
            if i < n-1:
                if s[i]=="1" or (s[i]=="2"  and s[i+1] in "0123456"):
                    result += dfs(i+2) # either take i as a code or take i and i+1 as a code
            Memo[i] = result
            return result
        return dfs(0)