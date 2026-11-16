class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we do a binary search to find the cut
        left, right = 0, len(nums)-1
        res_min = nums[0]

        while left<=right:
            if nums[left]<nums[right]: # if the current window is already sorted, we stop
                res_min = min(res_min, nums[left])
                break

            mid = (left+right)//2
            res_min = min(res_min, nums[mid])
            if nums[mid]>=nums[left]: # the left half is sorted, search the right
                left= mid + 1
            else: # the right is sorted, search in the left
                right= mid - 1
        return res_min
        