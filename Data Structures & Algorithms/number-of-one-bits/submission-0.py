class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32): # iterate through the 32 possible bit
            mask = 1<<i # create a mask with a signle 1 at position i
            if (mask & n) !=0: # check if this bit is in n
                res+=1
        return res
        