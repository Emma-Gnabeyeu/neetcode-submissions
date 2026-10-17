class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr+= c.lower()
        # return newStr == newStr[::-1]
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.isAlphaNum(s[l]):
                l=l+1
            while r>l and not self.isAlphaNum(s[r]):
                r=r-1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
    def isAlphaNum(self, c):
        return ( ord('a') <= ord(c.lower()) <= ord('z') or
                  ord('0') <= ord(c) <= ord('9') )
        