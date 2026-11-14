class Solution:
    def wordBreak_(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if (i+len(w) <= len(s)) and (w == s[i:i+len(w)]) :
                    return True and dfs(i+len(w))
            return False

        return dfs(0)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP with Memo
        Memo = {len(s): True}
        def dfs(i):
            if i in Memo:
                return Memo[i]
            
            for w in wordDict:
                if (i+len(w) <= len(s)) and (w == s[i:i+len(w)]) :
                    if dfs(i+len(w)):
                        Memo[i] = True
                        return True
            Memo[i] = False
            return False

        return dfs(0)