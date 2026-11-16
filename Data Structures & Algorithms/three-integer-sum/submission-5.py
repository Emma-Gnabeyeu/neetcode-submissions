class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers appraoch
        nums.sort() # we sort the array first, 
        result = []
        for i in range(len(nums)):  # fix one number and then search for the two others with two pointers
            if nums[i]>0 : # all remaining numbers are positives
               break
            if i>0 and nums[i]==nums[i-1]: # here we skip dupplicates as well
                continue

            j, k = i+1, len(nums)-1 #  two pointers 
            while j < k:
                my_target = - nums[i]
                if my_target < nums[j]+nums[k]:
                    k-=1
                elif my_target > nums[j]+nums[k]:
                    j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1 # increment, next element in the sorted array
                    k-=1 
                    # Let try to skip duplicate at the left pointers
                    while nums[j] == nums[j-1] and j < k: # if that next elt is equal to the preveous one.
                        j+=1
        return result


