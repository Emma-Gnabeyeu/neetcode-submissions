class Solution:
    def countSubstrings(self, s: str) -> int:
        num = 0 # Number of palindromes in the string
        for i in range(len(s)):
            # odd palindrome by two pointers
            left, right = i, i
            while left>=0 and right< len(s) and s[left]==s[right]:
                num += 1
                left-=1
                right+=1
            # even palindrome
            left, right = i, i+1
            while left>=0 and right< len(s) and s[left]==s[right]:
                num+=1
                left-=1
                right+=1
        return num


        