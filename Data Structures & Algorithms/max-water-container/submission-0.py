class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we adopt a sliding window approach, with two pointers
        left, right = 0, len(heights)-1
        max_amount = 0
        while left < right:
            if heights[left] < heights[right]:
                max_amount = max(max_amount, heights[left]* ( right - left))
                left+=1
            else:
                max_amount = max(max_amount, heights[right]* ( right - left))
                right-=1
        return max_amount
