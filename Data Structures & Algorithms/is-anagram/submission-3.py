class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            PreMapS, PreMapT = {}, {} # val : frequency
            for n in s:
                if n in PreMapS:
                    PreMapS[n]+=1
                else:
                    PreMapS[n] = 1
            for n in t:
                if n in PreMapT:
                    PreMapT[n]+=1
                else:
                    PreMapT[n] = 1
            return PreMapS== PreMapT

        