class Solution:
    def maxArea(self, heights):
        area = 0
        n = len(heights)
        left = 0
        right = n-1
        while left < right:
            tempArea = min(heights[left], heights[right]) * abs(left-right)
            if tempArea > area:
                area = tempArea
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return area