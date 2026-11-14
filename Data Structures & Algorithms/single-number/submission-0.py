class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictio = {}
        for i in nums:
            if i not in dictio:
                dictio[i]=1
            else:
                dictio[i]+=1
        for i in dictio:
            if dictio[i]==1:
                return i


        