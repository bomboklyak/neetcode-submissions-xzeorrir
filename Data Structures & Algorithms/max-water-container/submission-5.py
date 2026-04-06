class Solution:
    def maxArea(self, heights):
        area = 0
        n = len(heights)
        left = 0
        right = n-1
        while left < right:
            if heights[left] <= heights[right]:
                tempArea = heights[left] * (right-left)
                left += 1
            else:
                tempArea = heights[right] * (right-left)
                right -= 1
            if tempArea > area:
                area = tempArea
        return area