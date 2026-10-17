class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        for i in range(len(nums)):
            scond = target - nums[i]
            if scond in prevMap:
                return [prevMap[scond], i]
            else:
                prevMap[nums[i]] = i
        return
        

