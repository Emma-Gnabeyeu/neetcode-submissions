class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        palin = s[0]
        for i in range(len(s)): # i is the center of the palindrome
            # odd length
            left, right = i, i
            while left >=0 and right <len(s) and s[left]==s[right]:
                if len(s[left:right+1]) > len(palin):
                    palin = s[left:right+1]
                left-=1
                right+=1
            # even length
            left, right = i, i+1
            while left >=0 and right <len(s) and s[left]==s[right]:
                if len(s[left:right+1]) > len(palin):
                    palin = s[left:right+1]
                left-=1
                right+=1
        return palin




        