class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preMap = {} 
        for i, n in enumerate(nums):
            if n in preMap:
                return True
            else:
                preMap[n]=1
        return False
        