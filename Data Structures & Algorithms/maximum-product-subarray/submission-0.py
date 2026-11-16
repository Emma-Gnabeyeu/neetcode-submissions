class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we first adopt a prefix suffix approach
        n, result = len(nums), nums[0]
        prefix=0
        suffix =0 
        for i in range(n):
            if prefix !=0: # Continue extending subarrays
                prefix = nums[i]*prefix 
            else: # a zero breaks subarrays
                prefix = nums[i]
            if suffix !=0: 
                suffix = nums[n-i-1]*suffix 
            else: # a zero breaks subarrays
                suffix = nums[n-i-1]
            result  = max(result, prefix, suffix)
        return result
